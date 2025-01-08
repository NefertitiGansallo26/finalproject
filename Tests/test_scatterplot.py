import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestScatterPlot(unittest.TestCase):

    def setUp(self):
        """Load and preprocess the dataset for each test."""
        file_path = r'C:\Users\Theresa Gansallo\OneDrive\Documents\UNI 2nd year\PROFESSIONAL SOFTWARE AND CAREER PRACTICES(Edward)\Final_Project\Data\literacy-rate-vs-gdp-per-capita.csv'
        self.data = pd.read_csv(file_path)
        self.data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        self.continent_mapping = {
            # Africa
            'South Africa': 'Africa', 'Nigeria': 'Africa', 'Egypt': 'Africa', 'Kenya': 'Africa',
            # Add other continents as needed
            'Australia': 'Oceania', 'New Zealand': 'Oceania'
        }
        self.data['Continent'] = self.data['Entity'].map(self.continent_mapping)
        self.data = self.data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])

    def test_dataset_loading(self):
        """Test if the dataset is loaded successfully."""
        self.assertFalse(self.data.empty, "Dataset failed to load or is empty.")

    def test_column_renaming(self):
        """Test if the critical columns are renamed correctly."""
        self.assertIn("Literacy_Rate", self.data.columns, "Column 'Literacy_Rate' is missing.")
        self.assertIn("GDP_Per_Capita", self.data.columns, "Column 'GDP_Per_Capita' is missing.")

    def test_continent_mapping(self):
        """Test if all rows have a valid continent after mapping."""
        unmapped = self.data[self.data['Continent'].isnull()]
        self.assertTrue(unmapped.empty, "Some rows are not mapped to a continent.")

    def test_valid_data_filtering(self):
        """Test if there are no NaN values in the filtered dataset."""
        self.assertFalse(self.data[['Literacy_Rate', 'GDP_Per_Capita', 'Continent']].isnull().any().any(),
                         "Filtered data contains NaN values.")

    def test_scatterplot_colors(self):
        """Test if scatter plot has the correct number of colors (one per continent)."""
        plt.figure()
        scatter = sns.scatterplot(
            data=self.data,
            x='Literacy_Rate',
            y='GDP_Per_Capita',
            hue='Continent',
            palette='Set2'
        )

        # Add the regression line
        sns.regplot(
            data=self.data,
            x='Literacy_Rate',
            y='GDP_Per_Capita',
            scatter=False,
            color='black',
            line_kws={"label": "Regression Line"}
        )

        # Create legend
        plt.legend(title='Continent', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Count only the continent-related legend items
        legend_labels = [t.get_text() for t in scatter.legend_.texts if t.get_text() != "Regression Line"]
        unique_continents = len(self.data['Continent'].unique())
        
        self.assertEqual(len(legend_labels), unique_continents, 
                         f"Legend should have {unique_continents} continent colors, but found {len(legend_labels)}.")

if __name__ == '__main__':
    unittest.main()
