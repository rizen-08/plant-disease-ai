# treatments.py
# Comprehensive treatment & management database for curated plant diseases

TREATMENT_DB = {
    # --- APPLE ---
    "apple_scab": {
        "cause": "Fungus (Venturia inaequalis)",
        "symptoms": "Olive-green to brown velvety spots on leaves and fruit; leaves may yellow and drop early.",
        "organic": "Rake and destroy fallen leaves in autumn. Apply sulfur, lime-sulfur, or neem oil sprays during bud break.",
        "chemical": "Apply preventative fungicides such as Captan, Myclobutanil, or Mancozeb from green-tip through petal fall.",
        "prevention": "Prune trees to open the canopy and improve airflow. Plant scab-resistant cultivars."
    },
    "apple_black_rot": {
        "cause": "Fungus (Botryosphaeria obtusa)",
        "symptoms": "Purple flecks on leaves enlarging into 'frogeye' spots with tan centers; black mummified fruit.",
        "organic": "Prune out dead wood, cankers, and mummified fruit. Apply copper-based fungicides or sulfur sprays.",
        "chemical": "Apply Captan or Thiophanate-methyl sprays starting at silver tip and repeating every 10–14 days.",
        "prevention": "Sanitize pruning tools with 70% alcohol between cuts and remove all orchard debris."
    },
    "apple_cedar_rust": {
        "cause": "Fungus (Gymnosporangium juniperi-virginianae)",
        "symptoms": "Bright yellow-orange spots on upper leaf surfaces with tiny black dots in the center.",
        "organic": "Remove nearby Eastern red cedar or juniper hosts within a 300-meter radius if possible. Spray sulfur or copper.",
        "chemical": "Apply Myclobutanil, Fenarimol, or Mancozeb at pink-bud stage through early summer.",
        "prevention": "Plant rust-resistant apple varieties and inspect nearby junipers for orange gelatinous galls in spring."
    },

    # --- BELL PEPPER ---
    "bell_pepper_bacterial_spot": {
        "cause": "Bacterium (Xanthomonas campestris pv. vesicatoria)",
        "symptoms": "Small, water-soaked dark brown spots on leaves and raised scabby spots on fruit.",
        "organic": "Spray fixed copper bactericides mixed with neem oil. Remove severely infected lower leaves.",
        "chemical": "Apply copper hydroxide combined with Mancozeb to slow bacterial resistance.",
        "prevention": "Use certified disease-free seed, practice a 2–3 year crop rotation, and avoid overhead sprinkler irrigation."
    },

    # --- CHERRY ---
    "cherry_powdery_mildew": {
        "cause": "Fungus (Podosphaera clandestina)",
        "symptoms": "White powdery fungal growth on young leaves, causing curling, stunting, and distortion.",
        "organic": "Spray potassium bicarbonate, neem oil, or horticultural sulfur at the first sign of white powder.",
        "chemical": "Apply Myclobutanil, Trifloxystrobin, or Tebuconazole at shuck fall and repeat every 14 days.",
        "prevention": "Prune trees to maximize sunlight penetration and avoid excessive nitrogen fertilizer."
    },

    # --- CORN (MAIZE) ---
    "corn_common_rust": {
        "cause": "Fungus (Puccinia sorghi)",
        "symptoms": "Brick-red to cinnamon-brown oval pustules on both upper and lower leaf surfaces.",
        "organic": "Apply sulfur or copper-based foliar sprays early if weather is cool and humid.",
        "chemical": "Apply Azoxystrobin, Propiconazole, or Pyraclostrobin if pustules appear before tasseling.",
        "prevention": "Plant resistant hybrids and avoid late planting dates."
    },
    "corn_gray_leaf_spot": {
        "cause": "Fungus (Cercospora zeae-maydis)",
        "symptoms": "Long, narrow, rectangular tan-to-gray lesions bounded by leaf veins.",
        "organic": "Bury infected crop residue through deep tillage after harvest to speed up decomposition.",
        "chemical": "Apply strobilurin or triazole fungicides (e.g., Pyraclostrobin + Metconazole) at tasseling (VT/R1).",
        "prevention": "Rotate out of corn for at least 1–2 years and select hybrids with high GLS resistance ratings."
    },
    "corn_northern_leaf_blight": {
        "cause": "Fungus (Exserohilum turcicum)",
        "symptoms": "Large, cigar-shaped grayish-green to tan lesions (2.5 to 15 cm long) on lower leaves first.",
        "organic": "Manage crop debris via tillage and rotate with non-host crops like soybean or legumes.",
        "chemical": "Foliar application of Propiconazole, Azoxystrobin, or Mancozeb when lesions reach the ear leaf.",
        "prevention": "Use hybrids carrying Ht resistance genes and manage field drainage."
    },

    # --- GRAPE ---
    "grape_black_rot": {
        "cause": "Fungus (Guignardia bidwellii)",
        "symptoms": "Reddish-brown circular leaf spots with black borders; berries shrivel into hard black mummies.",
        "organic": "Remove all mummified berries during winter dormancy. Spray Bordeaux mixture or copper + sulfur.",
        "chemical": "Apply Mancozeb, Myclobutanil, or Captan from early shoot growth through 4 weeks post-bloom.",
        "prevention": "Open the vine canopy via leaf pulling around fruit clusters to speed up drying after rain."
    },
    "grape_esca_black_measles": {
        "cause": "Fungal Complex (Phaeomoniella chlamydospora & Phaeoacremonium spp.)",
        "symptoms": "'Tiger-stripe' interveinal chlorosis and necrosis on leaves; dark purple/black spotting on berries.",
        "organic": "Cut out infected cordons below wood staining during dry winter weather. Seal pruning wounds with Trichoderma paste.",
        "chemical": "No curative foliar fungicide exists; protect pruning wounds with Topsin-M (Thiophanate-methyl) or boric acid paste.",
        "prevention": "Never prune during rainy periods; burn or remove dead vine wood from the vineyard immediately."
    },
    "grape_isariopsis_leaf_spot": {
        "cause": "Fungus (Pseudocercospora vitis)",
        "symptoms": "Irregular dark brown to black angular blotches on leaves, mostly starting in the lower canopy late in the season.",
        "organic": "Apply copper oxychloride or potassium bicarbonate sprays and rake fallen leaves.",
        "chemical": "Apply Mancozeb, Carbendazim, or Azoxystrobin at 14-day intervals if defoliation threatens ripening.",
        "prevention": "Maintain good trellis ventilation and weed control beneath vines."
    },

    # --- ORANGE / CITRUS ---
    "orange_citrus_greening": {
        "cause": "Bacterium (Candidatus Liberibacter spp.) spread by the Asian Citrus Psyllid",
        "symptoms": "Blotchy asymmetrical yellowing of leaves (mottling), stunted growth, lopsided bitter fruit that stays green at the bottom.",
        "organic": "Control psyllid vectors using neem oil, insecticidal soaps, or kaolin clay. Introduce natural predators (Tamarixia radiata).",
        "chemical": "Manage Asian Citrus Psyllid populations with systemic insecticides (Imidacloprid, Thiamethoxam). Remove confirmed infected trees.",
        "prevention": "Only plant certified disease-free nursery stock and inspect new flush shoots regularly for psyllid nymphs."
    },

    # --- PEACH ---
    "peach_bacterial_spot": {
        "cause": "Bacterium (Xanthomonas arboricola pv. pruni)",
        "symptoms": "Angular purple-to-black spots on leaves whose centers fall out ('shot-hole' appearance); pitted spots on fruit.",
        "organic": "Apply fixed copper sprays at dormant bud swell and leaf drop in autumn.",
        "chemical": "Apply Oxytetracycline or low-rate copper formulations from shuck split through summer.",
        "prevention": "Maintain balanced tree vigor with proper nitrogen/potassium levels and windbreaks to reduce sandblasting wounds."
    },

    # --- POTATO ---
    "potato_early_blight": {
        "cause": "Fungus (Alternaria solani)",
        "symptoms": "Dark brown circular lesions with concentric 'target-board' rings, starting on older lower leaves.",
        "organic": "Apply copper fungicide or Bacillus subtilis bio-fungicide. Mulch soil to prevent spore splash.",
        "chemical": "Apply Chlorothalonil, Mancozeb, or Azoxystrobin every 7–10 days once lesions appear.",
        "prevention": "Avoid nitrogen/phosphorus deficiency (weak plants are highly susceptible) and rotate crops for 2+ years."
    },
    "potato_late_blight": {
        "cause": "Oomycete Water Mold (Phytophthora infestans)",
        "symptoms": "Large, dark green to black water-soaked blotches on leaves with white cottony growth on undersides in humid weather.",
        "organic": "Immediately destroy infected foliage. Apply fixed copper sprays preventatively during cool, wet weather.",
        "chemical": "Urgent application of Metalaxyl/Mefenoxam, Cymoxanil, Mandipropamid, or Chlorothalonil.",
        "prevention": "Plant certified disease-free seed tubers, eliminate volunteer potatoes, and kill vines 2 weeks before harvest."
    },

    # --- RICE ---
    "rice_brown_spot": {
        "cause": "Fungus (Bipolaris oryzae)",
        "symptoms": "Small oval brown lesions with gray centers and yellow halos across leaf blades and glumes.",
        "organic": "Correct soil potassium, silicon, and zinc deficiencies. Treat seeds with hot water (53°C for 10 mins) or Trichoderma.",
        "chemical": "Spray Propiconazole, Iprobenfos, or Mancozeb + Carbendazim at tillering and booting stages.",
        "prevention": "Maintain balanced soil fertility—brown spot thrives in nutrient-depleted or drought-stressed paddies."
    },
    "rice_leaf_blast": {
        "cause": "Fungus (Magnaporthe oryzae)",
        "symptoms": "Diamond- or spindle-shaped lesions with gray/white centers and reddish-brown borders.",
        "organic": "Avoid excess nitrogen top-dressing. Apply Pseudomonas fluorescens or Neem cake to soil.",
        "chemical": "Apply Tricyclazole, Isoprothiolane, or Azoxystrobin immediately upon spotting spindle lesions.",
        "prevention": "Keep consistent flood water depth (draining fields increases blast severity) and use blast-resistant varieties."
    },
    "rice_neck_blast": {
        "cause": "Fungus (Magnaporthe oryzae)",
        "symptoms": "Grayish-brown necrotic rotting at the panicle neck node, causing the grain head to snap or turn white ('whitehead').",
        "organic": "Split nitrogen applications and apply silicon soil amendments to strengthen stem and neck tissues.",
        "chemical": "Preventative spray of Tricyclazole (75% WP) or Edifenphos at 5% panicle emergence (booting/heading).",
        "prevention": "Destroy infected straw and stubble after harvest and avoid late-season nitrogen spikes."
    },
    "rice_hispa": {
        "cause": "Insect Pest (Dicladispa armigera - Spiny Black Beetle)",
        "symptoms": "White parallel streaks on leaves where beetles scrape green chlorophyll; larvae tunnel inside leaf tissues.",
        "organic": "Clip and destroy leaf tips during transplanting. Spray neem seed kernel extract (NSKE 5%).",
        "chemical": "Apply Chlorpyrifos, Quinalphos, or Lambda-cyhalothrin if damage exceeds 1–2 adults/grubs per hill.",
        "prevention": "Clear grassy weeds from field bunds and avoid over-fertilizing with nitrogen."
    },

    # --- SOYBEAN ---
    "soybean_caterpillar": {
        "cause": "Insect Pest (Anticarsia gemmatalis / Defoliating Caterpillars)",
        "symptoms": "Irregular holes and skeletonized leaves; heavy infestations strip upper canopy leaves.",
        "organic": "Spray Bacillus thuringiensis (Bt) or Baculovirus anticarsia while caterpillars are small (<1.5 cm).",
        "chemical": "Apply Chlorantraniliprole, Spinosad, or Indoxacarb if defoliation reaches 30% pre-bloom or 15% pod-fill.",
        "prevention": "Preserve natural predators (ground beetles, parasitic wasps) by avoiding broad-spectrum pyrethroids early."
    },
    "soybean_diabrotica_speciosa": {
        "cause": "Insect Pest (Cucurbit Beetle - Diabrotica speciosa)",
        "symptoms": "Small circular 'shot-hole' feeding perforations across tender soybean leaflets.",
        "organic": "Apply neem oil, Beauveria bassiana entomopathogenic fungus, or kaolin clay deterrents.",
        "chemical": "Apply Thiamethoxam + Lambda-cyhalothrin or Acephate if defoliation thresholds are exceeded.",
        "prevention": "Use insecticidal seed treatments to protect emerging seedlings from root-feeding larvae."
    },

    # --- SQUASH & STRAWBERRY ---
    "squash_powdery_mildew": {
        "cause": "Fungus (Podosphaera xanthii / Erysiphe cichoracearum)",
        "symptoms": "Talcum-like white powder covering upper and lower leaf surfaces, leading to premature leaf drying.",
        "organic": "Spray potassium bicarbonate, neem oil, or a 1:9 milk-to-water solution in early morning.",
        "chemical": "Apply Myclobutanil, Chlorothalonil, or Sulfur (do not apply sulfur above 30°C to avoid leaf burn).",
        "prevention": "Space hills generously for airflow and water at the base of the plant rather than wetting foliage."
    },
    "strawberry_leaf_scorch": {
        "cause": "Fungus (Diplocarpon earliana)",
        "symptoms": "Numerous irregular dark purple blotches that merge until the entire leaf turns reddish-purple and dries up ('scorched').",
        "organic": "Mow and remove old infected foliage after harvest renovation. Apply copper or potassium bicarbonate.",
        "chemical": "Apply Captan, Thiram, or Myclobutanil at 10–14 day intervals during spring blossom and autumn growth.",
        "prevention": "Renew strawberry beds every 2–3 years, use drip irrigation, and ensure well-drained soil."
    },

    # --- TOMATO ---
    "tomato_bacterial_spot": {
        "cause": "Bacterium (Xanthomonas spp.)",
        "symptoms": "Small, dark, greasy-looking spots on leaves and stems; raised scabby spots on green fruit.",
        "organic": "Apply copper octanoate or Bacillus amyloliquefaciens bio-bactericide. Prune lower leaves.",
        "chemical": "Tank-mix Copper Hydroxide + Mancozeb every 7–10 days during warm, rainy weather.",
        "prevention": "Mulch around plants to stop soil splash, never touch wet plants, and stake vines upright."
    },
    "tomato_early_blight": {
        "cause": "Fungus (Alternaria linariae / Alternaria solani)",
        "symptoms": "Bullseye-patterned brown spots with yellow halos starting on the oldest bottom leaves first.",
        "organic": "Prune off the bottom 15–20 cm of leaves once the plant establishes. Spray copper or neem oil.",
        "chemical": "Apply Chlorothalonil, Mancozeb, or Azoxystrobin every 7–14 days.",
        "prevention": "Apply thick straw/plastic mulch to block soil-borne spores from splashing onto lower leaves."
    },
    "tomato_late_blight": {
        "cause": "Oomycete Water Mold (Phytophthora infestans)",
        "symptoms": "Rapidly expanding pale-green to brown irregular blotches on leaves, darkened stems, and greasy brown fruit rot.",
        "organic": "Pull and bag severely infected plants immediately. Spray preventative copper fungicide on healthy neighbors.",
        "chemical": "Apply Chlorothalonil, Mandipropamid, or Cymoxanil + Famoxadone immediately.",
        "prevention": "Water strictly at soil level in the morning, space plants wide apart, and use resistant varieties (e.g., 'Defiant', 'Mountain Magic')."
    },
    "tomato_leaf_mold": {
        "cause": "Fungus (Passalora fulva / Cladosporium fulvum)",
        "symptoms": "Pale yellow spots on upper leaf surfaces with olive-green to velvety purple mold directly underneath.",
        "organic": "Increase greenhouse ventilation immediately to drop humidity below 85%. Spray potassium bicarbonate or copper.",
        "chemical": "Apply Chlorothalonil, Mancozeb, or Difenoconazole.",
        "prevention": "Space plants widely, prune excess foliage, and run fans in high tunnels/greenhouses."
    },
    "tomato_septoria_spot": {
        "cause": "Fungus (Septoria lycopersici)",
        "symptoms": "Dozens of tiny circular spots (1.5–3 mm) with dark brown borders and tan/gray centers dotted with black specks.",
        "organic": "Remove infected lower leaves and apply copper fungicide or Serenade (Bacillus subtilis) every 7 days.",
        "chemical": "Apply Chlorothalonil or Mancozeb at first symptom appearance.",
        "prevention": "Remove all nightshade weeds (horsenettle, nightshade), mulch heavily, and rotate crops for 2+ years."
    },
    "tomato_spider_mites": {
        "cause": "Arachnid Pest (Tetranychus urticae - Two-Spotted Spider Mite)",
        "symptoms": "Tiny yellow/white stippling dots on leaves, bronze discoloration, and fine silk webbing under leaves.",
        "organic": "Blast undersides of leaves with a strong water spray. Apply neem oil, insecticidal soap, or release predatory mites (Phytoseiulus persimilis).",
        "chemical": "Apply targeted miticides such as Abamectin, Bifenazate, or Spiromesifen (avoid broad pyrethroids as they trigger mite outbreaks).",
        "prevention": "Keep plants well-watered and mist dusty pathways—spider mites thrive in hot, dry, dusty conditions."
    },
    "tomato_target_spot": {
        "cause": "Fungus (Corynespora cassiicola)",
        "symptoms": "Brown necrotic lesions with subtle concentric rings on leaves and sunken brown pitted lesions on fruit.",
        "organic": "Prune lower canopy to increase airflow and apply copper hydroxide sprays.",
        "chemical": "Apply Azoxystrobin, Boscalid, Chlorothalonil, or Difenoconazole.",
        "prevention": "Avoid overhead irrigation and destroy crop debris promptly after final harvest."
    },
    "tomato_mosaic_virus": {
        "cause": "Virus (Tomato Mosaic Virus - ToMV / TMV)",
        "symptoms": "Light and dark green mottled 'mosaic' pattern on leaves, fern-like curled leaflets, and internal browning of fruit.",
        "organic": "No cure exists once infected. Carefully uproot and bag infected plants to prevent contact spread.",
        "chemical": "Viruses cannot be cured with chemical sprays. Disinfect stakes and pruning shears in a 10% bleach or trisodium phosphate solution.",
        "prevention": "Wash hands with soap before handling plants (especially if handling tobacco products) and plant ToMV-resistant varieties."
    },
    "tomato_yellow_leaf_curl_virus": {
        "cause": "Virus (TYLCV) transmitted by Silverleaf Whiteflies (Bemisia tabaci)",
        "symptoms": "Upward curling and cupping of small leaves, bright yellow leaf margins, severe stunting, and flower drop.",
        "organic": "Use yellow sticky traps and reflective silver plastic mulch to repel whiteflies. Spray neem oil or insecticidal soap.",
        "chemical": "Control whitefly vectors with Imidacloprid, Pyriproxyfen, or Cyantraniliprole. Rogue out infected plants early.",
        "prevention": "Install 50-mesh insect netting in nurseries and plant TYLCV-resistant hybrids."
    }
}


