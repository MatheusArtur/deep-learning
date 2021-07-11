# Numpy Exercise, Added resources on each question for further reading
import numpy as np
from numpy import linalg as LA


##### NumPy Array


# How to create an empty and a full NumPy array? # https://www.geeksforgeeks.org/how-to-create-an-empty-and-a-full-numpy-array/
empa = np.empty((3, 4), dtype=int)
print("Empty Array")
print(empa)

flla = np.full([3, 3], 55, dtype=int)
print("\n Full Array")
print(flla)

# Create a Numpy array filled with all zeros # https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
np.zeros((5,), dtype=int)

# Create a Numpy array filled with all ones # https://www.geeksforgeeks.org/create-a-numpy-array-filled-with-all-ones/
b = np.ones([3, 3], dtype = int) 

# Check whether a Numpy array contains a specified row # https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-155.php
num = np.arange(20)
arr1 = np.reshape(num, [4, 5])
print("Original array:")
print(arr1)
print([0, 1, 2, 3, 4] in arr1.tolist())
print([0, 1, 2, 3, 5] in arr1.tolist())
print([15, 16, 17, 18, 19] in arr1.tolist())

# How to Remove rows in Numpy array that contains non-numeric values? # https://www.geeksforgeeks.org/how-to-remove-rows-in-numpy-array-that-contains-non-numeric-values/
n_arr = np.array([[10.5, 22.5, 3.8],
                  [41, np.nan, np.nan]])
  
print("Given array:")
print(n_arr)
  
print("\nRemove all rows containing non-numeric elements")
print(n_arr[~np.isnan(n_arr).any(axis=1)])

# Remove single-dimensional entries from the shape of an array # https://www.w3resource.com/numpy/manipulation/squeeze.php#:~:text=The%20squeeze()%20function%20is,the%20shape%20of%20an%20array.&text=Input%20data.&text=Selects%20a%20subset%20of%20the,one%2C%20an%20error%20is%20raised.
a = np.array([[[0], [2], [4]]])
np.squeeze(a, axis=0).shape

# Find the number of occurrences of a sequence in a NumPy array # https://www.geeksforgeeks.org/find-the-number-of-occurrences-of-a-sequence-in-a-numpy-array/
arr = np.array([[2, 8, 9, 4], 
                   [9, 4, 9, 4],
                   [4, 5, 9, 7],
                   [2, 9, 4, 3]])
  
output = repr(arr).count("9, 4")

# Find the most frequent value in a NumPy array # https://www.geeksforgeeks.org/find-the-most-frequent-value-in-a-numpy-array/
x = np.array([1,2,3,4,5,1,2,1,1,1])
print(np.bincount(x).argmax())

# Combining a one and a two-dimensional NumPy Array # https://www.geeksforgeeks.org/combining-a-one-and-a-two-dimensional-numpy-array/
num_1d = np.arange(5)   
num_2d = np.arange(10).reshape(2,5) 
for a, b in np.nditer([num_1d, num_2d]):
    print("%d:%d" % (a, b),)

# How to build an array of all combinations of two NumPy arrays? # https://www.geeksforgeeks.org/how-to-build-an-array-of-all-combinations-of-two-numpy-arrays/
np.array(np.meshgrid([1, 2, 3], [4, 5], [6, 7])).T.reshape(-1,3)

# How to add a border around a NumPy array? # https://www.geeksforgeeks.org/how-to-add-a-border-around-a-numpy-array/
array = np.ones((2, 2))
array = np.pad(array, pad_width=1, mode='constant',
               constant_values=0)

# How to compare two NumPy arrays?
np.array_equal([1, 2], [1, 2])

# How to check whether specified values are present in NumPy array? # https://www.geeksforgeeks.org/how-to-check-whether-specified-values-are-present-in-numpy-array/
n_array = np.array([[2, 3, 0],
                    [4, 1, 6]])

# How to get all 2D diagonals of a 3D NumPy array? # https://www.geeksforgeeks.org/how-to-get-all-2d-diagonals-of-a-3d-numpy-array/
np_array = np.arange(3*4*5).reshape(3,4,5)
result = np.diagonal(np_array, axis1=1, axis2=2)

# Flatten a Matrix in Python using NumPy # https://www.geeksforgeeks.org/flatten-a-matrix-in-python-using-numpy/#:~:text=flatten()%20function%20we%20can,to%20one%20dimension%20in%20python.&text=order%3A'C'%20means%20to,%2C%20row%2Dmajor%20order%20otherwise.
gfg = np.array([[2, 3], [4, 5]])
flat_gfg = gfg.flatten()

# Flatten a 2d numpy array into 1d array # https://www.geeksforgeeks.org/python-flatten-a-2d-numpy-array-into-1d-array/
ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
print("initial array", str(ini_array1))
result = ini_array1.flatten()

# Move axes of an array to new positions # https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-52.php
x = np.zeros((2, 3, 4))
print(np.moveaxis(x, 0, -1).shape)
print(np.moveaxis(x, -1, 0).shape)

