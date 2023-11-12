from matplotlib import pyplot as plt
import numpy as np

x = [20, 25, 37]
y = [25000, 40000, 60000]

plt.plot(x, y)
plt.xlabel("Age")
plt.ylabel('Salary')
plt.title('Salary by Age')
plt.show()
