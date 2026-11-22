import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import json
from treatments import get_treatment_info

st.set_page_config(page_title="Plant Disease AI", page_icon="🌿", layout="centered")
st.title("🌿 Plant Disease AI & Treatment Advisor")
st.write("Take or upload a photo of a plant leaf for an instant diagnosis (**98.36% accuracy across 121 classes**) and a tailored treatment plan.")

model_path = "best_plant_model.pth"
classes_json = "class_names.json"

with open(classes_json, "r") as f:
    class_names = json.load(f)

num_classes = len(class_names)

@st.cache_resource
def load_model(num_cls):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.efficientnet_b0(weights=None)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_cls)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model, device

model, device = load_model(num_classes)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

uploaded_file = st.file_uploader("Snap or upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(image, caption="Uploaded Leaf", use_container_width=True)
        
    with col2:
        with st.spinner("Analyzing leaf patterns..."):
            image_tensor = transform(image).unsqueeze(0).to(device)
            with torch.no_grad():
                outputs = model(image_tensor)
                probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
                top3_prob, top3_idx = torch.topk(probabilities, 3)
                
        top_raw_class = class_names[top3_idx[0].item()]
        top_clean_name = top_raw_class.replace("_", " ").title()
        top_conf = top3_prob[0].item() * 100
        
        st.subheader("Top 3 Diagnoses")
        for i in range(3):
            cls_name = class_names[top3_idx[i].item()].replace("_", " ").title()
            prob = top3_prob[i].item() * 100
            st.write(f"**{i+1}. {cls_name}** — {prob:.2f}%")
            st.progress(min(max(int(prob), 1), 100))

    st.divider()

    info = get_treatment_info(top_raw_class)
    
    if info["status"] == "healthy":
        st.success(f"### ✅ {top_clean_name} ({top_conf:.1f}% Confidence)")
    else:
        st.error(f"### ⚠️ Detected: {top_clean_name} ({top_conf:.1f}% Confidence)")
        
    st.markdown(f"**Primary Cause:** {info['cause']}")
    st.markdown(f"**Key Symptoms:** {info['symptoms']}")
    
    tab1, tab2, tab3 = st.tabs(["🌱 Organic Control", "🧪 Chemical Treatment", "🛡️ Prevention & Care"])
    
    with tab1:
        st.info(info["organic"])
    with tab2:
        st.warning(info["chemical"])
    with tab3:
        st.success(info["prevention"])