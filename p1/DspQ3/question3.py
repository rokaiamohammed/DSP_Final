import plotly.express as px
import pandas as pd
data_file = 'total-covid-cases-region.csv'

df = pd.read_csv(data_file)


fig = px.bar(df, x="Entity", y="Total confirmed cases of COVID-19 (cases)", color="Entity",
  animation_frame="Date", animation_group="Entity", range_y=[0,2000000])
fig.show()