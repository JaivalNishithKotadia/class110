from numpy import False_
import plotly.figure_factory as ff
import pandas as pd
import statistics as st
import random as rd

df=pd.read_csv("data.csv")
data=df['average'].tolist()
dataset=[]

for number in range(0,100):
    randomIndex=rd.randint(0,len(data))
    value=data[randomIndex]
    dataset.append(value)

mean=st.mean(dataset)
stdDev=st.stdev(dataset)

print("Mean is->",mean)
print('STD DEVIATION IS ->', stdDev)

fig=ff.create_distplot([dataset],["Average"],show_hist=False)
fig.show()

