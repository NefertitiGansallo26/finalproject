#### Author: Nefertiti Gansallo - 230324248    DAT5902: Professional Software and Career Practices Final Project

## Overview:
This project analyses whether there is a correlation between literacy rates and GDP per capita, using the data from **Our world in Data**. The analysis focuses on identifying trends and patterns across each country and their respective continent, with visualisations that highlight the relationship between literacy rates and GDP per capita. 

### Hypothesis: Countries with higher literacy rates have a higher GDP per capita.

This project investigates the relationship between literacy rates and GDP per capita across different continents, using a dataset that contains global literacy rates and GDP per capita statistics. The project was developed using Python and its respective data science libraries such as Pandas, Seaborn and Matplotlib. Unit tests were created using unittest and are verified through a CircleCI continous integration pipeline.

### Project Structure:
- config.yml: CircleCI configuration file for setting up the data to be tested and executing the Python script.
- Data/: Folder containting the dataset in csv file formatting.
- Graphs/: Folder containing python code for creating graphs.
- Images/: Folder containing images of generated graphs.
- Tests/: Folder containing unit test files for each graph.
- Key_Tests.txt: File contains a description of the key tests that the code must pass. 
- requirements.txt: File that contains all the necessary dependencies for the project that are installed correctly.

### Dependencies:
The project requires the following Python packages/libraries:
- Pandas
- Matplotlib
- Seaborn 
- Unittest
- Pytest

## Files and Folders:
.circeci folder contains config file used to connect to circeci pipeline.

Data folder contains csv documentation of data used to create graphs and perfom an analysis. The name of the csv file in this folder is : 
- literacy-rate-vs-gdp-per-capita.csv

Graphs folder contains all of the code used to create the two graphs which are used for analysis.The file names of the graphs are:
- Bar_Plot.py
- Scatter_Plot.py

Images folder contains two images of the two graphs. The file names for the images are:
- Image_1.png
- Image_2.png

Tests folder contains unit tests for the codes for the graphs. The file names for the unit tests are:
- test_barplot.py
- test_scatterplot.py

## Data sources:
Our World in Data: https://ourworldindata.org/grapher/literacy-rate-vs-gdp-per-capita

