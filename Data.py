# -*- coding: utf-8 -*-
"""Numpy and Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Ow1VLaE2H5cThFIkqs0dAI13JzYUgQW

# Python Basic operations
"""

class Disease:
  def __init__(self, disease = 'Depression'):
    self.type = disease
    
  def getName(self):
    print("Mental Health Diseases: {0}".format(self.type))

d1 = Disease('Social Anxiety Disorder')
d1.getName()

# Try Catch Block
# The try block will generate a NameError, because x is not defined:

try:
  print(y)
except NameError:
  print("Well, the variable y is not defined")
except:
  print("OMG, Something else went wrong")

try:
 Value = int(input("Type a number between 1 and 10:"))
except ValueError:
  print("You must type a number between 1 and 10!")
else:
  if (Value > 0) and (Value <= 10):
      print("You typed: ", Value)
  else:
      print("The value you typed is incorrect!")



"""# Numpy Array Basics"""

# importing numpy
import numpy as np

# Defining 1D array
my1DArray = np.array([1, 8, 27, 64])
print(my1DArray)

# Defining and printing 2D array
my2DArray = np.array([[1, 2, 3, 4], [2, 4, 9, 16], [4, 8, 18, 32]])
print(my2DArray)

#Defining and printing 3D array
my3Darray = np.array([[[ 1, 2 , 3 , 4],[ 5 , 6 , 7  ,8]], [[ 1,  2,  3,  4],[ 9, 10, 11, 12]]])
print(my3Darray)

# Print out memory address
print(my2DArray.data)

# Print the shape of array
print(my2DArray.shape)

# Print out the data type of the array
print(my2DArray.dtype)

"""
Print the stride of the array.

So what is stride of array?  It is the number of locations in memory between 
beginnings of successive array elements, measured in bytes or in units of the
size of the array's elements
"""
print(my2DArray.strides)

"""# Array using numpy built-in functions"""

# Array of ones
ones = np.ones((3,4))
print(ones)

# Array of zeros
zeros = np.zeros((2,3,4),dtype=np.int16)
print(zeros)

# Array with random values
np.random.random((2,2))

# Empty array
emptyArray = np.empty((3,2))
print(emptyArray)

# Full array
fullArray = np.full((2,2),7)
print(fullArray)

# Array of evenly-spaced values
evenSpacedArray = np.arange(10,25,5)
print(evenSpacedArray)

# Array of evenly-spaced values
evenSpacedArray2 = np.linspace(0,2,9)
print(evenSpacedArray2)

"""# Numpy array and file operations"""

# Save a numpy array into file
x = np.arange(0.0,50.0,1.0)
np.savetxt('data.out', x, delimiter=',')

# Loading numpy array from text
z = np.loadtxt('data.out', unpack=True)
print(z)

# Loading numpy array using genfromtxt method
my_array2 = np.genfromtxt('data.out',
                      skip_header=1,
                      filling_values=-999)
print(my_array2)

"""# Inspecting numpy arrays"""

# Print the number of `my2DArray`'s dimensions
print(my2DArray.ndim)

# Print the number of `my2DArray`'s elements
print(my2DArray.size)

# Print information about `my2DArray`'s memory layout
print(my2DArray.flags)

# Print the length of one array element in bytes
print(my2DArray.itemsize)

# Print the total consumed bytes by `my2DArray`'s elements
print(my2DArray.nbytes)

"""# Broadcasting in NumPy
Broadcasting is a mechanism that permits `NumPy` to operate with arrays of different shapes when performing arithmetic operations.
"""

# Rule 1: Two dimensions are operatable if they are equal
# Create an array of two dimension
A =np.ones((6, 8))

# Shape of A
print(A.shape)

# Create another array
B = np.random.random((6,8))

# Shape of B
print(B.shape)

# Sum of A and B, here the shape of both the matrix is same.
print(A + B)

# Rule 2: Two dimensions are also comptable when one of them is 1
# Initialize `x`
x = np.ones((3,4))
print(x)

# Check shape of `x`
print(x.shape)

# Initialize `y`
y = np.arange(4)
print(y)

# Check shape of `y`
print(y.shape)

# Subtract `x` and `y`
x - y

# Rule 3: Arrays can be broadcasted together if they are compatible in all dimensions

x = np.ones((6,8))
y = np.random.random((10, 1, 8))
print(x + y)

# Analytical question
"""
The dimensions of x(6,8) and y(10,1,8) are diffrent. However, it is possible 
to add them. Why is that? Also, change y(10,2,8) or y(10,1,4) it will 
give ValueError. Can you find out why?
"""

"""# Numpy and mathematics at work"""

# Basica operations (+, -, *, /, %)
x = np.array([[1, 2, 3], [2, 3, 4]])
y = np.array([[1, 4, 9], [2, 3, -2]])

