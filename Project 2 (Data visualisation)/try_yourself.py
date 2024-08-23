import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values , y_values , c = "green" , edgecolor = 'none' , s=10)
plt.title('Cubic numbers' , fontsize = 12)
plt.xlabel('values' , fontsize = 11)
plt.ylabel('cube' , fontsize = 11)
plt.axis([0,5100 , 0,126000000])
plt.show()