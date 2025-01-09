import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestScatterPlot(unittest.TestCase):

#loading the dataset for testing
    def setUp(self):
        file_path ='Data/literacy-rate-vs-gdp-per-capita.csv'

        self.data = pd.read_csv(file_path)
        self.data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        self.continent_mapping = {
            'South Africa': 'Africa', 'Nigeria': 'Africa', 'Egypt': 'Africa', 'Kenya': 'Africa',
            'Australia': 'Oceania', 'New Zealand': 'Oceania'
        }
        self.data['Continent'] = self.data['Entity'].map(self.continent_mapping)
        self.data = self.data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])

#Testing if the dataset loads properly
    def test_dataset_loading(self):
        self.assertFalse(self.data.empty, "Dataset failed to load or is empty.")


#Testing if the columns have been renamed correctly 
    def test_column_renaming(self):
        self.assertIn("Literacy_Rate", self.data.columns, "Column 'Literacy_Rate' is missing.")
        self.assertIn("GDP_Per_Capita", self.data.columns, "Column 'GDP_Per_Capita' is missing.")

#Testing if countries have been mapped to their continent
    def test_continent_mapping(self):
        unmapped = self.data[self.data['Continent'].isnull()]
        self.assertTrue(unmapped.empty, "Some rows are not mapped to a continent.")

#Testing if the data has been filtered correctly
    def test_valid_data_filtering(self):
        self.assertFalse(self.data[['Literacy_Rate', 'GDP_Per_Capita', 'Continent']].isnull().any().any(),
                         "Filtered data contains NaN values.")
        

#Testing if scatter plot has the correct number of colours to match each continent 
    def test_scatterplot_colors(self):
        plt.figure()
        scatter = sns.scatterplot(
            data=self.data,
            x='Literacy_Rate',
            y='GDP_Per_Capita',
            hue='Continent',
            palette='Set2'
        )

        # Adding regression line
        sns.regplot(
            data=self.data,
            x='Literacy_Rate',
            y='GDP_Per_Capita',
            scatter=False,
            color='black',
            line_kws={"label": "Regression Line"}
        )

        # Creating legend
        plt.legend(title='Continent', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Counting only the continents in the legend
        legend_labels = [t.get_text() for t in scatter.legend_.texts if t.get_text() != "Regression Line"]
        unique_continents = len(self.data['Continent'].unique())
        
        self.assertEqual(len(legend_labels), unique_continents, 
                         f"Legend should have {unique_continents} continent colors, but found {len(legend_labels)}.")

if __name__ == '__main__':
    unittest.main()
