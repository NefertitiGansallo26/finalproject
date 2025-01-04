import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = 'path_to_cleaned_data.csv'  # Replace with the correct path
latest_data = pd.read_csv(file_path)

# Correlation Heatmap
plt.figure(figsize=(6, 4))
correlation_matrix = latest_data[['Literacy_Rate', 'GDP_Per_Capita']].corr()
sns.heatmap(
    correlation_matrix, 
    annot=True, 
    cmap='coolwarm', 
    fmt='.2f', 
    cbar=True
    )
plt.title('Correlation Heatmap', fontsize=14)
plt.show()