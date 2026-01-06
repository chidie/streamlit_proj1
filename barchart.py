import pandas as pd
from plotly import express as px

file_path = "data/iris.csv"
df = pd.read_csv(file_path)
print(df.head())

# What species do we have?
unique_species = df['species'].unique()
print("Species: ", unique_species)

# Find the average petal length and plot it in a bar chart.
df1 = df.groupby(['species']).mean().reset_index()
plot = px.bar(df1, x='species', y='petal_length', title='Bar chart showing average petal length across species', color="species")
plot.show()