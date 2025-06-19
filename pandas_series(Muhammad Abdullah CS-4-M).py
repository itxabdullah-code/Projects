import pandas as pd
import numpy as np
print(pd.__version__) 

list_1= [1,2,3,"Pandas"]
print(list_1[0:2])

#create one dimensional tabel by using pd.series()
series_1= pd.Series(list_1)
series_2= pd.Series([1,2,3,"Abdullah"])
print(series_1)
print(series_2)


# To find out the type of series by using type()
print(type(series_1))
print(type(series_2))

#To change the index name or number of series elements
# series_3= pd.Series([1,2],index=["A","B"])
# print(series_3)

#To change the data type of series
series_3= pd.Series([1,2,0],index=["A","B","C"], dtype=bool)
print(series_3)
series_3= pd.Series([1,2],index=["A","B"], dtype=float)
print(series_3)

#To create the name of column in series 
# series_3= pd.Series([1,2],index=["A","B"], dtype=float, name="Data Value")
# print(series_3)

#To create a series table by just giving one value for every number of cell
# series_4=pd.Series(1,index=["A","B","C"])
# series_5= pd.Series(5,name="Pre")
# print(series_5)
# print(series_4)

#You can also create a series table by using dictionary
# dic_1={"A":"Abdullah","B":"Bilal","C":"Cavin"}
# series_6=pd.Series(dic_1,name="Dictoinary Series")
# print(series_6)

#To access the series by using index
# print(series_6["A"])

#To acceess the series elements by usign slicing
# print(series_6["A":"B"])

#To find maximum value from series
# print(max(series_6))

#To find minimum value from series
# print(min(series_6))

#To find the index of maximum & minimum value of series
# print("maximum value's index: ",np.argmax(series_6))
# print("minimum value's index: ",np.argmin(series_6))

#To relate elements and extraction form series
# series_7= pd.Series([11,22,33,44,55],name="Simple")
# print(series_7)
# print(series_7[series_7 < 30])

# Adding two series elements 
# series_7= pd.Series([11,22,33,44,55],name="Simple")
# series_8= pd.Series([1,2,3,4,5],name="Simple")
# print(series_7 + series_8)

# Subtraction of two series tables
# series_7= pd.Series([11,22,33,44,55],name="Simple")
# series_8= pd.Series([1,2,3,4,5],name="Simple")
# print(series_7 - series_8)

#Multipliying two series
# series_7= pd.Series([11,22,33,44,55],name="Simple")
# series_8= pd.Series([1,2,3,4,5],name="Simple")
# print(series_7 * series_8)

#Dividing two series
# series_7= pd.Series([11,22,33,44,55],name="Simple")
# series_8= pd.Series([1,2,3,4,5],name="Simple")
# series_9= pd.Series([3,4,5],name="Simple")
# print((series_7 / series_8))
# print((series_7 / series_8).astype(int)) 

#Handling not equal elements
# series_8= pd.Series([1,2,3,4,5],name="Simple")
# series_9= pd.Series([3,4,5],name="Simple")
# print(series_8+series_9,"NAN: Not A Number...")






