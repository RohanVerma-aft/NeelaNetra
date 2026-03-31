# Hackathon MVP: river chemistry + pollution analysis

def analyze_river(latest_data):
    """
    latest_data: dict with keys "algae", "industrial", "oil"
    returns dict with:
      - pollution_index
      - dominant_pollutant
      - pollution_level_text
      - disease_risks
      - advice
    """

    # Simple pollution index (sum weighted)
    pollution_index = latest_data["algae"]*0.5 + latest_data["industrial"]*0.3 + latest_data["oil"]*0.2
    pollution_index = min(100, int(pollution_index))

    # Determine dominant pollutant
    dominant_pollutant = max(latest_data, key=lambda k: latest_data[k])

    # Pollution level text
    if pollution_index < 30:
        level = "Low"
    elif pollution_index < 60:
        level = "Moderate"
    else:
        level = "High"

    # Disease risk based on pollutants
    if dominant_pollutant == "algae":
        diseases = ["Skin infections", "Algae-related toxins"]
        advice = "Avoid bathing in hotspots, do not consume raw water"
    elif dominant_pollutant == "industrial":
        diseases = ["Respiratory problems", "Typhoid"]
        advice = "Avoid direct contact and drinking untreated water"
    elif dominant_pollutant == "oil":
        diseases = ["Skin irritation", "Eye irritation"]
        advice = "Avoid contact, report spills to authorities"
    else:
        diseases = []
        advice = "Water is safe"

    return {
        "pollution_index": pollution_index,
        "dominant_pollutant": dominant_pollutant.title(),
        "pollution_level_text": level,
        "disease_risks": diseases,
        "advice": advice
    }