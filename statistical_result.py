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
# 0. Minimum and Maximum value
["(Minimum sample, Maximum sample)", (min(results_drawn),max(results_drawn)) ],
# 1. Mean
["Mean", evaluate_c_i[0] ], 
# 2. Percentiles
["Median",statistics.median(results_drawn)],
["Percentiles", statistics.quantiles(results_drawn, n=4, method='inclusive') ], # Optional
["Interquartile range", scipy.stats.iqr(results_drawn, interpolation='midpoint')], # {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}   
# 3. Modes
["Mode",statistics.mode(results_drawn)], # PICK ONE OF THESE
["Modes",statistics.multimode(results_drawn)], # PICK ONE OF THESE
# 4. Measure of dispersion
["Sample variance",statistics.variance(results_drawn)], # PICK ONE OF THESE
["Population variance",statistics.pvariance(results_drawn)], # PICK ONE OF THESE
["Sample standard deviation",statistics.stdev(results_drawn)], # PICK ONE OF THESE
["Population standard deviation",statistics.pstdev(results_drawn)], # PICK ONE OF THESE
# 5. Distortion of symmetry
["Skewness",scipy.stats.skew(results_drawn)], ["Kurtosis" , scipy.stats.kurtosis(results_drawn)] ],
# 6. Confidence interval
[f"{confidence_level * 100}% Confidence Interval", f"{evaluate_c_i[1] } ≤ Mean ≤ {evaluate_c_i[2] }"] ]


# Print the table of the statistical result
header_of_table = ["Statistical measure", "Output"]
print(f"\n\t\t Monte Carlo simulation for {total_number_of_trials:,} trials\n" +
tabulate(final_report,header_of_table, tablefmt="fancy_grid" , colalign=("right",)))

####################################################################################
######### Accompany this table with a table with relative frequency with cut-off ###
####################################################################################

cut_off_point_in_percentage = 2
frequency_counter = []
for integer in range( min(results_drawn), max(results_drawn) + 1):
    relative_frequency = results_drawn.count(integer) /total_number_of_trials * 100 
    if relative_frequency > cut_off_point_in_percentage:
        frequency_counter.append( [integer, relative_frequency ])


print(f"\nMonte Carlo simulation for {total_number_of_trials:,} trials" , 
f"\n(only show percentages above {cut_off_point_in_percentage}%)\n" +
tabulate(frequency_counter,["Rerolls", "Relative frequency (%)"], tablefmt="fancy_grid" , numalign="center"))

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
frequency_count = [ results_drawn.count(element) * 100 / total_number_of_trials for element in all_different_results ]

plt.bar(all_different_results ,frequency_count,align='center') # A bar chart
plt.xlabel('X-AXIS')
plt.ylabel('Relative frequency (%)')
plt.title(f"Monte carlo simulation with {total_number_of_trials:,} runs")

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

