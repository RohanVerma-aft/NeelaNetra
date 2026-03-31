import matplotlib
matplotlib.use("Agg")  # non-GUI backend
import matplotlib.pyplot as plt
from pathlib import Path
import json

# Load river JSON
DATA_FILE = Path(__file__).parent / "app" / "data" / "river_data.json"

with open(DATA_FILE) as f:
    all_data = json.load(f)

river_data = all_data["yamuna"]

# Prepare data
years = [d["year"] for d in river_data]
BOD = [d["BOD"] for d in river_data]
DO = [d["DO"] for d in river_data]
Nitrate = [d["Nitrate"] for d in river_data]

# Plot
plt.figure(figsize=(10,5))
plt.plot(years, BOD, marker='o', label="BOD")
plt.plot(years, DO, marker='o', label="DO")
plt.plot(years, Nitrate, marker='o', label="Nitrate")
plt.title("Yamuna River Chemistry Trend")
plt.xlabel("Year")
plt.ylabel("Level")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save PNG
plt.savefig("yamuna_trend.png")
plt.close()
print("✅ Trend graph saved as yamuna_trend.png")