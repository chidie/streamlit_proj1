import pandas as pd
import plotly.express as px

file_path = "data\\us-cities-top-1k.csv"
df = pd.read_csv(file_path)

plot = px.scatter_mapbox(data_frame=df,
                         lat='lat',
                         lon='lon',
                         hover_name="City",
                         size='Population',
                         zoom= 4.5,
                         title='Population across different cities',
                         mapbox_style='open-street-map')

plot.show()