# Interchange two axes of an array # https://www.geeksforgeeks.org/numpy-swapaxes-function-python/
arr = np.array([[2, 4, 6]])
gfg = np.swapaxes(arr, 0, 1)
print (gfg)

# NumPy – Fibonacci Series using Binet Formula # https://www.geeksforgeeks.org/numpy-fibonacci-series-using-binet-formula/
a = np.arange(1, 11)
lengthA = len(a)
sqrtFive = np.sqrt(5)
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive))
print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn))

# Counts the number of non-zero values in the array # https://www.geeksforgeeks.org/numpy-count_nonzero-method-python/
arr = [[0, 1, 2, 3, 0], [0, 5, 6, 0, 7]]
gfg = np.count_nonzero(arr)
print (gfg) 

# Count the number of elements along a given axis # https://www.geeksforgeeks.org/numpy-size-function-python/
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.size(arr, 0))
print(np.size(arr, 1))

# Trim the leading and/or trailing zeros from a 1-D array # https://www.geeksforgeeks.org/numpy-trim_zeros-in-python/
gfg = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
res = np.trim_zeros(gfg)
print(res)

# Change data type of given numpy array # https://www.tutorialspoint.com/change-data-type-of-given-numpy-array-in-python#:~:text=We%20have%20a%20method%20called,()%20method%20of%20numpy%20array.
array = np.array([1.5, 2.6, 3.7, 4.8, 5.9])
array = array.astype(np.int32)

# Reverse a numpy array # https://www.geeksforgeeks.org/python-reverse-a-numpy-array/
ini_array = np.array([1, 2, 3, 6, 4, 5])

print("initial array", str(ini_array))
print("type of ini_array", type(ini_array))

res = np.flipud(ini_array)

print("final array", str(res))

# How to make a NumPy array read-only? # https://www.geeksforgeeks.org/how-to-make-a-numpy-array-read-only/
a = np.zeros(11)
print("Before any change ")
print(a)
  
a[1] = 2
print("Before after first change ")
print(a)
  
a.flags.writeable = False
print("After making array immutable on attempting  second change ")
a[1] = 7


###### Questions on NumPy Matrix


# Get the maximum value from given matrix # https://numpy.org/doc/stable/reference/generated/numpy.matrix.max.html
x = np.matrix(np.arange(12).reshape((3,4)));x
([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
x.max()

# Get the minimum value from given matrix # https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html

x = -np.matrix(np.arange(12).reshape((3,4))); x
([[  0,  -1,  -2,  -3],
        [ -4,  -5,  -6,  -7],
        [ -8,  -9, -10, -11]])
x.min()


# Find the number of rows and columns of a given matrix using NumPy # https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-26.php
m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)

# Select the elements from a given matrix # https://numpy.org/doc/stable/reference/generated/numpy.select.html
x = np.arange(10)
condlist = [x<3, x>5]
choicelist = [x, x**2]
np.select(condlist, choicelist)

# Find the sum of values in a matrix # https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html
x = np.matrix([[1, 2], [4, 3]])
x.sum()

# Calculate the sum of the diagonal elements of a NumPy array # https://www.geeksforgeeks.org/calculate-the-sum-of-the-diagonal-elements-of-a-numpy-array/
n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
print("Numpy Matrix is:")
print(n_array)
trace = np.trace(n_array)
print("\nTrace of given 3X3 matrix:")
print(trace)

# Adding and Subtracting Matrices in Python # https://www.geeksforgeeks.org/adding-and-subtracting-matrices-in-python/
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])
  
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
print("Addition of two matrix")
print(np.add(A, B))

# Ways to add row/columns in numpy array # https://www.geeksforgeeks.org/python-ways-to-add-row-columns-in-numpy-array/
ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
print("initial_array : ", str(ini_array))

column_to_be_added = np.array([1, 2, 3])
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))
 
print ("resultant array", str(result))

# Matrix Multiplication in NumPy # https://numpy.org/doc/stable/reference/generated/numpy.dot.html
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b)

# Get the eigen values of a matrix # https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html
x = np.random.random()
Q = np.array([[np.cos(x), -np.sin(x)], [np.sin(x), np.cos(x)]])
LA.norm(Q[0, :]), LA.norm(Q[1, :]), np.dot(Q[0, :],Q[1, :])

# How to Calculate the determinant of a matrix using NumPy? # https://www.geeksforgeeks.org/how-to-calculate-the-determinant-of-a-matrix-using-numpy/
n_array = np.array([[50, 29], [30, 44]])
  
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
  
print("\nDeterminant of given 2X2 matrix:")
print(int(det))

# How to inverse a matrix using NumPy # https://www.geeksforgeeks.org/how-to-inverse-a-matrix-using-numpy/
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
  
print(np.linalg.inv(A))

