import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import random
import csv
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df['level'].tolist()
mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)

print(median)
print(mode)
print(mean)

fig = px.scatter(df, x = "student_id", y = "level", color = "attempt")


fig.show()
