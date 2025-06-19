import numpy as np
import pandas as pd

# DataFrames: Pandas DataFrames is two_dimensional, size_mutable, potentially heterogenueous tabluar data structure with labeled axes (row & columns)
# data= np.random.randint(1,13,(3,4))
# df1 = pd.DataFrame(data)
# print(df1)
# df=pd.DataFrame(data,index=["A","B","C"],columns=[11,22,33,44])
# print(df)
# df2=pd.DataFrame([[1,2,3],[2,3,5]],columns=["a","b","c"])
# print(df2)

#Create DataFrame by using dictionary
#Dictionary key show column name and value shows data of that columns in dataframe
# data1 = {'Name': ['Ali', 'Sara', 'Ahmed'], 'Age': [25, 28, 22]}
# df2= pd.DataFrame(data1)
# print(df2)

#Create dataframe by usign list-dictionary
# data2= [{"A":"Amir","B":"Bilal","C":"Calvin"},{"B":"Abdullah","A":"Burhan"}]
# df3= pd.DataFrame(data2)
# print(df3)

#To write csv file
# df1.to_csv("Data.csv", mode="a", index= False, header= True)


# To read csv file
# print(pd.read_csv("Data.csv"))

# To create a dataframe by using csv file
# df3= pd.read_csv("Data.csv")
# print(df3)

# To access all columns names of dataframe
# print(df3.columns)

# To access all index's of dataframes
# print(df3.index)

# To access just specified rows 
# df4= pd.read_csv("Data.csv", nrows=2)
# df5= pd.read_csv("Data.csv", nrows=3)
# print(df4)
# print(df5)

#To create DataFrame by using list-dictionary
# x=[{"ID":1,"Category":"Electronics","Region":"North","Sales":1200,"Profit":150,"Discount":50,"Rating":4.5},
#    {"ID":2,"Category":"Gurniture","Region":"West","Sales":560,"Profit":150,"Discount":50,"Rating":4.5},
#    {"ID":3,"Category":"Clothing","Region":"East","Sales":1250,"Profit":150,"Discount":50,"Rating":4.5},
#    {"ID":4,"Category":"Furniture","Region":"South","Sales":900,"Profit":150,"Discount":50,"Rating":2.5},
#    {"ID":5,"Category":"Electronics","Region":"North","Sales":1000,"Profit":150,"Discount":50,"Rating":3},
#    {"ID":6,"Category":"Clothing","Region":"East","Sales":1300,"Profit":150,"Discount":50,"Rating":4.5},
#    {"ID":7,"Category":"Furniture","Region":"West","Sales":2000,"Profit":150,"Discount":50,"Rating":4.5},
#    {"ID":8,"Category":"Electronics","Region":"North","Sales":1800,"Profit":150,"Discount":50,"Rating":4.5}]
# df=pd.DataFrame(x)
# df.to_csv("Data.csv",mode="w",index=False)

# To access specific columns of dataframe pd.usecols = [no of column]
# df= pd.read_csv("Data.csv",usecols=[2])
# print(df)
# df= pd.read_csv("Data.csv",usecols=[3,2])
# print(df)

#To skip specific rows of dataframes skiprows=[index of row]
# in skiprows function index starts from column title with 0.
# df= pd.read_csv("Data.csv")
# print(df)
# df= pd.read_csv("Data.csv", skiprows=2)
# print(df)
# df= pd.read_csv("Data.csv", skiprows=[1,8])
# print(df)

# To create a column of dataframe as an index index_col= "Column title" OR index of column
# df= pd.read_csv("Data.csv", index_col="ID")
# print(df)
# df.to_csv("Data.csv", mode="w")

#To create header of dataframe by using each row of dataframe . Header start our datafrom that specific position and skip other above remaining uper columns header= index of column
# df= pd.read_csv("Data.csv")
# print(df)
# print(pd.read_csv("Data.csv", header=1))
# print(pd.read_csv("Data.csv", header=2))
# print(pd.read_csv("Data.csv", header=2))

# To write string as header in dataframe by using prefix= string
# We should also use header=None with prefix it's mandatory
# df= pd.read_csv("Data.csv")
# print(df)
# df= pd.read_csv("Data.csv", header= None prefix= 'column' )
# print(df)

