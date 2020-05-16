##############################
############ LINE GRAPH
##############################
import matplotlib.pyplot as plt 
  
# x axis values 
x = [*range(1,21)]
# corresponding y axis values 
y = [frequencies_of_each_roll[index][1] /(20 ** 4) * 100 for index in range(20)] 
z = [frequencies_of_each_roll[index][2] /(20 ** 4) * 100 for index in range(20)] 
  
# Plot the graph and its legend
plt.plot(x,y, x,z)
plt.legend([ 'ADV of DISADV', 'DISADV of ADV'])
  
# naming the x axis 
plt.xlabel('Roll number')  
# naming the y axis 
plt.ylabel('Relative frequency (%)') 
  
# Give a title to my graph 
plt.title('Probability distribution for different strategies') 
  
# function to show the plot 
plt.show() 
