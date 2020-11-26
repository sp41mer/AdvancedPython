import csv
import numpy as np
import matplotlib.pyplot as plt
"""
Data Set Information:

The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level,within an Italian city. Data were recorded from March 2004 to February 2005 (one year)representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. Ground Truth hourly averaged concentrations for CO, Non Metanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx) and Nitrogen Dioxide (NO2) and were provided by a co-located reference certified analyzer. Evidences of cross-sensitivities as well as both concept and sensor drifts are present as described in De Vito et al., Sens. And Act. B, Vol. 129,2,2008 (citation required) eventually affecting sensors concentration estimation capabilities. Missing values are tagged with -200 value.
This dataset can be used exclusively for research purposes. Commercial purposes are fully excluded.


Attribute Information:

0 Date (DD/MM/YYYY)
1 Time (HH.MM.SS)
2 True hourly averaged concentration CO in mg/m^3 (reference analyzer)
3 PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)
4 True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer)
5 True hourly averaged Benzene concentration in microg/m^3 (reference analyzer)
6 PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)
7 True hourly averaged NOx concentration in ppb (reference analyzer)
8 PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)
9 True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)
10 PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)
11 PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)
12 Temperature in °C
13 Relative Humidity (%)
14 AH Absolute Humidity
"""

with open("air_data.csv", 'r') as f:
    data = list(csv.reader(f, delimiter=";"))
air_data_from_file = np.array(data[1:], dtype=np.str)


air_data = np.genfromtxt("air_data.csv", delimiter=";", skip_header=1)
print(air_data)
print(air_data[4:10,5])
print(air_data[2:10, 2: 10])

temp = air_data[4,5]
air_data[4,5] = 10
print(air_data[3:5,5])
air_data[4,5] = temp

co_concentration = air_data[:10, 2]
humidity = air_data[:10, 14]
for xy in zip(co_concentration, humidity):
    plt.plot(xy[0],xy[1],'gs')
    plt.annotate('(%s, %s)' % xy, xy=xy)

plt.show()

plt.scatter(co_concentration,humidity)
plt.show()


x = np.random.randint(low=0, high=10, size=10)
plt.figure()
plt.hist(x)

plt.show()

x = [100, 200, 300, 400, 500]
labels = ['first', 'second', 'third', 'fourth', 'fifth']

plt.pie(x,labels=labels,autopct='%1.1f%%')

plt.show()
