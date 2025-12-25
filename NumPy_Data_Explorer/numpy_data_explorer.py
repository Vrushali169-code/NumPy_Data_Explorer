import numpy as np
import time
print("NumPy Data Explorer Project Started")

# 1D array
arr1 = np.array([10, 20, 30, 40, 50])
# 2D array
arr2 = np.array([[1, 2, 3],
                [4, 5, 6]])

# Using built-in methods
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 2))
range_arr = np.arange(1, 11)
random_arr = np.random.randint(1, 100, size=10)
print("1D Array:")
print(arr1)
print("\n2D Array:")
print(arr2)


# Indexing
print("\nIndexing:")
print(arr1[0])        # first element of 1D array
print(arr2[1][2])     # element from 2D array (row 2, column 3)
# Slicing
print("\nSlicing:")
print(arr1[1:4])      # slicing 1D array
print(arr2[:, 1])     # all rows, 2nd column of 2D array

#Mathematical Oprations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(np.sqrt(a))
print(np.power(a,2))

#Axis-Wise Operations
matrix = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Row-wise sum:", np.sum(matrix, axis=1))
print("Column-wise sum:", np.sum(matrix,axis=0))

#Statistical Operations
data = np.array([15, 20, 35, 40, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:",np.max(data))

#Reshaping Arrays
arr = np.arange(1, 13)
reshaped_arr = arr.reshape(3, 4)
print(reshaped_arr)

#Broadcasting
matrix = np.array([[1, 2, 3],
            [4, 5, 6]])
scalar = 10
result = matrix + scalar
print(result)

#save and load numpy array
np.save("data/sample_array.npy",matrix)

loaded_array = np.load("data/sample_array.npy")
print(loaded_array)

py_list = list(range(1000000))
start = time.time()
py_list_result = [x * 2 for x in py_list]
print("Python List Time:", time.time()-start)

np_array = np.arange(1000000)
start = time.time()
np_result = np_array * 2
print("NumPy Array Time:", time.time()-start)