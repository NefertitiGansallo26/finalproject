import unittest
import pandas as pd

class TestPlotPipeline(unittest.TestCase):

#loading the dataset for testing
    def setUp(self):
        self.file_path = 'Data/literacy-rate-vs-gdp-per-capita.csv'
        self.data = pd.read_csv(self.file_path)  
        self.mapping = {
            "South Africa": "Africa",
            "India": "Asia",
            "Germany": "Europe"
        }


#testing if the dataset loads properly
    def test_load_dataset(self): 
        self.assertFalse(self.data.empty, "Dataset failed to load or is empty.")
        self.assertIn("Entity", self.data.columns, "Column 'Entity' is missing.")
        self.assertIn("Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99", self.data.columns,
                      "Column 'Adult literacy rate...' is missing.")

# testing if the columns have been renamed correctly 
    def test_rename_columns(self):
        renamed_data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        }).copy()
        self.assertIn("Literacy_Rate", renamed_data.columns)
        self.assertIn("GDP_Per_Capita", renamed_data.columns)
        self.assertNotIn("Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99", renamed_data.columns)

 # testing if countries have been mapped to continents
    def test_map_to_continents(self):
        renamed_data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        }).copy()
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        self.assertIn("Continent", renamed_data.columns)
        self.assertEqual(renamed_data.loc[renamed_data['Entity'] == "South Africa", "Continent"].iloc[0], "Africa")
        self.assertTrue(pd.isnull(renamed_data.loc[renamed_data['Entity'] == "Unknown Country", "Continent"]).all())

#Testing if data has been filtered correctly 
    def test_filter_valid_data(self):
        renamed_data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        }).copy()
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        filtered_data = renamed_data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])
        self.assertGreater(len(filtered_data), 0, "Filtered data is empty.")
        self.assertTrue((~filtered_data['Entity'].isin(["Unknown Country"])).all())

#Testing if averages are calculated for each continent 
    def test_calculate_averages(self):
        renamed_data = self.data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        }).copy()
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        filtered_data = renamed_data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])
        averages = filtered_data.groupby('Continent')[['GDP_Per_Capita', 'Literacy_Rate']].mean()
        self.assertTrue("Africa" in averages.index, "Africa is not in the grouped averages.")
        if "Africa" in averages.index:
            self.assertGreater(averages.loc["Africa", "Literacy_Rate"], 0, "Average Literacy Rate for Africa should be > 0.")

if __name__ == "__main__":
    unittest.main()
