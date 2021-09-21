import plotly.figure_factory as ff
import pandas as pd
import statistics as st
import random as rd
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df['average'].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for number in range(0,counter):
        random_index=rd.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean

def showFig(mean_list):
    df=mean_list
    mean=st.mean(df)
    
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,15],mode='lines',name='MEAN'))
    fig.show()


def setup():
    mean_list=[]
    for number in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    showFig(mean_list)
    mean = st.mean(mean_list)
    print("Mean of sampling distribution :-",mean )
    

setup() 

population_of_mean=st.mean(data)
print('Population of mean->',population_of_mean)

def stddeviaiton():
    mean_list=[]
    for number in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    stddev=st.stdev(mean_list)
    print('STD DEVIATION->',stddev)

