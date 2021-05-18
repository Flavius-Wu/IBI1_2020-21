import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections
from scipy.optimize import curve_fit
import math

covid_data = pd.read_csv("full_data.csv")  # The code for importing the .csv file works
#print(covid_data.head(5))
#print(covid_data.info())
print(covid_data.iloc[0:12:2, 0:5])  # showing all columns, and every second row between (and including) 0 and 10
#print(covid_data.describe())
my_columns = [False, False, False, False, False, True]  # used a Boolean
print(covid_data.loc[(covid_data[
                          'location'] == 'Afghanistan'), my_columns])  # to show \total cases" for all rows corresponding to Afghanistan
print(covid_data.loc[(covid_data[
                          'location'] == 'World'), "new_cases"].mean())  # computed the mean of new cases for the entire world.
print(covid_data.loc[(covid_data[
                          'location'] == 'World'), "new_cases"].median())  # computed the median of new cases for the entire world.
new_case = (covid_data.loc[(covid_data['location'] == 'World'), "new_cases"])
new_death = (covid_data.loc[(covid_data['location'] == 'World'), "new_deaths"])
total = (covid_data.loc[(covid_data['location'] == 'World'), "total_cases"])
plt.boxplot(new_case)
plt.ylabel("infected_number")
plt.xlabel("Worldwide")
plt.title("a boxplot of new cases worldwide")
plt.show()  # created a boxplot of new cases worldwide.
world_dates = (covid_data.loc[(covid_data['location'] == 'World'), "date"])
plt.plot(world_dates, new_case, 'o-', color="blue",label="new_case")
plt.plot(world_dates, new_death, 'o-', color="red",label="new_death")
plt.ylabel("infected_number")
plt.xlabel("Date")
plt.title("a plot of new case&death worldwide")
plt.legend(loc=0)
plt.xticks(range(0, 92, 7))
plt.xticks(rotation=40)
plt.show()  # plot both new cases and new deaths worldwide

#the method was inspired and adopted from CSDN, all credits to the original author\
#the code has been modified and channged to fit in this program
def logistic_increase_function(t, K, P0, r):
    r = 0.29
    t0 = 1
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)
# define logistic increase function

t = list(range(1,92+1))   #read the whole list
t = np.array(t)          #list date
P = np.array(total)       #list number

popt, pocv = curve_fit(logistic_increase_function, t, P,bounds=(0, 820000))
#fit the dots by a curve
P_predict=logistic_increase_function(t,popt[0],popt[1],popt[2])
future=[93,95,97,100,107,113,115,125] #define future days
future=np.array(future)  #list future days
future_predict=logistic_increase_function(future,popt[0],popt[1],popt[2]) #the future infected number under logistic
plot1=plt.plot(t,P,'s',label="COVID confirm cases")  #plot COVID confirm cases
plot2=plt.plot(t, P_predict,'r',label='infected number curve') #plot infected number curve
plot3=plt.plot(future,future_predict,'s',label='prediction of infect') # plot prediction of infect
plt.xlabel('date')
plt.ylabel('conform cases')
plt.legend(loc=0)
plt.show()


