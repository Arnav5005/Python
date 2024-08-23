import matplotlib.pyplot as plt
# scatter : 
# you might plot small values in one color and larger values in a different color. You could also plot a large data 
# set with one set of styling options and then emphasize individual points by replotting them with different options.

# Method 1

x_value = [1,2,3,4,5,6]
y_value = [1,4,9,16,25,36]
plt.scatter(x_value , y_value , s=20) # use plt.scatter(2,4,s=200)to highlight a single point
# set chart title and label axes
plt.title("square numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("square of value" , fontsize = 11)
plt.tick_params(axis = 'both' , which = 'major' , labelsize = 11)
plt.show()

# Method 2

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , s = 1)
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.show()

# Removing Outlines from Data Points

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , edgecolor = 'none' , s = 2)
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.show()

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , c ='green' , edgecolor = 'none' , s = 2) # you can also put color code instead of color name
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.show()

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , c = 'gold' , edgecolor = 'none' , s = 2) 
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.show()

# Using a Colormap
# A colormap is a series of colors in a gradient that moves from a starting to ending color. Colormaps are used in 
# visualizations to emphasize a pattern in the data. For example, you might make low values a light color and high 
# values a darker color.The pyplot module includes a set of built-in colormaps.

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , c = y_values, cmap = plt.cm.Blues , edgecolor = 'none' , s = 2) 
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.show()

# http://matplotlib.org/ here you can access all the colourmaps 

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter (x_values , y_values , c = y_values, cmap = plt.cm.Blues , edgecolor = 'none' , s = 2) 
plt.title("sqaures of numbers" , fontsize = 12)
plt.xlabel("value" , fontsize = 11)
plt.ylabel("squares", fontsize = 11)
# set range for axes
plt.axis([0, 1100, 0, 1100000])
plt.savefig('plots.png', bbox_inches = 'tight')