# Add two array
add = np.add(x, y)
print(add)

# Subtract two array
sub = np.subtract(x, y)
print(sub)

# Multipley two array
mul = np.multiply(x, y)
print(mul)

# Divide x, y
div = np.divide(x,y)
print(div)

# Calculated the remainder of x and y
rem = np.remainder(x, y)
print(rem)

"""# Subset, Slice, And Index Arrays"""

x = np.array([10, 20, 30, 40, 50])

# Select items at index 0 and 1
print(x[0:2])

# Select item at row 0 and 1 and column 1 from 2D array
y = np.array([[ 1,  2,  3,  4], [ 9, 10, 11 ,12]])
print(y[0:2, 1])

# Specifying conditions
biggerThan2 = (y >= 2)
print(y[biggerThan2])

# Importing pandas
import pandas as pd

"""# Can you set default parameters in Pandas?"""

print("Pandas Version:", pd.__version__)

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

"""# Data strcutre of pandas


*   Series
*   DataFrames
"""

series = pd.Series([2, 3, 7, 11, 13, 17, 19, 23])
print(series)

# Creating dataframe from Dictionary
dict_df = [{'A': 'Apple', 'B': 'Ball'},{'A': 'Aeroplane', 'B': 'Bat', 'C': 'Cat'}]
dict_df = pd.DataFrame(dict_df)
print(dict_df)
  
# Creating dataframe from Series
series_df = pd.DataFrame({
    'A': range(1, 5),
    'B': pd.Timestamp('20190526'),
    'C': pd.Series(5, index=list(range(4)), dtype='float64'),
    'D': np.array([3] * 4, dtype='int64'),
    'E': pd.Categorical(["Depression", "Social Anxiety", "Bipolar Disorder", "Eating Disorder"]),
    'F': 'Mental health',
    'G': 'is challenging'
})
print(series_df)

# Creating a dataframe from ndarrays
sdf = {
    'County':['Østfold', 'Hordaland', 'Oslo', 'Hedmark', 'Oppland', 'Buskerud'],
    'ISO-Code':[1,2,3,4,5,6],
    'Area': [4180.69, 4917.94, 454.07, 27397.76, 25192.10, 14910.94],
    'Administrative centre': ["Sarpsborg", "Oslo", "City of Oslo", "Hamar", "Lillehammer", "Drammen"]
    }
sdf = pd.DataFrame(sdf)
print(sdf)

"""# Loading a dataset into Pandas DataFrame"""

import pandas as pd
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'ethnicity', 'gender','capital_gain','capital_loss','hours_per_week','country_of_origin','income']
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',names=columns)
df.head(10)

# Displays the rows, columns, data types and memory used by the dataframe
df.info()

# Displays the no of data points and columns in the dataframe
df.shape

# Display all columns of the dataframe
df.columns

# Displays summary statistics for each numerical column in the dataframe
df.describe()

"""# Selecting rows and columns in the dataframe"""

# Selects a row
df.iloc[10] 

# Selects 10 rows             
df.iloc[0:10]

# Selects a range of rows           
df.iloc[10:15]            

 # Selects the last 2 rows
df.iloc[-2:]  

# Selects every other row in columns 3-5
df.iloc[::2, 3:5].head()

import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame({'F': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 5), columns=list('EDCBA'))],
               axis=1)
df.iloc[0, 2] = np.nan
df

# Define a function that should color the values that are less than 0 
def colorNegativeValueToRed(value):
  if value < 0:
    color = 'red'
  elif value > 0:
    color = 'black'
  else:
    color = 'green'

  return 'color: %s' % color

s = df.style.applymap(colorNegativeValueToRed, subset=['A','B','C','D','E'])
s

# Let us hightlight max value in the column with green background and min value with orange background
def highlightMax(s):
    isMax = s == s.max()
    return ['background-color: orange' if v else '' for v in isMax]

def highlightMin(s):
    isMin = s == s.min()
    return ['background-color: green' if v else '' for v in isMin]

df.style.apply(highlightMax).apply(highlightMin).highlight_null(null_color='red')

import seaborn as sns

cm = sns.light_palette("pink", as_cmap=True)

s = df.style.background_gradient(cmap=cm)
s

class Disease:
  def __init__(self, disease = 'Depression'):
    self.type = disease
    
  def getName(self):
    print("Mental Health Diseases: {0}".format(self.type))

d1 = Disease('Social Anxiety Disorder')
d1.getName()

try:
  Value = int(input("Type a number between 1 and 10:"))
except ValueError:
   print("You must type a number between 1 and 10!")
else:
   if (Value > 0) and (Value <= 10):
       print("You typed: ", Value)
   else:
       print("The value you typed is incorrect!")
