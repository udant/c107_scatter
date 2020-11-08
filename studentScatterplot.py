import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
#fig = px.scatter(df,x="date",y="cases",title="Covid Cases",color="country")
fig = px.scatter(df,x="attempt",y="student_id",title="scatter",color="student_id")
fig.show()
