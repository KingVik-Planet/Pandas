import matplotlib.pyplot as plt
import numpy as np

# Variables - 5 Classes of Land use and Land Cover
LandUse = ("Forest", "Shrubs", "Urban", "Water", "Grassland")

# Class (2000, 2010, and 2020) with Count
# Sum of counts for each year is 54321
LandUseData = {
    "2000": np.array([20000, 15000, 8000, 6321, 5000]),
    "2010": np.array([18000, 16000, 10000, 6321, 4000]),
    "2020": np.array([15000, 17000, 12000, 5321, 5000])
}

width = 0.7

fig, ax = plt.subplots()
bottom = np.zeros(5)

for year, data in LandUseData.items():
    Plot = ax.bar(LandUse, data, width, label=year, bottom=bottom)
    ax.bar_label(Plot, label_type="center")
    bottom += data

plt.legend()
ax.set_ylabel("Area (hectares)")
ax.set_xlabel("Land Use / Land Cover Class")
ax.set_title("Land Use and Land Cover Change (2000, 2010 and 2020)")
plt.show()