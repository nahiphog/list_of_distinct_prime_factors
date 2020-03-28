import statistics # To calculate the Mean, Median, Mode, Sample Variance
import numpy # To calculate the Confidence interval
import scipy.stats # To calculate skewness and kurtosis
from tabulate import tabulate
import matplotlib.pyplot as plt

# Name of list for the record drawn from Monte Carlo simulation
results_drawn = []

# Change this value
total_number_of_trials = 10 

# Compute confidence interval
confidence_level = 0.99
def mean_confidence_interval(data, confidence, runs):
    a = numpy.array(data)
    m, se = numpy.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., runs-1)
    return [m, m-h, m+h]
evaluate_c_i = mean_confidence_interval(results_drawn, confidence_level, total_number_of_trials)

final_report = [ 
["Mean",evaluate_c_i[0] ], ["Median",statistics.median(results_drawn)], ["Mode",statistics.mode(results_drawn)], 
["Sample variance",statistics.variance(results_drawn)], 
["Skewness",scipy.stats.skew(results_drawn)], ["Kurtosis" , scipy.stats.kurtosis(results_drawn)],
[f"{confidence_level * 100}% Confidence Interval", f"{evaluate_c_i[1] } ≤ Mean ≤ {evaluate_c_i[2] }"] ]

# Print the table of the statistical result
print(f"\n\t\t Monte Carlo simulation for {total_number_of_trials:,} trials\n" +
tabulate(final_report,["Statistical measure", "Output"], tablefmt="fancy_grid" , colalign=("right",)))

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




