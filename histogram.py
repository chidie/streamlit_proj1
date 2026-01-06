import pandas as pd
import plotly.express as px

file_path = "data/iris.csv"
df = pd.read_csv(file_path)

plot = px.histogram(data_frame=df,
                    color="species",
                    x="sepal_length",
                    barmode="group",
                    title="Distribution of sepal_length")

plot.show()