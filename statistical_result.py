import statistics # To calculate the mean and median
import numpy as np # To calculate the variance
import pylab as p  # To calculate skewness
import scipy.stats
from scipy.stats import kurtosis
from scipy.stats import skew 
import pylab as p  # for Kurtosis
from tabulate import tabulate
import matplotlib.pyplot as plt

confidence_level = 0.99
def mean_confidence_interval(data, confidence):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return [m-h, m+h]

# Name of list for the record drawn from Monte Carlo simulation
results_drawn = []

# Change this value
total_number_of_trials = 10 

final_report = [ 
["Mean",statistics.mean(results_drawn)], ["Median",statistics.median(results_drawn)], ["Mode",statistics.mode(results_drawn)], 
["Variance",np.var(results_drawn)], ["Skewness",skew(results_drawn)], ["Kurtosis" , kurtosis(results_drawn)],
[f"{confidence_level * 100}% Confidence Interval", 
f"( {mean_confidence_interval(results_drawn, confidence_level)[0] } ≤ Mean ≤ {mean_confidence_interval(results_drawn, confidence_level)[1] } ) "] 
]

# Print the table of the statistical result
headers = ["Statistical measure", "Output"]
print(f"\n\t\tMonte Carlo simulation for {total_number_of_trials} trials.\n" + 
tabulate(final_report,headers, tablefmt="psql" , colalign=("right",))


############################################################
######### Accompany this table with a histogram ############
############################################################
plt.hist(results_drawn, 300, histtype = 'bar', facecolor = 'green')
plt.style.use('seaborn-whitegrid')
plt.ylabel("Y-AXIS LABEL")
plt.xlabel("X-AXIS LABEL")
plt.title(f"TITLE with {(total_number_of_trials)} runs")
plt.axis([1,10,0,results_drawn.count(statistics.mode(results_drawn)) * 1.2])
plt.show()

####################################################################################
######### Accompany this table with a histogram with relative frequency ############
####################################################################################

all_different_results = list( dict.fromkeys(results_drawn) )
frequency_count = [ results_drawn.count(element) * 100 / len(final_result) for element in all_different_results ]

plt.bar(all_different_results ,frequency_count,align='center') # A bar chart
plt.xlabel('X-AXIS')
plt.ylabel('Relative frequency (%)')
plt.title(f"Monte carlo simulation with {(total_number_of_trials)} runs")

draw_horizontal_lines = False
if draw_horizontal_lines == True:
    for i in range(len(frequency_count)):
        plt.hlines(frequency_count[i],0,all_different_results[i]) # Here you are drawing the horizontal lines

plt.show()

####################################################################################
######### Timer basis ##############################################################
####################################################################################
import random
from time import time

duration_to_run_in_seconds = 5

terminate_experiment = time() +  duration_to_run_in_seconds

results_drawn = []

while time() < terminate_experiment:
    results_drawn.append(  random.randint(0, 10) )

print(len(results_drawn))




