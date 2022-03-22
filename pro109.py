import csv
from collections import Counter
import pandas as pd
import math
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random 



df=pd.read_csv("StudentsPerformance.csv")
data=df["math score"].to_list()


mean= statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)

stdev=statistics.stdev(data)

firststdevStart=mean-stdev
firststdevEnd=mean+stdev

secondstdevStart=mean-2*stdev
secondstdevEnd=mean+2*stdev 

threestdevStart=mean-3*stdev
threestdevEnd=mean+3*stdev 


list_of_data_within_1_std_deviation = [result for result in data if result > firststdevStart and result < firststdevEnd]

list_of_data_within_2_std_deviation = [result for result in data if result > secondstdevStart and result < secondstdevEnd]

list_of_data_within_3_std_deviation = [result for result in data if result > threestdevStart and result < threestdevEnd]


perOfFirstList=len(list_of_data_within_1_std_deviation)*100.0 / len(data)

perOfSecondList=len(list_of_data_within_2_std_deviation)*100.0 / len(data)

perOfThreeList=len(list_of_data_within_3_std_deviation)*100.0 / len(data)


fig=ff.create_distplot([data],['math score'],show_hist=False)

fig.add_trace(go.Scatter(x=[firststdevStart,firststdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x=[firststdevEnd,firststdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))


fig.add_trace(go.Scatter(x=[secondstdevStart,secondstdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x=[secondstdevEnd,secondstdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.show()



print(perOfFirstList,perOfSecondList,perOfThreeList)