# test_rivers.py
import requests

def test_river_api(river_name):
    url = f"http://127.0.0.1:8000/api/river/{river_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"River: {data['river']}")
        print(f"Pollution Index: {data['current_pollution_index']}")
        print(f"Dominant Pollutant: {data['dominant_pollutant']}")
        print(f"Disease Risks: {', '.join(data['disease_risks'])}")
        print(f"Latest Chemistry: {data['latest_chemistry']}")
        print(f"Trend Graph Base64 (first 50 chars): {data['trend_graph_base64'][:50]}...")
    else:
        print("River not found!")

if __name__ == "__main__":
    test_river_api("yamuna")