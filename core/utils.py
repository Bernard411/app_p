def diagnose_plant(leaf_color, leaf_shape, spots_on_leaves, wilting, mold_growth, stem_condition, soil_type, weather_conditions, watering_frequency, pest_presence, fertilizer_use):
    # Initialize diagnosis result and recommendations
    diagnosis_result = None
    recommendations = None

    # Example of diagnostic rules
    if leaf_color == "yellow" and spots_on_leaves:
        diagnosis_result = {
            "name": "Leaf Spot Disease",
            "symptoms": "Yellowing leaves with spots.",
            "risk_factors": "High humidity and poor air circulation.",
            "prevention": "Ensure proper spacing between plants.",
            "treatment": "Apply a fungicide if necessary."
        }
        recommendations = "Ensure proper spacing between plants to improve air circulation and reduce humidity. Apply a fungicide if necessary."
    elif wilting and mold_growth:
        diagnosis_result = {
            "name": "Blight",
            "symptoms": "Wilting and mold growth.",
            "risk_factors": "Overhead watering and poor soil drainage.",
            "prevention": "Avoid overhead watering.",
            "treatment": "Remove and destroy affected plants. Improve soil drainage."
        }
        recommendations = "Remove and destroy affected plants. Avoid overhead watering and improve soil drainage."
    elif leaf_color == "yellow" and stem_condition == "soft":
        diagnosis_result = {
            "name": "Root Rot",
            "symptoms": "Yellowing leaves and soft stem.",
            "risk_factors": "Poor soil drainage and overwatering.",
            "prevention": "Improve soil drainage.",
            "treatment": "Reduce watering. Consider using a fungicide."
        }
        recommendations = "Improve soil drainage and reduce watering. Consider using a fungicide."
    elif leaf_shape == "curled" and spots_on_leaves:
        diagnosis_result = {
            "name": "Curling Leaf Disease",
            "symptoms": "Curled leaves with spots.",
            "risk_factors": "Virus spread by insects.",
            "prevention": "Control insect population.",
            "treatment": "Apply appropriate insecticide."
        }
        recommendations = "Control insect population. Apply appropriate insecticide."
    elif mold_growth and soil_type == "clay":
        diagnosis_result = {
            "name": "Soil Mold",
            "symptoms": "Mold growth in soil.",
            "risk_factors": "Poor soil aeration and drainage.",
            "prevention": "Improve soil aeration.",
            "treatment": "Use soil fungicide."
        }
        recommendations = "Improve soil aeration. Use soil fungicide."
    elif wilting and weather_conditions == "hot":
        diagnosis_result = {
            "name": "Heat Stress",
            "symptoms": "Wilting during hot weather.",
            "risk_factors": "High temperatures and direct sunlight.",
            "prevention": "Provide shade and adequate water.",
            "treatment": "Increase watering and provide shade."
        }
        recommendations = "Increase watering and provide shade."
    elif leaf_color == "brown" and watering_frequency == "low":
        diagnosis_result = {
            "name": "Drought Stress",
            "symptoms": "Brown leaves due to lack of water.",
            "risk_factors": "Infrequent watering.",
            "prevention": "Increase watering frequency.",
            "treatment": "Water plants deeply and regularly."
        }
        recommendations = "Water plants deeply and regularly."
    elif pest_presence and leaf_shape == "holey":
        diagnosis_result = {
            "name": "Pest Infestation",
            "symptoms": "Holes in leaves.",
            "risk_factors": "High pest population.",
            "prevention": "Regular pest monitoring.",
            "treatment": "Apply appropriate pesticide."
        }
        recommendations = "Regular pest monitoring. Apply appropriate pesticide."
    elif leaf_color == "purple" and fertilizer_use == "low":
        diagnosis_result = {
            "name": "Phosphorus Deficiency",
            "symptoms": "Purple leaves due to lack of phosphorus.",
            "risk_factors": "Insufficient fertilizer use.",
            "prevention": "Use balanced fertilizer.",
            "treatment": "Apply phosphorus-rich fertilizer."
        }
        recommendations = "Apply phosphorus-rich fertilizer."
    elif mold_growth and leaf_shape == "fuzzy":
        diagnosis_result = {
            "name": "Powdery Mildew",
            "symptoms": "Fuzzy white mold on leaves.",
            "risk_factors": "High humidity and poor air circulation.",
            "prevention": "Ensure proper air circulation.",
            "treatment": "Apply fungicide."
        }
        recommendations = "Ensure proper air circulation. Apply fungicide."
    elif stem_condition == "cracked" and soil_type == "sandy":
        diagnosis_result = {
            "name": "Stem Cracking",
            "symptoms": "Cracked stems.",
            "risk_factors": "Dry, sandy soil.",
            "prevention": "Improve soil moisture retention.",
            "treatment": "Mulch around the base to retain moisture."
        }
        recommendations = "Mulch around the base to retain moisture."
    elif leaf_color == "yellow" and leaf_shape == "droopy":
        diagnosis_result = {
            "name": "Nitrogen Deficiency",
            "symptoms": "Yellow, droopy leaves.",
            "risk_factors": "Insufficient nitrogen.",
            "prevention": "Use nitrogen-rich fertilizer.",
            "treatment": "Apply nitrogen-rich fertilizer."
        }
        recommendations = "Apply nitrogen-rich fertilizer."
    elif pest_presence and mold_growth:
        diagnosis_result = {
            "name": "Pest and Mold Infestation",
            "symptoms": "Presence of pests and mold.",
            "risk_factors": "High humidity and pest population.",
            "prevention": "Control humidity and pests.",
            "treatment": "Apply pesticide and fungicide."
        }
        recommendations = "Control humidity and pests. Apply pesticide and fungicide."
    elif wilting and fertilizer_use == "excessive":
        diagnosis_result = {
            "name": "Fertilizer Burn",
            "symptoms": "Wilting due to excessive fertilizer use.",
            "risk_factors": "Over-fertilization.",
            "prevention": "Follow recommended fertilizer dosage.",
            "treatment": "Flush soil with water."
        }
        recommendations = "Follow recommended fertilizer dosage. Flush soil with water."
    elif leaf_color == "yellow" and weather_conditions == "cold":
        diagnosis_result = {
            "name": "Cold Stress",
            "symptoms": "Yellow leaves during cold weather.",
            "risk_factors": "Low temperatures.",
            "prevention": "Protect plants from cold.",
            "treatment": "Move plants to warmer area."
        }
        recommendations = "Protect plants from cold. Move plants to warmer area."
    elif leaf_shape == "distorted" and pest_presence:
        diagnosis_result = {
            "name": "Aphid Damage",
            "symptoms": "Distorted leaves due to aphids.",
            "risk_factors": "Aphid infestation.",
            "prevention": "Monitor and control aphids.",
            "treatment": "Apply aphid-specific pesticide."
        }
        recommendations = "Monitor and control aphids. Apply aphid-specific pesticide."
    elif mold_growth and watering_frequency == "high":
        diagnosis_result = {
            "name": "Overwatering",
            "symptoms": "Mold growth due to excessive watering.",
            "risk_factors": "Frequent watering.",
            "prevention": "Reduce watering frequency.",
            "treatment": "Allow soil to dry out between waterings."
        }
        recommendations = "Reduce watering frequency. Allow soil to dry out between waterings."
    elif leaf_color == "brown" and pest_presence:
        diagnosis_result = {
            "name": "Spider Mite Infestation",
            "symptoms": "Brown leaves with fine webbing.",
            "risk_factors": "Spider mites.",
            "prevention": "Regular monitoring for mites.",
            "treatment": "Apply miticide."
        }
        recommendations = "Regular monitoring for mites. Apply miticide."
    elif stem_condition == "soft" and soil_type == "wet":
        diagnosis_result = {
            "name": "Stem Rot",
            "symptoms": "Soft, rotting stems.",
            "risk_factors": "Excessive soil moisture.",
            "prevention": "Improve soil drainage.",
            "treatment": "Reduce watering and improve drainage."
        }
        recommendations = "Reduce watering and improve drainage."
    elif leaf_shape == "spotted" and weather_conditions == "humid":
        diagnosis_result = {
            "name": "Bacterial Leaf Spot",
            "symptoms": "Spotted leaves in humid conditions.",
            "risk_factors": "High humidity.",
            "prevention": "Ensure proper air circulation.",
            "treatment": "Apply copper-based bactericide."
        }
        recommendations = "Ensure proper air circulation. Apply copper-based bactericide."

    return diagnosis_result, recommendations
