import plotly.express as px
import pandas as pd
time_periods = [
    {"time":"00:00-11:59", "multiplier":1.2},
    {"time":"12:00-13:59", "multiplier":1.4},
    {"time":"14:00-16:59", "multiplier":1.2},
    {"time":"17:00-20:59", "multiplier":1.6},
    {"time":"21:00-23:59", "multiplier":1.4},
]
data = pd.DataFrame(time_periods)
data
fig = px.bar(data, x = "time", y = "multiplier")
fig.show()
