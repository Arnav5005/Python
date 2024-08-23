import matplotlib.pyplot as plt

input = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input , squares , linewidth = 3)
# this will change the label type and graph thickness 
# use plt.plot(squares) to get output without thickness and it would have just plotted squares
plt.title("square numbers" , fontsize = 12)
plt.xlabel("Value", fontsize=11)
plt.ylabel("square of value" , fontsize = 11)
plt.tick_params(axis='both', labelsize=14) # the function tick_params() styles the tick marks 
plt.show()