# How to count the frequency of unique values in NumPy array? # https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-94.php
a = np.array( [10,10,20,10,20,20,20,30, 30,50,40,40] )
print("Original array:")
print(a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))

# Multiply matrices of complex numbers using NumPy in Python

# Compute the outer product of two given vectors using NumPy in Python

# Calculate inner, outer, and cross products of matrices and vectors using NumPy

# Compute the covariance matrix of two given NumPy arrays

# Convert covariance matrix to correlation matrix using Python

# Compute the Kronecker product of two mulitdimension NumPy arrays

# Convert the matrix into a list


###### Questions on NumPy Indexing


# Replace NumPy array elements that doesn’t satisfy the given condition

# Return the indices of elements where the given condition is satisfied

# Replace NaN values with average of columns

# Replace negative value with zero in numpy array

# How to get values of an NumPy array at certain index positions?

# Find indices of elements equal to zero in a NumPy array

# How to Remove columns in Numpy array that contains non-numeric values?

# How to access different rows of a multidimensional NumPy array?

# Get row numbers of NumPy array having element larger than X

# Get filled the diagonals of NumPy array

# Check elements present in the NumPy array

# Combined array index by index


##### Questions on NumPy Linear Algebra


# Find a matrix or vector norm using NumPy

# Calculate the QR decomposition of a given matrix using NumPy

# Compute the condition number of a given matrix using NumPy

# Compute the eigenvalues and right eigenvectors of a given square array using NumPy?

# Calculate the Euclidean distance using NumPy


###### Questions on NumPy Random


# Create a Numpy array with random values

# How to choose elements from the list with different probability using NumPy?

# How to get weighted random choice in Python?

# Generate Random Numbers From The Uniform Distribution using NumPy

# Get Random Elements form geometric distribution

# Get Random elements from Laplace distribution

# Return a Matrix of random values from a uniform distribution

# Return a Matrix of random values from a Gaussian distribution

###### Questions on NumPy Sorting and Searching

# How to get the indices of the sorted array using NumPy in Python?

# Finding the k smallest values of a NumPy array

# How to get the n-largest values of an array using NumPy?

# Sort the values in a matrix

# Filter out integers from float numpy array

# Find the indices into a sorted array


##### Questions on NumPy Mathematics


# How to get element-wise true division of an array using Numpy?

# How to calculate the element-wise absolute value of NumPy array?

# Compute the negative of the NumPy array

# Multiply 2d numpy array corresponding to 1d array

# Computes the inner product of two arrays

# Compute the nth percentile of the NumPy array

# Calculate the n-th order discrete difference along the given axis

# Calculate the sum of all columns in a 2D NumPy array

# Calculate average values of two given NumPy arrays

# How to compute numerical negative value for all elements in a given NumPy array?

# How to get the floor, ceiling and truncated values of the elements of a numpy array?

# How to round elements of the NumPy array to the nearest integer?

# Find the round off the values of the given matrix

# Determine the positive square-root of an array

# Evaluate Einstein’s summation convention of two multidimensional NumPy arrays


##### Questions on NumPy Statistics


# Compute the median of the flattened NumPy array

# Find Mean of a List of Numpy Array

# Calculate the mean of array ignoring the NaN value

# Get the mean value from given matrix

# Compute the variance of the NumPy array

# Compute the standard deviation of the NumPy array

# Compute pearson product-moment correlation coefficients of two given NumPy arrays

# Calculate the mean across dimension in a 2D NumPy array

# Calculate the average, variance and standard deviation in Python using NumPy

# Describe a NumPy Array in Python


##### Questions on Polynomial


# Define a polynomial function

# How to add one polynomial to another using NumPy in Python?

# How to subtract one polynomial to another using NumPy in Python?

# How to multiply a polynomial to another using NumPy in Python?

# How to divide a polynomial to another using NumPy in Python?

# Find the roots of the polynomials using NumPy

# Evaluate a 2-D polynomial series on the Cartesian product

# Evaluate a 3-D polynomial series on the Cartesian product


##### Questions on NumPy Strings


# Repeat all the elements of a NumPy array of strings

# How to split the element of a given NumPy array with spaces?

# How to insert a space between characters of all the elements of a given NumPy array?

# Find the length of each string element in the Numpy array

# Swap the case of an array of string

# Change the case to uppercase of elements of an array

# Change the case to lowercase of elements of an array

# Join String by a seperator

# Check if two same shaped string arrayss one by one

# Count the number of substrings in an array

# Find the lowest index of the substring in an array

# Get the boolean array when values end with a particular character

# More Questions on NumPy

# Different ways to convert a Python dictionary to a NumPy array

# How to convert a list and tuple into NumPy arrays?

# Ways to convert array of strings to array of floats

# Convert a NumPy array into a csv file

# How to Convert an image to NumPy array and save it to CSV file using Python?

# How to save a NumPy array to a text file?

# Load data from a text file

# Plot line graph from NumPy array

# Create Histogram using NumPy
