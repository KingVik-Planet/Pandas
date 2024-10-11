import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Class = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
value = [3.083, 28.321, 16.077, 16.762, 35.757]
bar_labels = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
bar_colors = ["tab:cyan", "tab:blue","tab:orange","tab:green", "tab:red"]
ax.bar(Class, value, label = bar_labels , color = bar_colors)
ax.set_ylabel("Year 1993")
ax.set_xlabel("Land Cover Land Use Class")
ax.legend(title = "LCLU", loc = 2)
ax.set_title("Land Cover Land Use Changes Year 1993")

plt.show()