import pandas as pd
import plotly.express as px

file_path = "data/iris.csv"
df = pd.read_csv(file_path)
# print(df.head(4))

plot = px.scatter(data_frame=df, x="sepal_length", y="petal_length", title="sepal_length versus petal_length", color="species", size="sepal_width", facet_col="species")
plot.show()