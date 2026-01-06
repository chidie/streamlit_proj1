import pandas as pd
from plotly import express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


file_path = "data/iris.csv"
df = pd.read_csv(file_path)

# Add box traces (sepal_width) on secondary y-axis
box_fig = px.box(df, x='species', y='sepal_width', color='species')
box_fig.show()

violin_fig = px.violin(df, x='species', y='sepal_width', color='species', box=True)
violin_fig.show()