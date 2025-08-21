import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2d)
print("First column:", arr2d[:, 0])
rand_arr = np.random.randint(1, 100, size=10)
print("Random array:", rand_arr)
print("Mean:", rand_arr.mean())
print("Max:", rand_arr.max())
print("Shape:", rand_arr.shape)
print("Broadcasting:\n", arr2d + np.array([10, 20, 30]))

