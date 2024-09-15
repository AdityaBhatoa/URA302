import numpy as np

# 1.1 Create a 1D array with values from 5 to 25
one_d_array = np.arange(5, 26)
print("1D array:", one_d_array)

# 1.2 Generate a 2D array with random integers between 10 and 50
two_d_array = np.random.randint(10, 50, (3, 4))
print("2D array:\n", two_d_array)

# 2.1 Get properties of the 1D array
print("1D array - Shape:", one_d_array.shape)
print("1D array - Size:", one_d_array.size)
print("1D array - Data type:", one_d_array.dtype)

# 2.2 Get properties of the 2D array
print("2D array - Shape:", two_d_array.shape)
print("2D array - Size:", two_d_array.size)
print("2D array - Data type:", two_d_array.dtype)

# 3.2 Perform element-wise operations on two arrays
array_x = np.array([2, 4, 6, 8, 10])
array_y = np.array([1, 3, 5, 7, 9])

print("Addition:", array_x + array_y)
print("Subtraction:", array_x - array_y)
print("Element-wise multiplication:", array_x * array_y)
print("Element-wise division:", array_x / array_y)

# 4.2 Multiply each element of a 2D array by 5
array_2d = np.arange(1, 10).reshape(3, 3)
result = array_2d * 5
print("Result:\n", result)

# 5.2 Extract specific rows and columns from a 4x4 array
array_4x4 = np.arange(10, 26).reshape(4, 4)
second_row = array_4x4[1, :]
last_column = array_4x4[:, -1]
print("Second row:", second_row)
print("Last column:", last_column)

# 5.3 Set the first row of the 4x4 array to zeros
array_4x4[0, :] = 0
print("Modified array:\n", array_4x4)

# 6.2 Find elements in a 1D array greater than 30
array_random = np.random.randint(20, 41, 10)
greater_than_30 = array_random[array_random > 30]
print("Elements greater than 30:", greater_than_30)

# 7.2 Reshape a 1D array into a 3x4 2D array
array_to_reshape = np.arange(11, 23)
reshaped_array = array_to_reshape.reshape(3, 4)
print("Reshaped array:\n", reshaped_array)

# 8.2 Matrix operations: multiplication and transpose
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
product = np.matmul(matrix1, matrix2)
transpose_matrix1 = matrix1.T

print("Matrix multiplication:\n", product)
print("Transpose of Matrix A:\n", transpose_matrix1)

# 9.2 Statistical operations on a random 1D array
array_for_stats = np.random.randint(10, 61, 15)
mean_value = np.mean(array_for_stats)
median_value = np.median(array_for_stats)
std_dev_value = np.std(array_for_stats)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard deviation:", std_dev_value)

# 10.2 Matrix operations: determinant, inverse, and eigenvalues
matrix3 = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
det = np.linalg.det(matrix3)
inv = np.linalg.inv(matrix3)
eigenvalues, eigenvectors = np.linalg.eig(matrix3)

print("Determinant:", det)
print("Inverse:\n", inv)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
