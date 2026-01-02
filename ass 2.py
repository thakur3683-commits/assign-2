import numpy as np

arr = np.arange(1, 21)
arr.sum()
arr.mean()
np.median(arr)
arr.std()
np.where(arr > 10)

arr2d = np.arange(1, 17).reshape(4, 4)
arr2d
arr2d.T
arr2d.sum(axis=1)
arr2d.sum(axis=0)

a = np.random.randint(1, 21, (3, 3))
b = np.random.randint(1, 21, (3, 3))
a + b
a - b
a * b
a.dot(b)

one_d = np.arange(1, 13)
reshaped = one_d.reshape(3, 4)
reshaped[:2, -2:]
