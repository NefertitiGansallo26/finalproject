import unittest
import pandas as pd

class TestPlotPipeline(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.csv"
        self.sample_data = pd.DataFrame({
            "Entity": ["South Africa", "India", "Germany", "Unknown Country"],
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": [87, 74, 99, None],
            "GDP per capita, PPP (constant 2017 international $)": [6450, 2010, 45000, None]
        })
        self.sample_data.to_csv(self.file_path, index=False)
        self.mapping = {
            "South Africa": "Africa",
            "India": "Asia",
            "Germany": "Europe"
        }

    def test_load_dataset(self):
        """Test loading the dataset."""
        data = pd.read_csv(self.file_path)
        self.assertEqual(len(data), 4)  # Should load all rows
        self.assertListEqual(list(data.columns), list(self.sample_data.columns))  # Check columns

    def test_rename_columns(self):
        """Test renaming columns."""
        data = pd.read_csv(self.file_path)
        renamed_data = data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        self.assertIn("Literacy_Rate", renamed_data.columns)
        self.assertIn("GDP_Per_Capita", renamed_data.columns)
        self.assertNotIn("Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99", renamed_data.columns)

    def test_map_to_continents(self):
        """Test mapping countries to continents."""
        data = pd.read_csv(self.file_path)
        renamed_data = data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        self.assertIn("Continent", renamed_data.columns)
        self.assertEqual(renamed_data.loc[0, "Continent"], "Africa")  # South Africa mapped to Africa
        self.assertTrue(pd.isnull(renamed_data.loc[3, "Continent"]))  # Unknown country not mapped

    def test_filter_valid_data(self):
        """Test filtering valid data."""
        data = pd.read_csv(self.file_path)
        renamed_data = data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        filtered_data = renamed_data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])
        self.assertEqual(len(filtered_data), 3)  # Only valid rows remain
        self.assertNotIn("Unknown Country", filtered_data['Entity'].values)

    def test_calculate_averages(self):
        """Test calculating averages by continent."""
        data = pd.read_csv(self.file_path)
        renamed_data = data.rename(columns={
            "Adult literacy rate, population 15+ years, both sexes (%), LR.AG15T99": "Literacy_Rate",
            "GDP per capita, PPP (constant 2017 international $)": "GDP_Per_Capita"
        })
        renamed_data['Continent'] = renamed_data['Entity'].map(self.mapping)
        filtered_data = renamed_data.dropna(subset=['Literacy_Rate', 'GDP_Per_Capita', 'Continent'])
        averages = filtered_data.groupby('Continent')[['GDP_Per_Capita', 'Literacy_Rate']].mean()
        self.assertIn("Africa", averages.index)
        self.assertAlmostEqual(averages.loc["Africa", "Literacy_Rate"], 87)  # Average for Africa

# Run tests in main
if __name__ == "__main__":
    unittest.main()
