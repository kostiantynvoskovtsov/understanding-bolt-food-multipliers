import plotly.express as px
import pandas as pd
time_periods_1 = [
    {"time":"00:00-11:59", "multiplier":1.2},
    {"time":"12:00-13:59", "multiplier":1.4},
    {"time":"14:00-16:59", "multiplier":1.2},
    {"time":"17:00-20:59", "multiplier":1.4},
    {"time":"21:00-23:59", "multiplier":1.2},
]
time_periods_2 = [
    {"time":"00:00-11:59", "multiplier":1.2},
    {"time":"12:00-13:59", "multiplier":1.4},
    {"time":"14:00-16:59", "multiplier":1.2},
    {"time":"17:00-20:59", "multiplier":1.6},
    {"time":"21:00-23:59", "multiplier":1.4},
]

data1 = pd.DataFrame(time_periods_1)
data2 = pd.DataFrame(time_periods_2)
data1["day"] = "Monday"
data2["day"] = "Tuesday"
comb_data = pd.concat([data1, data2])
comb_data
