# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:56:06 2020

@author: agbon
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

distance_lower_bound = np.array([0, 801, 2001, 5501])
distance_upper_bound = np.array([800, 2000, 5500, 20000])    
fuel_burn = np.array([2.4, 3.42, 7.57, 6.29])   
passengers = np.array([136, 180, 291, 572])

#stacked column (4 column array in this case)
flight_burn_data = np.column_stack((distance_lower_bound,
                                    distance_upper_bound,
                                    fuel_burn,
                                    passengers))

#create a dataframe from the column stack object
df = pd.DataFrame(flight_burn_data, columns=['distance(lower bound)', 
                                              'distance(upper bound)',
                                              'fuel burn',
                                              'passengers'])

distance = input("Please enter flight distance (km): ")
distance = int(distance)


##basically filtering and then selecting the proper fuel burn value
filter1 = df['distance(lower bound)']<=distance
filter2 = df['distance(upper bound)']>=distance
fburn_select = df['fuel burn'].where(filter1 & filter2, axis=0) 
fburn_select = fburn_select.dropna()
fburn_select = fburn_select.iloc[0]


#passenger data filtering
passenger_select = df['passengers'].where(filter1 & filter2, axis=0) 
passenger_select = passenger_select.dropna()
passenger_select = passenger_select.iloc[0]


##other key data
total_fuel_burnt = fburn_select * distance 
passenger_load_factor = 0.8 
passenger_complete = passenger_load_factor * passenger_select 
kg_co2_kg_fuel = 3.15

##emissions calculations continued 
passenger_emissions1 = total_fuel_burnt / passenger_complete
passenger_emissions2 = passenger_emissions1 * kg_co2_kg_fuel

##account for re-routing inefficiencies
inefficiencies = 0.1 
additional_emissions = passenger_emissions2 * inefficiencies

emissions = passenger_emissions2 + additional_emissions
emissions = float(emissions)

print("Total emissions computed as: " + str(emissions) + "kg of CO2.")

##account for other greenhouse gasses 
additional_emissions_factor = 1.5
additional_GHG = emissions * additional_emissions_factor

total_emissions = additional_GHG + emissions 
total_emissions = float(total_emissions)


##here is where I need help
emission_graph_emissions = np.array([emissions, total_emissions])
emission_types = ['Base Emissions', 'Net-Zero Emissions']

#to define the number of columns in the chart
x_ticks = np.arange(len(emission_graph_emissions))
plt.bar(x_ticks, emission_graph_emissions, color='g', width = 0.2)
plt.xticks(x_ticks, ('Base Emissions', 'Net-Zero Emissions'))
plt.ylabel('Tonnes')
plt.show()


