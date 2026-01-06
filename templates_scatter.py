import pandas as pd
import plotly.express as px

df = pd.read_csv("data/iris.csv")

plotly_themes = ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation',
                 'xgridoff', 'ygridoff', 'gridon', 'none']

plot = px.scatter(data_frame=df,
                  x = 'petal_length', 
                  size='sepal_width', 
                  template='plotly_dark',
                  y='petal_width',
                  color='species',
                  title='Scatter plot with template')

plot.show()