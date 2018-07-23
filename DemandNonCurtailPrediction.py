import csv
from datetime import datetime
import matplotlib.pyplot as plt 
import matplotlib
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np

def mean_absolute_percentage_error(y_true, y_pred): 
   
    for i in range(0,len(y_true)):
        if y_true[i]==0:
    		y_true[i]=1000


    y_true, y_pred = np.array(y_true), np.array(y_pred)
    
    
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100





with open('No Curtailment Systems/SQ3-1.1.1.1-7-20160819 modified.csv', 'rU') as f:
  reader = csv.reader(f)
  your_list = list(reader)

Demandprod=[]
date=[]
Demandpred=[]
for i in range(1,len(your_list)):
	
	Demandpred.append(float(your_list[i][4]))#.replace(';','.')))
	Demandprod.append(float(your_list[i][7]))#.replace(';','.')))
	date.append(datetime.strptime(your_list[i][0],'%d/%m/%y %H:%M'))



Demandprod2=[]
date2=[]
Demandpred2=[]
for i in range(1,48000):	
	Demandpred2.append(Demandpred[i])
	Demandprod2.append(Demandprod[i])
	date2.append(date[i])
plt.figure(2)
plt.plot(date2,Demandprod2)
plt.plot(date2,Demandpred2)
plt.title("Demand Prediction vs Production")
plt.xlabel("Time of Day")
plt.ylabel("Kilo-Watts (Power)")
plt.show()

Demandpred2Tot=str(sum(Demandpred2))
Demandprod2Tot=str(sum(Demandprod2))
rms2 = sqrt(mean_squared_error(Demandprod2, Demandpred2))
mape2 = mean_absolute_percentage_error(Demandprod2, Demandpred2)

print "Demand prediction 2:" + str(' ') + Demandpred2Tot
print "Demand produced 2:" + str(' ') + Demandprod2Tot
print "Percentage Difference 2:" + str(' ') + str(((float(Demandprod2Tot)-float(Demandpred2Tot))/float(Demandprod2Tot))*100)
print "RMS for Day 2: " +str(' ') + str(rms2)
print "MAPE day 2: " +str(' ') + str(mape2)

#Baseline results
#Demand prediction 2: 43787.303074
# Demand produced 2: 47568.674417
# Percentage Difference 2: 7.94928887413
# RMS for Day 2:  1.04942088578
# MAPE day 2:  1217.03177734


