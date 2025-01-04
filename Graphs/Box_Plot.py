import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = 'path_to_cleaned_data.csv'  # Replace with the correct path
latest_data = pd.read_csv(file_path)

 # Define literacy rate ranges

bins = [0, 50, 75, 100]
labels = ['Low (<50%)', 'Medium (50-75%)', 'High (>75%)']
latest_data['Literacy_Rate_Range'] = pd.cut(latest_data['Literacy_Rate'], bins=bins, labels=labels)
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=latest_data, 
    x='Literacy_Rate_Range', 
    y='GDP_Per_Capita', 
    palette='Set2'
    )
plt.title('GDP per Capita by Literacy Rate Range', fontsize=14)
plt.xlabel('Literacy Rate Range', fontsize=12)
plt.ylabel('GDP per Capita (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
