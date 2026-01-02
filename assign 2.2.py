import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]
plt.bar(students, marks)
plt.title('Student Marks')
plt.show()

regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]
plt.pie(revenue, labels=regions, explode=[0.1, 0, 0, 0], autopct='%1.1f%%')
plt.show()

data = np.random.randint(1, 101, 1000)
plt.hist(data)
plt.show()
