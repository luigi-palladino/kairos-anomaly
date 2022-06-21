import pandas as pd
df = pd.read_csv("csv/normal_plan/fufi-robotnik_base_control-odom.csv")
df1 = pd.read_csv("csv/normal_plan_1/fufi-robotnik_base_control-odom.csv")
df2 = pd.read_csv("csv/window_plan/fufi-robotnik_base_control-odom.csv")
df3 = pd.read_csv("csv/window_plan_1/fufi-robotnik_base_control-odom.csv")
df.info()
df.columns

import matplotlib.pyplot as plt

# plt.plot(df1['pose.pose.position.x'],df1['pose.pose.position.y'],'k')
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import mpld3

import plotly.express as px

df =df1

fig = px.line(df, x="pose.pose.position.x", y="pose.pose.position.y", color="Time", title="layout.hovermode='closest' (the default)")
fig.update_traces(mode="markers+lines")

fig.show()