import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Step 1: Load CSV data
data = pd.read_csv("data/sales_data.csv")

# Step 2: Display basic information
print("Dataset Info:")
print(data.info())

# Step 3: Calculate average values
avg_sales = data["Sales"].mean()
avg_profit = data["Profit"].mean()
avg_expenses = data["Expenses"].mean()

print("\nAverage Values:")
print(f"Average Sales: {avg_sales}")
print(f"Average Profit: {avg_profit}")
print(f"Average Expenses: {avg_expenses}")

# Step 4: Bar Chart - Monthly Sales
plt.figure()
plt.bar(data["Month"], data["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("output/bar_chart.png")
plt.close()

# Step 5: Scatter Plot - Sales vs Profit
plt.figure()
plt.scatter(data["Sales"], data["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("output/scatter_plot.png")
plt.close()

# Step 6: Heatmap - Correlation
plt.figure()
sns.heatmap(data[["Sales", "Profit", "Expenses"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("output/heatmap.png")
plt.close()

print("\nVisualizations saved in the output folder.")