def get_treatment_info(class_name: str) -> dict:
    """Returns structured treatment advice for any predicted class name."""
    key = class_name.lower().strip()

    # 1. Healthy Leaf Check
    if "healthy" in key:
        plant = key.replace("_healthy", "").replace("_", " ").title()
        return {
            "status": "healthy",
            "cause": "No pathogen detected — Leaf appears healthy!",
            "symptoms": f"Normal, vibrant {plant} foliage with no visible lesions, chlorosis, or pest damage.",
            "organic": "Continue regular watering at the soil level and apply balanced organic compost or seaweed extract.",
            "chemical": "No chemical treatment needed! Avoid unnecessary pesticide applications to protect beneficial insects.",
            "prevention": "Inspect undersides of leaves weekly, maintain good spacing for airflow, and keep soil mulched."
        }

    # 2. Exact Match in Database
    if key in TREATMENT_DB:
        data = TREATMENT_DB[key].copy()
        data["status"] = "diseased"
        return data

    # 3. Smart Keyword Fallback (for remaining secondary classes)
    if "rust" in key:
        return {
            "status": "diseased",
            "cause": "Fungal Rust Pathogen (Puccinia / Uromyces spp.)",
            "symptoms": "Orange, yellow, or reddish-brown powdery spore pustules on leaf surfaces.",
            "organic": "Remove heavily infected leaves and spray sulfur or copper fungicide early.",
            "chemical": "Apply triazole or strobilurin fungicides (e.g., Tebuconazole, Myclobutanil, Azoxystrobin).",
            "prevention": "Water at the base of the plant in the morning and improve airflow between rows."
        }
    elif "mildew" in key:
        return {
            "status": "diseased",
            "cause": "Fungal Mildew Pathogen (Powdery or Downy Mildew)",
            "symptoms": "Powdery white surface patches or yellowish angular spots with fuzzy growth underneath.",
            "organic": "Spray potassium bicarbonate, neem oil, or copper soap.",
            "chemical": "Apply Myclobutanil or Sulfur (for powdery mildew) or Mancozeb/Chlorothalonil (for downy mildew).",
            "prevention": "Reduce humidity around leaves, prune dense foliage, and avoid evening overhead watering."
        }
    elif "bacterial" in key or "wilt" in key:
        return {
            "status": "diseased",
            "cause": "Bacterial Plant Pathogen (Xanthomonas / Pseudomonas / Erwinia spp.)",
            "symptoms": "Water-soaked angular leaf spots, yellow halos, or rapid wilting of stems.",
            "organic": "Apply fixed copper bactericide sprays and remove infected plant parts immediately with sterilized shears.",
            "chemical": "Apply Copper Hydroxide tank-mixed with Mancozeb.",
            "prevention": "Never work in the garden when foliage is wet, sanitize tools with 70% alcohol, and rotate crops."
        }
    elif "virus" in key or "mosaic" in key or "bunchy" in key:
        return {
            "status": "diseased",
            "cause": "Plant Virus (often transmitted by aphids, whiteflies, or thrips)",
            "symptoms": "Mottled yellow/green mosaic patterns, leaf curling, distortion, and stunted plant growth.",
            "organic": "Remove and destroy infected plants to protect healthy neighbors. Control insect vectors with neem oil or sticky traps.",
            "chemical": "Viruses cannot be cured chemically. Manage sucking insect vectors (aphids/whiteflies) with targeted insecticides.",
            "prevention": "Use certified virus-free seeds/transplants, control weeds, and disinfect tools regularly."
        }
    else:
        return {
            "status": "diseased",
            "cause": "Fungal Leaf Spot / Blight Pathogen",
            "symptoms": "Necrotic brown or black lesions, spots, or blighting across leaf tissue.",
            "organic": "Prune affected leaves, apply mulch to prevent soil splash, and spray copper fungicide or neem oil.",
            "chemical": "Apply a broad-spectrum protectant fungicide such as Chlorothalonil, Mancozeb, or Azoxystrobin.",
            "prevention": "Practice crop rotation, clear infected crop debris at the end of the season, and use drip irrigation."
        }