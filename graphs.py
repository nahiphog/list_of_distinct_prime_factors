import matplotlib.pyplot as plt 
  
################ Some fake data

import itertools as it
die = range(1, 21)
AoDRolls = [max(min(roll[0], roll[1]), min(roll[2], roll[3])) for roll in it.product(die, repeat=4)]
DoARolls = [min(max(roll[0], roll[1]), max(roll[2], roll[3])) for roll in it.product(die, repeat=4)]
singleRolls = die

AoDtoPlot ,DoAtoPlot, singletoPlot = [], [], []

for N in die:
  AoDWins = len([i for i in AoDRolls if i >= N])
  DoAWins = len([i for i in DoARolls if i >= N])
  singleWins = len([i for i in singleRolls if i >= N])
  AoDtoPlot.append(100 * AoDWins / len(AoDRolls))
  DoAtoPlot.append(100 * DoAWins / len(DoARolls))
  singletoPlot.append(100 * singleWins / len(singleRolls))
  
################

# Give a title to my graph 
plt.title('Probability distribution for different strategies') 
  
# Show dimension = Length x Height
figure = plt.figure(figsize=(10,6))

# Plot range of graph: Range = [xmin, xmax, ymin, ymax]
plt.axis([0, 20, 0, 110]) 

# Plot all the relevant graphs with colors, labels, and linewidth
# With dash lines: 'r--'
# With points: 'ro'
plt.plot(die, AoDtoPlot, color = 'r', label = 'AoD', linewidth = 3,  zorder=3) 
plt.plot(die, DoAtoPlot, color = 'g', label = 'DoA', linewidth = 3,  zorder=2.5)
plt.plot(die, singletoPlot, color = 'b', label = 'singles', linewidth = 3,  zorder=2)

# Any grid?
plt.grid("x") # Options: x, y, Both

# Label which x-axis coordinates?
plt.xticks(die)

# Label which y-axis coordinates?
plt.yticks([0, 10, 33, 100])

# Y-axis adjustments? LINEAR by default, {"linear", "log", "symlog", "logit", ...}
plt.yscale('linear')

# Label the X-axis and Y-axis
plt.xlabel("$N$")
plt.ylabel("Probability of rolling $\geqslant N$ (in %)")

# Show legend
plt.legend()

# Save figure in your local directory
plt.savefig('graph.png')

# Insert text in graph (In position X, position Y, and the actual text)
plt.text(10, 30, r'$\mu=100,\ \sigma=15$', rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')

# Insert an arrow with attached text at the end of it
plt.annotate('SOME RANDOM TEXT!', 
            xy=(10, 10), 
            xytext=(5, 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

# Draw a thick blue vline at x=0 that spans the upper quadrant of the yrange
plt.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')

# Draw a default hline at y=.5 that spans the middle half of the axes
plt.axhline(y=.5, xmin=0.25, xmax=0.75, linestyle ="--") # "--", ":", "--"
plt.axhline(y=.5, xmin=0.25, xmax=0.75)

plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
plt.axvspan(1.25, 1.55, facecolor='#2ca02c', alpha=0.5)

# Show graph
plt.show()

#################### 

# MANY GRAPHS

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(131) # DIMENSIONS 1x3 ==> 1st graph to be generated
plt.bar(names, values) # BAR GRAPH
plt.subplot(133) # DIMENSIONS 1x3 ==> 2nd graph to be generated
plt.scatter(names, values) # SCATTER GRAPH
plt.subplot(132)# DIMENSIONS 1x3 ==> 3rd graph to be generated 
plt.plot(names, values) # LINE GRAPH
plt.suptitle('Categorical Plotting')
plt.show()


################################################################################
############### PIE CHART
################################################################################

import matplotlib.pyplot as plt
from random import randint

results_drawn = [ randint(1,14) for _ in range(int(1e3)) ]

# Data to plot
labelzzz = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'
sizes = [results_drawn.count(integer) for integer in range(1, 14 + 1)]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, labels=labelzzz,
autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.show()
