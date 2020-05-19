import matplotlib.pyplot as plt 
  
################ Some fake data

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
plt.plot(die, AoDtoPlot, color = 'r', label = 'AoD', linewidth = 3)
plt.plot(die, DoAtoPlot, color = 'g', label = 'DoA', linewidth = 3)
plt.plot(die, singletoPlot, color = 'b', label = 'singles', linewidth = 3)

# Any grid?
plt.grid(axis="x") # Options: x, y, both

# Label which x-axis coordinates?
plt.xticks(die)

# Label which y-axis coordinates?
plt.yticks([0, 10, 33, 100])

# Label the X-axis and Y-axis
plt.xlabel("$N$")
plt.ylabel("Probability of rolling $\geqslant N$ (in %)")

# Show legend
plt.legend()

# Save figure in your local directory
plt.savefig('graph.png')

# Show graph
