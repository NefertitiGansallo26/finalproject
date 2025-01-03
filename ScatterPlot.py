import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = r'C:\Users\Theresa Gansallo\OneDrive\Documents\UNI 2nd year\PROFESSIONAL SOFTWARE AND CAREER PRACTICES(Edward)\finalproject\literacy-rate-vs-gdp-per-capita.csv'
latest_data = pd.read_csv(file_path)

# Rename columns for simplicity
latest_data = latest_data.rename(columns={
    "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
    "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
})

# Print the renamed column names to confirm
print("Renamed Columns:", latest_data.columns)

# Scatter Plot: Literacy Rate vs GDP per Capita
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=latest_data, 
    x='Literacy_Rate', 
    y='GDP_Per_Capita', 
    hue='Entity',  # Optional: Differentiate countries with colors
    palette='viridis',
    legend=False
)
plt.title('Relationship Between Literacy Rate and GDP per Capita', fontsize=14)
plt.xlabel('Literacy Rate (%)', fontsize=12)
plt.ylabel('GDP per Capita (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