#To create name of columns of dataframe by using list using name= list
# df= pd.read_csv("Data.csv", skiprows= 1,names=["A","B","C","D","E","F","G"])
# print(df)

#To access top rows of dataframe head()
#To access buttomn rows of dataframe tail()
#To check all the data types of columns df.dtypes
# df= pd.read_csv("Data.csv")
# print(df)
# print(df.head(3))
# print(df.tail(2))
# print(df.dtypes)

#To change all the true value attributes to other values "true_value=list" 
# To change all the false value attributes to other value "false_value= ["No"] i.e.
# df= pd.read_csv("Data.csv",true_values=["yes"],false_values=["no"])
# print(df)

#Parameters of read_csv funcion
#header prefix naems head tail dtype true_values false_values

# To fill all unfilled values with some data or msg by using na_values= string OR list[]
# df= pd.read_csv("Data.csv" ,na_values= "not")
# print(df)
# df= pd.read_csv("Data.csv" ,na_values= ["not", "no value"])
# print(df)

# When want  to there should not b show NaN on screen for balnk cell we should use keep_default_na=False
# df= pd.read_csv("Data.csv" )
# print(df)
# df= pd.read_csv("Data.csv" , keep_default_na=False)
# print(df)

# when we want to check that value is null or not in dataframe we use df.isnull()
# df= pd.read_csv("Data.csv")
# print(df)
# print(df.isnull())
# print(df.isnull().sum())    # To check whether columns contain which numbers of null values
# print(df.isnull().sum().sum())      #To sum up all the null vlaus
# pd.notnull is also a function that is reverse process of isnull()

# df= pd.read_csv("Data.csv")
# print(df)
# print(df.fillna(0))
# print(df.fillna("Null"))

#To replace items or element in file use df.replace()
# df= pd.read_csv("Data.csv")
# print(df)
# df=df.replace(to_replace=900, value=1150)
# print(df)
# df=df.replace(1150,900)
# print(df)
# df=df.replace({"Sales":900}, "None")
# print(df)
#regex=True is use to change the specified values
# df=df.replace({"Discount":50},"50%",regex=False)
# print(df)
# print(df.info())
# print(df.describe())

#pd.interpulate(df) is use to fill null value by analyzing other uper or lower values
# df= pd.read_csv("Data.csv" )
# print(abs(-4.4))
# print(df)
# print(df.interpolate()) # it just give suggetion for integer


