import numpy as np

a = np.array([2, 3, 5])
print(a)

# *** Creating a Range *** (start, end, skip)
r = np.arange(0, 12)
print(r)

# Reshape to two dim arr
t = r.reshape(3, 4)
print(t)

# Skip by 2
r = np.arange(1, 12, 2)
print(r)

# *** Line Space *** (Evenly Space)
linear_space = np.linspace(1, 12, 6)  # this wil get six float value between 1 - 12 ( 1, 3.2, 5.4, 7.6, 9.8, 12 )
print(linear_space)

# Recreate The Data to Two Dimensional Array you can use reshape(row, col)
two_dim_arr = linear_space.reshape(3, 2)
print(two_dim_arr)

# How Many Elements in a array
print("Size : ", linear_space.size)

# What the Shape
print("Linear Shape : ", linear_space.shape)
print("Two Dim Shape : ", two_dim_arr.shape)

# Get The Numpy Data Type
print("Data Type of Linear : ", linear_space.dtype)
print("Data Type of r : ", r.dtype)

# How Much Memory in Byte each Elements in Bytes
print("How Much Mem in lin : ", linear_space.itemsize)

# Creting Multi Dimensional Array
multi_dim_arr = np.array([[1, 2, 3], [4, 8, 9]])
print(multi_dim_arr)

# Comparing the Multi dim array directly, example :
print(multi_dim_arr > 4)  # it will give us two dimensional array but the value will be true or false

# Multiply all the array by three
print(multi_dim_arr * 3)

# Or Reassign by
multi_dim_arr *= 3
print(multi_dim_arr)  # Same Result


# *** Creating Empty Array Full of Zeros
zeros_arr = np.zeros((9,))  # Linear arr
print(zeros_arr)

zeros_arr = np.zeros((3, 4))
print(zeros_arr)

# *** Creating Empty Array Full of Ones
ones_arr = np.ones(10)  # Linear arr
print(ones_arr)

ones_arr = np.ones((2, 3))
print(ones_arr)


# *** Creating Array With Passing the Data type
new_arr = np.array([2, 3, 4], dtype=np.int16)
print(new_arr)
print(new_arr.dtype)
print("Memory of int16 : ", new_arr.itemsize, " Bytes")


# *** Creating Random Array
rand_arr = np.random.random((2, 3))  # random val between 0 to 1
# np.set_printoptions(precision=2, suppress=True) # Show only two decimal places
print(rand_arr)


# Creating Random Int Array
rand_arr_int = np.random.randint(1, 10, 5)  # Generate random value between 1 to 10, how much ? 5 times
print("Random Int : ", rand_arr_int)

# Sum The Array
print(rand_arr_int.sum())

# *** Creating new one
arr = np.random.randint(1, 13, 20)
print("ARR : ", arr)

# Some Func
print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.var())  # Variants
print(arr.std())  # Standard Deviation


# *** Another Cool Trick : Get Sum of Each Row
arr = np.random.randint(1, 10, 6)
arr = arr.reshape(3, 2)
print(arr)

sum_arr_row = arr.sum(axis=1)  # Horizontal Sum
sum_arr_col = arr.sum(axis=0)  # Vertical Sum
print(sum_arr_row)
print(sum_arr_col)


# *** Shuffle the Data
arr = np.arange(10)
print(arr)  # Sorted Value
np.random.shuffle(arr)  # Dont Need to Reassign
print(arr)

# Randomly Picked One value
choice = np.random.choice(arr)
print(choice)
