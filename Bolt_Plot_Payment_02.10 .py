import plotly.express as px
import pandas as pd

# First we define the time periods and multipliers
time_periods = [
    {"time": "00:00", "multiplier": 1.2},
    {"time": "11:59", "multiplier": 1.2},
    {"time": "12:00", "multiplier": 1.4},
    {"time": "13:59", "multiplier": 1.4},
    {"time": "14:00", "multiplier": 1.2},
    {"time": "16:59", "multiplier": 1.2},
    {"time": "17:00", "multiplier": 1.4},
    {"time": "20:59", "multiplier": 1.4},
    {"time": "21:00", "multiplier": 1.2},
    {"time": "23:59",  "multiplier": 1.2},
]

# Next, we create a DataFrame for the data
data = pd.DataFrame(time_periods)
data
# Finally, it's time to plot results
fig = px.bar(data, x="time", y="multiplier", width=800, height=400)
fig.update_layout(bargroupgap=0.05)

fig.show()
