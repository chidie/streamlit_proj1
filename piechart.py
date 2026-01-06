import pandas as pd
import plotly.express as px

file_path = "data/tips.csv"
df = pd.read_csv(file_path)
print(df.columns)
print(df.nunique())

plot = px.pie(data_frame=df, 
              values='total_bill', 
              names='day', 
              facet_col='size',
              hole=0.3,
              title='Pie Charts showing total tips across gender')
plot.show()