import numpy as np
# import matplotlib.pyplot as mlt

# Creating one dimensional array np.array([])
# one_dim= np.array([2,4,5])
# print(one_dim)
# print(one_dim.ndim)
# # print(type(one_dim))

# To check the total number of elements of an array
# print(one_dim.size)


# # Creating two dimensional array np.array([[],[]])
# two_dim= np.array([[2,4,5],[2,4,6]])
# print(two_dim)
# print(two_dim.ndim)
# # print(type(two_dim))]

#To Create empty matrixes by giving dimensions
# emp_arr=np.empty((2,5))
# print(emp_arr)

# # To create zero array np.zeros((dimension))
# zero_arr= np.zeros((2,4)).astype(int)
# print(zero_arr)
# zero_arr1=np.zeros((2,2))
# print(zero_arr1)

# To create one array np.ones((dimension))
# one_arr=np.ones(2)
# one_arr1= np.ones((2,3))
# one_arr2=np.ones((2,2),dtype=int)
# print(one_arr)
# print(one_arr1)
# print(one_arr2)

# To create array or matrix as you want with single numbers/element np.full((dimension),number,data_type)
# two_arr= np.full((2,4),5,int)
# two_arr1= np.full((1,3),2)
# print(two_arr)
# print(two_arr1)

# To Create one dimensional array by just giving the range of numbers np.arrange(start,end+1,difference)
# arr_arr= np.arange(1,11)
# arr_arr1= np.arange(1,11,2)
# print(arr_arr)
# print(arr_arr1)

# To create array by just giving the range and number of elements np.random.randint(start,end,no_of_elements)
# ran_arr=np.random.rand(1,50)
# print(ran_arr)
# ran_arr1= np.random.randint(1,10,20)
# print(ran_arr1)

# To find the dimension of array or knowing the shape calculation np.shape()
two_dim= np.array([[2,4,5],[2,4,6]])
# print(two_dim)
# print(np.shape(two_dim))
# print(two_dim.shape)        

# To change the current dimension of an array
# two_dim= two_dim.reshape(3,2)       # To change the dimension of an array
# print(two_dim)
# two_dim= two_dim.reshape(1,3,2)
# print(two_dim)

# To change the multidimentional array np.ravel()
one_dimension= two_dim.ravel()
# print(one_dimension)

# To change multiple dimensions array into one dimensional array np.flaten()
# two_dimension= one_dimension.flatten((2,3))
# print(two_dimension)

# To add arrays vertically, horizentallyy or element by elemnet (column by column)
# np.vstack(arr1,arr2)   np.hstack(arr1,arr2)    np.column_stack()
# one_dim1= np.array([2,4,5])
# one_dim2= np.array([2,43,34])
# print(np.vstack((one_dim1,one_dim2)))
# print(np.hstack((one_dim1,one_dim2)))
# print(np.column_stack((one_dim1,one_dim2)))

# To instersect and differenciate the array
# union= all elements of arrays 
# intersection1d= all matched elements
one_dim1= np.array([2,4,5])
one_dim2= np.array([2,43,34])
# print(np.union1d(one_dim1,one_dim2))
# print(np.intersect1d(one_dim1,one_dim2))
# print(np.setdiff1d(one_dim1,one_dim2))

#numpy array mathmatics
#To sum up the arrays   
one_dim1= np.array([2,4,5])
one_dim2= np.array([2,43,34])
print(np.sum([one_dim1,one_dim2]))

# # To sum up the array by horizentaly
# print(np.sum([one_dim1,one_dim2],axis=1))

# # To sum up the array by vertically
# print(np.sum([one_dim1,one_dim2],axis=0))

#Basic Addtion
one_dim1 = one_dim1 + 1
print(one_dim1)
print(one_dim1.size)

# #Basic Subtraction
# one_dim1= one_dim1 - 1
# print(one_dim1)

# #Basic Multiplication
# one_dim1=one_dim1 * 2
# print(one_dim1)

# #Basic Division
# one_dim1=one_dim1 / 2
# print(one_dim1)

# #Mean
# one_dim1=one_dim1.astype(int)
# print(np.mean(one_dim1))
# print(one_dim1.mean())

# #Median
# print(np.median(one_dim1))

