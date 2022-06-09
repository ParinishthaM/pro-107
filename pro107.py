import csv
import pandas as pd
import plotly.express as px

fr = pd.read("data3.csv")
mean = fr.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()