import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = r'C:\Users\Theresa Gansallo\OneDrive\Documents\UNI 2nd year\PROFESSIONAL SOFTWARE AND CAREER PRACTICES(Edward)\Final_Project\Data\literacy-rate-vs-gdp-per-capita.csv'
data = pd.read_csv(file_path)

# Rename columns for simplicity
data = data.rename(columns={
    "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
    "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
})

# Expanded mapping of countries to continents
continent_mapping = {
    # Africa
    'South Africa': 'Africa', 'Nigeria': 'Africa', 'Egypt': 'Africa', 'Kenya': 'Africa',
    'Algeria': 'Africa', 'Ghana': 'Africa', 'Morocco': 'Africa', 'Ethiopia': 'Africa',
    'Tanzania': 'Africa', 'Uganda': 'Africa', 'Senegal': 'Africa', 'Zambia': 'Africa',

    # Asia
    'China': 'Asia', 'India': 'Asia', 'Japan': 'Asia', 'Saudi Arabia': 'Asia',
    'Indonesia': 'Asia', 'South Korea': 'Asia', 'Malaysia': 'Asia', 'Vietnam': 'Asia',
    'Pakistan': 'Asia', 'Bangladesh': 'Asia', 'Iran': 'Asia', 'Philippines': 'Asia',

    # Europe
    'Germany': 'Europe', 'United Kingdom': 'Europe', 'France': 'Europe', 'Italy': 'Europe',
    'Spain': 'Europe', 'Poland': 'Europe', 'Sweden': 'Europe', 'Netherlands': 'Europe',
    'Norway': 'Europe', 'Ukraine': 'Europe', 'Greece': 'Europe', 'Belgium': 'Europe',

    # North America
    'United States': 'North America', 'Canada': 'North America', 'Mexico': 'North America',
    'Cuba': 'North America', 'Honduras': 'North America', 'Guatemala': 'North America',
    'Panama': 'North America', 'Jamaica': 'North America',

    # South America
    'Brazil': 'South America', 'Argentina': 'South America', 'Chile': 'South America',
    'Colombia': 'South America', 'Peru': 'South America', 'Ecuador': 'South America',
    'Paraguay': 'South America', 'Uruguay': 'South America',

    # Oceania
    'Australia': 'Oceania', 'New Zealand': 'Oceania', 'Papua New Guinea': 'Oceania',
    'Fiji': 'Oceania', 'Samoa': 'Oceania', 'Tonga': 'Oceania', 'Kiribati': 'Oceania'
}

# Map countries to continents
data['Continent'] = data['Entity'].map(continent_mapping)

# Filter for valid data and mapped countries
data = data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])

# Calculate Correlation Coefficient
correlation = data['Literacy_Rate'].corr(data['GDP_Per_Capita'])
print(f"Correlation Coefficient between Literacy Rate and GDP per Capita: {correlation:.3f}")

# Scatter Plot with More Countries
plt.figure(figsize=(12, 8))

# Scatterplot with smaller points
scatter = sns.scatterplot(
    data=data,
    x='Literacy_Rate',
    y='GDP_Per_Capita',
    hue='Continent',
    palette='Set2',
    s=30  # Adjusted point size
)

# Regression Line
sns.regplot(
    data=data,
    x='Literacy_Rate',
    y='GDP_Per_Capita',
    scatter=False,
    color='black',
    line_kws={"label": "Regression Line"}
)

# Legend
handles, labels = scatter.get_legend_handles_labels()
handles.append(plt.Line2D([0], [0], color='black', lw=2, label='Regression Line'))
plt.legend(handles=handles, title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')

# Final Plot Customizations
plt.title('Literacy Rate vs GDP per Capita by Continent (Expanded Countries)', fontsize=16)
plt.xlabel('Literacy Rate (%)', fontsize=14)
plt.ylabel('GDP per Capita (USD)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # show plot
