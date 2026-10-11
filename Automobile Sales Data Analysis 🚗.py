

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("automobile_sales.csv")

print(df.head())
print(df.info())
#print(df.describe(numeric_only=True))

df["Total_Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("Total Units Sold:", np.sum(df["Units_Sold"]))
print("Total Revenue:", np.sum(df["Total_Revenue"]))

print("\nSales by Brand:")
print(df.groupby("Brand")["Units_Sold"].sum())

print("\nRevenue by City:")
print(df.groupby("City")["Total_Revenue"].sum())

sns.barplot(data=df, x="Brand", y="Units_Sold", estimator=sum)
plt.title("Sales by Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="Fuel_Type", y="Units_Sold", estimator=sum)
plt.title("Sales by Fuel Type")
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="Total_Revenue", estimator=sum)
plt.title("Revenue by City")
plt.tight_layout()
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Total_Revenue"].sum()

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Automobile Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.histplot(data=df, x="Unit_Price", bins=10, kde=True)
plt.title("Vehicle Price Distribution")
plt.tight_layout()
plt.show()
