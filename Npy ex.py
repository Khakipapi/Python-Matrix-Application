import numpy as np

a = np.array([1, 2, 3], dtype='int16')
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# get dimesions
print(a.ndim)
print(b.ndim)

# get shape
print(a.shape)
print(b.shape)

# get type
print(a.dtype)
print(b.dtype)

# get size
print(a.itemsize)

# get total size
print(b.nbytes)

# Accessing and changing elements, rows ...
c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print('\n', c)

# get specific element [r, c]
print(c[1, 5])

# get specific row
print(c[1, :])

# get specific column
print(c[:, 2])

# getting fancy
print(c[0, 1:6:2])

# change an element
c[1, 5] = 20
print(c)
# change a series of elements
c[:, 2] = 5
print(c)

c[:, 2] = [1, 2]
print(c)

d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(d)
# get specific element (work outside in )
print(d[0, 1, 1])

# replace
d[:, 1, :] = [[9, 9, ], [8, 8]]
print(d)
# **********************************************************************************************
# Initializing different types of Arrays

# all zeros matrix
e = np.zeros((2, 3))
print(e)
# all 1's matrix
e1 = np.ones((4, 2, 2))
print(e1)

# any other number
e2 = np.full((2, 2), 3)
print(e2)

# to copy the shape of an existing array
e3 = np.full_like(b, 4)
print(e3)

# initialize an array of random numbers
f = np.random.rand(4, 2)
print()
print(f)

# to pass in a shape use
f1 = np.random.random_sample(c.shape)
print()
print(f1)