z={"Name":["Abdullah","Amir","Aziz","Asim","Ammar"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
df= pd.DataFrame(z,index=[1,2,3,4,5])
# print(df)

# pd.loc[(row/column index names)] It works like index functoin to access specif name of row or column
# Yes (for slices)
# print(df.loc[2])
# print(df.loc[[1,4]])
# print(df.loc[0:0,"Education"])
# print(df.loc[df["Education"]>10])

#pd.iloc[row index, column index] It works for access element for specific row or column
# NO (for slices)
# print(df.iloc[1])
# print(df.loc[1])
# print(df.iloc[[1,3]])
# print(df.iloc[:,0])
# print(df.iloc[:,1])
# print(df.iloc[[0,2]]) 

# pd.groupby() is use to split the data into groups based on some criteria.
#operations:# Spliting the object 
            # applying function
            # combining the result
# df=pd.read_csv("Data.csv")            
# grp= df.groupby(by = "Education"  ) #It checks whethter any of the group value not null then it gives true value.
# print(grp.groups)

#Merging dataframes by using pd.merge(df,df1)
xx={"Address":["Vehari","Lahore","Karachi","Multan","Islamabad"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
df1=pd.DataFrame(xx)
print(pd.merge(df,df1))
print(pd.merge(df1,df))
print(pd.merge(df,df1,on="Education")) #on is use to take both dataframes's columns as same or like primary key
print(pd.merge(df,df1,on=["Education","Department"],indicator=True)) 
pd.concat([df1, df], axis=0)  # Vertical (row-wise)
pd.concat([df1, df], axis=1)  # Horizontal (column-wise)

#To concatinate dataframes and series by verticaly adding large lenght pd.concat()
# s1=pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
# s2=pd.Series([6,7,8,9],index=["F","G","H","I"])
# sum=pd.concat([s1,s2])
# print(sum)

# z1={"Name":["Abdullah","Amir","Aziz","Asim","Ammar"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
# z2={"Name":["Abdullah","Amir","Aziz","Asim","Ammar"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
# df1= pd.DataFrame(z1,index=[1,2,3,4,5])
# df2= pd.DataFrame(z2,index=[6,7,8,9,10])
# print(pd.concat([df1,df2]))

# by x-axis series
# s1=pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
# s2=pd.Series([6,7,8,9],index=["A","B","C","D"],type=int)
# sum=pd.concat([s1,s2],axis=1)
# print(sum)

# by x-axix dataframe
# z1={"Name":["Abdullah","Amir","Aziz","Asim","Ammar"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
# z2={"Name":["Abdullah","Amir","Aziz","Asim","Ammar"],"Education":[14,12,15,10,12],"Department":["CS","IT","BBA","Eng","Zology"]}
# df1= pd.DataFrame(z1,index=[1,2,3,4,5])
# df2= pd.DataFrame(z2,index=[1,2,3,4,5])
# print(pd.concat([df1,df2],axis=1))


#To join or add other dataframe as column indexed
# outer and inner function are use with how (how='outer') to handle null values inner can't show null value and outer shows null value
# lsuffix='name' or rsuffix='name' is use to add the name into column of names
# df1=pd.DataFrame({
#     "A":[1,2,3,4,5],
#     "B":[6,7,8,9,10]
#     })
# df2=pd.DataFrame({
#      "C":[11,12,13,14,15],
#     "D":[16,17,18,19,20]
# })
# sum=df1.join(df2,lsuffix = '_01' )
# print(sum)
# sum=df2.join(df1, rsuffix="_02")
# print(sum)

# To add series or dataframe at the end of first dataframe or series
# df1=pd.DataFrame({
#     "A":[1,2,3,4,5],
#     "B":[6,7,8,9,10]
#     })
# df2=pd.DataFrame({
#      "A":[11,12,13,14,15],
#     "B":[16,17,18,19,20]
#     })
# print(df1.add(df2))

#df.pivot_table(index='...',columns='...')
#it is use to summarize multirows same data into one row and categroized into one row
# sample=pd.DataFrame([{"Name":"Abdullah","Model":2010,"no":10},
#                      {"Name":"Abdullah","Model":2009,"no":50},
#                      {"Name":"Abdullah","Model":2010,"no":40},
#                      {"Name":"Asim","Model":2010,"no":10},
#                      {"Name":"Asim","Model":2009,"no":40},
#                      {"Name":"Ali","Model":2010,"no":70},
#                      {"Name":"Asim","Model":2009,"no":90},
#                      {"Name":"Ali","Model":2010,"no":10}
#                      ])
# sample.to_csv("pivot.csv",index=False)
# print(sample.pivot_table(index="Name", columns="Model"))

#pd.melt() is use to melt our function as pivot function summarize all the dataframes a values.
#It Extend the size of dataframe by each column with just one value
# sample=pd.DataFrame([{"Name":"Abdullah","Model":2010,"no":10},
#                      {"Name":"Abdullah","Model":2009,"no":50},
#                      {"Name":"Abdullah","Model":2010,"no":40},
#                      {"Name":"Asim","Model":2010,"no":10},
#                      {"Name":"Asim","Model":2009,"no":40},
#                      {"Name":"Ali","Model":2010,"no":70},
#                      {"Name":"Asim","Model":2009,"no":90},
#                      {"Name":"Ali","Model":2010,"no":10}
                    #  ])
# print(pd.melt(sample))
 
# To melt just specific  column value as point and display details for melting process
# print(pd.melt(sample, id_vars=["Name"]))
# print(pd.melt(sample, id_vars=["Model"]))

#To unpivot specified type of data or value of column 
# print(pd.melt(sample, id_vars=["Model"],value_vars=["no"]))
# print(pd.melt(sample, id_vars=["Model"],value_vars=["Name"]))
# print(pd.melt(sample, id_vars=["no"],value_vars=["Name"]))
np.info(np.size)