# #Standard Deviation
# print(np.std(one_dim1))

#Numpy Matrix
#Access complete row
# two_dim= np.array([  [2,4,5],[7,8,9]])
# print(two_dim)
# print(two_dim[0])
# print(two_dim[1])

# #Access complete column
# print(two_dim[ :,1])
# print(two_dim[: ,0])

#Transpose Matrix
# print(two_dim)
# print(two_dim.transpose())

#dot products with two matrixes
# two_dim= np.array([  [2,5],       
#                       [7,9]])
# two_dim1=np.array([[1,55],
#                    [12,34]])
# print(two_dim)
# print(two_dim1)
# print(two_dim.dot(two_dim1))
# print(np.multiply(two_dim1,two_dim))

#To save the array
# np.save("num_py",two_dim)
# vs=np.load("num_py.npy")
# print(vs)
# print(vs.size)

# Matrix calculation
# arr1 = np.array([[2,3,4],[7,4,3]])
# arr2= np.array([[22,33,44],[2,3,4]])
# print(np.add(arr1,arr2))
# print(np.subtract(arr1,arr2))
# print(np.divide(arr1,arr2))
# print(np.multiply(arr1,arr2))

# #To find maximum value of an array
# print(arr1.max())

# #To find out the index of array of a maximum element
# print(arr1.argmax())

# #To find minimun value of an array
# print(arr1.min())
# print(arr1.min(axis=0))
# print(arr1.min(axis=1))

# #To find out the index of array of a minimum element
# print(arr1.argmin())

#Slicing of matrix
# arr_mat=np.arange(1,29).reshape(7,4)
# print(arr_mat)
# print(arr_mat[1])
# print(arr_mat[:,0])
# print(arr_mat[0:5,])
# print(arr_mat[0:5, 0:3])
# print("item size of arr_mat: ",arr_mat.itemsize, arr_mat.dtype)

# #concatination of matrix
# con_arr=np.arange(1,17).reshape(4,4)
# con_arr1= np.arange(1,17).reshape(4,4)
# print(con_arr)
# print(con_arr1)
# print(np.concatenate((con_arr,con_arr1),axis=1))

# #To split the matrix into equal parts np.split()
# print(np.split(con_arr,4))
# print(np.split(con_arr,2,axis=0))
# print(np.split(con_arr,2,axis=1))

#Trignometric operations sin cos tan
# x=76
# print(np.sin(x))
# print(np.cos(x))
# print(np.tan(x))
# x_sin=np.arange(0,2*np.pi,0.2)
# x_cos= np.arange(0,4*np.pi,0.4)
# print(x_sin)
# print(x_cos)
# print(x_cos.size,x_sin.size)
# print(mlt.plot(x_cos,x_sin))
# mlt.show()


#random functions
# ran_arr1=np.random.random(12)
# print(ran_arr1)
# ran_arr1=np.random.randint(4,8)
# print(ran_arr1)
# ran_arr1=np.random.randint(4,20,(2,2))
# print(ran_arr1)
# ran_arr1=np.random.randint(2,30,(2,3,3))
# print(ran_arr1)

#To fix the random array or matrix with elements
# np.random.seed(19)
# ran_arr1=np.random.random(12)
# print(ran_arr1)
# # ran_arr1=np.random.random(12)
# print(ran_arr1)
# ran_arr1=np.random.randint(4,20,(2,2))
# print(ran_arr1)
# ran_arr1=np.random.randint(4,20,6)
# print(ran_arr1)
#string operations
# first="my name is "
# second="Muhammad Abdullah."

# #concatinate
# print(first + second)
# print(np.add(first,second))

# #upper_case
# print(second.upper())

# #lower case
# print(second.lower())

# #capitalize case
# print(second.capitalize())

# #title case 
# print(second.title())

# #center case 
# print(second.center(60))
# print(np.char.center(second,60,fillchar="*"))
# print(np.char)

# exe_arr=np.linspace(1,11,22)
# exe_arr1 = np.arange(1,11,2)
# print(exe_arr1)
# print(exe_arr)
# print(exe_arr1 @ exe_arr)
# print("NumPy version:", np.__version__)
# a="Abdulllah"
# b="Mughal"
# c=a.join(b)
# print(c)
# d=a.concat(b)
# print(d)