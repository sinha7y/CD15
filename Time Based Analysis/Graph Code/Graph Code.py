import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

# Read Matlab file
datasubj1 = scipy.io.loadmat("ae2223I_measurement_data_subj1.mat") # Subject 1
datasubj2 = scipy.io.loadmat("ae2223I_measurement_data_subj2.mat") # Subject 2
datasubj3 = scipy.io.loadmat("ae2223I_measurement_data_subj3.mat") # Subject 3
datasubj4 = scipy.io.loadmat("ae2223I_measurement_data_subj4.mat") # Subject 4
datasubj5 = scipy.io.loadmat("ae2223I_measurement_data_subj5.mat") # Subject 5
datasubj6 = scipy.io.loadmat("ae2223I_measurement_data_subj6.mat") # Subject 6

# Note:
#     | P   V   A
# _________________
#  NM | C1  C2  C3
#  M  | C4  C5  C6

#-----------------------------------Functions----------------------------------------

# RMS calcualtor given a 8192 by 5 array
def RMS_calculate_8192x5(input_array):

  RMS_array = ((np.sum((input_array**2), axis=0))/8192)**.5
  return RMS_array

# RMS calcualtor given a 1 by 5 array
def RMS_calculate_1x5(input_array):

  RMS_array = ((np.sum(input_array**2))/5)**.5
  return RMS_array

# Variance calculator given a 8192 by 5 array
def VAR_calculate_8192x5(input_array):

  total = [0, 0, 0, 0, 0]
  mean = np.sum(input_array, axis=0)/8192
  for row in input_array:
    value = (row-mean)**2
    total = total + value
  Var = total/8192

  return Var

# Variance calculator given a 1 by 5 array
def VAR_calculate_1x5(input_array):

  total = 0
  mean = np.sum(input_array)/5
  for element in input_array:
    value = (element-mean)**2
    total = total + value
  Var = total/5

  return Var

def maximum(matrix,t):

  a=np.zeros((5,2))
  for j in range (5):
    maxim=0
    timp=0
    for i in range (len(matrix)):
      if (matrix[i][j]>maxim):
        maxim=matrix[i][j]
        timp=t[i]
    a[j][0]=maxim
    a[j][1]=timp
  
  return (a)

def minimum(matrix,t):

  a=np.zeros((5,2))
  for j in range (5):
    minim=100000
    timp=0
    for i in range (len(matrix)):
      if (matrix[i][j]<minim):
        minim=matrix[i][j]
        timp=t[i]
    a[j][0]=minim
    a[j][1]=timp
  
  return (a)

def steepest_change(matrix,t):
  a=np.zeros((5,3))
  for j in range (5):
    maxim=0
    change=0
    timp=0
    for i in range (len(matrix)-2):
      slope1 = (matrix[i+1][j]-matrix[i][j])/0.01
      slope2 = (matrix[i+2][j]-matrix[i+1][j])/0.01
      slope = abs(slope2-slope1)
      if (slope>change):
        change=slope
        timp=t[i]
      if (abs(slope1)>maxim):
        maxim=slope1
    a[j][0]=change
    a[j][1]=timp
    a[j][2]=maxim

  return(a)

#-----------------------------------Subject 1----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj1['t'][0]         # Time
data1_C1 = datasubj1['data_C1']      # Data Condition 1
data1_C2 = datasubj1['data_C2']      # Data Condition 2
data1_C3 = datasubj1['data_C3']      # Data Condition 3
data1_C4 = datasubj1['data_C4']      # Data Condition 4
data1_C5 = datasubj1['data_C5']      # Data Condition 5
data1_C6 = datasubj1['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e1_C1       = data1_C1['e'][0][0].reshape(8192, 5)
u1_C1       = data1_C1['u'][0][0].reshape(8192, 5)
x1_C1       = data1_C1['x'][0][0].reshape(8192, 5)
ft1_C1      = data1_C1['ft'][0][0].reshape(8192,1)
fd1_C1      = data1_C1['fd'][0][0].reshape(8192,1)


e1_C2 = data1_C2['e'][0][0].reshape(8192, 5)
u1_C2 = data1_C2['u'][0][0].reshape(8192, 5)
x1_C2 = data1_C2['x'][0][0].reshape(8192, 5)
ft1_C2 = data1_C2['ft'][0][0].reshape(8192,1)
fd1_C2 = data1_C2['fd'][0][0].reshape(8192,1)


e1_C3 = data1_C3['e'][0][0].reshape(8192, 5)
u1_C3 = data1_C3['u'][0][0].reshape(8192, 5)
x1_C3 = data1_C3['x'][0][0].reshape(8192, 5)
ft1_C3 = data1_C3['ft'][0][0].reshape(8192,1)
fd1_C3 = data1_C3['fd'][0][0].reshape(8192,1)


e1_C4 = data1_C4['e'][0][0].reshape(8192, 5)
u1_C4 = data1_C4['u'][0][0].reshape(8192, 5)
x1_C4 = data1_C4['x'][0][0].reshape(8192, 5)
ft1_C4 = data1_C4['ft'][0][0].reshape(8192,1)
fd1_C4 = data1_C4['fd'][0][0].reshape(8192,1)


e1_C5 = data1_C5['e'][0][0].reshape(8192, 5)
u1_C5 = data1_C5['u'][0][0].reshape(8192, 5)
x1_C5 = data1_C5['x'][0][0].reshape(8192, 5)
ft1_C5 = data1_C5['ft'][0][0].reshape(8192,1)
fd1_C5 = data1_C5['fd'][0][0].reshape(8192,1)


e1_C6 = data1_C6['e'][0][0].reshape(8192, 5)
u1_C6 = data1_C6['u'][0][0].reshape(8192, 5)
x1_C6 = data1_C6['x'][0][0].reshape(8192, 5)
ft1_C6 = data1_C6['ft'][0][0].reshape(8192,1)
fd1_C6 = data1_C6['fd'][0][0].reshape(8192,1)

#-----------------------------------Subject 2----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj2['t'][0]         # Time
data2_C1 = datasubj2['data_C1']      # Data Condition 1
data2_C2 = datasubj2['data_C2']      # Data Condition 2
data2_C3 = datasubj2['data_C3']      # Data Condition 3
data2_C4 = datasubj2['data_C4']      # Data Condition 4
data2_C5 = datasubj2['data_C5']      # Data Condition 5
data2_C6 = datasubj2['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e2_C1       = data2_C1['e'][0][0].reshape(8192, 5)
u2_C1       = data2_C1['u'][0][0].reshape(8192, 5)
x2_C1       = data2_C1['x'][0][0].reshape(8192, 5)
ft2_C1      = data2_C1['ft'][0][0].reshape(8192,1)
fd2_C1      = data2_C1['fd'][0][0].reshape(8192,1)


e2_C2 = data2_C2['e'][0][0].reshape(8192, 5)
u2_C2 = data2_C2['u'][0][0].reshape(8192, 5)
x2_C2 = data2_C2['x'][0][0].reshape(8192, 5)
ft2_C2 = data2_C2['ft'][0][0].reshape(8192,1)
fd2_C2 = data2_C2['fd'][0][0].reshape(8192,1)


e2_C3 = data2_C3['e'][0][0].reshape(8192, 5)
u2_C3 = data2_C3['u'][0][0].reshape(8192, 5)
x2_C3 = data2_C3['x'][0][0].reshape(8192, 5)
ft2_C3 = data2_C3['ft'][0][0].reshape(8192,1)
fd2_C3 = data2_C3['fd'][0][0].reshape(8192,1)


e2_C4 = data2_C4['e'][0][0].reshape(8192, 5)
u2_C4 = data2_C4['u'][0][0].reshape(8192, 5)
x2_C4 = data2_C4['x'][0][0].reshape(8192, 5)
ft2_C4 = data2_C4['ft'][0][0].reshape(8192,1)
fd2_C4 = data2_C4['fd'][0][0].reshape(8192,1)


e2_C5 = data2_C5['e'][0][0].reshape(8192, 5)
u2_C5 = data2_C5['u'][0][0].reshape(8192, 5)
x2_C5 = data2_C5['x'][0][0].reshape(8192, 5)
ft2_C5 = data2_C5['ft'][0][0].reshape(8192,1)
fd2_C5 = data2_C5['fd'][0][0].reshape(8192,1)


e2_C6 = data2_C6['e'][0][0].reshape(8192, 5)
u2_C6 = data2_C6['u'][0][0].reshape(8192, 5)
x2_C6 = data2_C6['x'][0][0].reshape(8192, 5)
ft2_C6 = data2_C6['ft'][0][0].reshape(8192,1)
fd2_C6 = data2_C6['fd'][0][0].reshape(8192,1)

#----------------------------------- Subject 3 ----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj3['t'][0]         # Time
data3_C1 = datasubj3['data_C1']      # Data Condition 1
data3_C2 = datasubj3['data_C2']      # Data Condition 2
data3_C3 = datasubj3['data_C3']      # Data Condition 3
data3_C4 = datasubj3['data_C4']      # Data Condition 4
data3_C5 = datasubj3['data_C5']      # Data Condition 5
data3_C6 = datasubj3['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e3_C1       = data3_C1['e'][0][0].reshape(8192, 5)
u3_C1       = data3_C1['u'][0][0].reshape(8192, 5)
x3_C1       = data3_C1['x'][0][0].reshape(8192, 5)
ft3_C1      = data3_C1['ft'][0][0].reshape(8192,1)
fd3_C1      = data3_C1['fd'][0][0].reshape(8192,1)


e3_C2 = data3_C2['e'][0][0].reshape(8192, 5)
u3_C2 = data3_C2['u'][0][0].reshape(8192, 5)
x3_C2 = data3_C2['x'][0][0].reshape(8192, 5)
ft3_C2 = data3_C2['ft'][0][0].reshape(8192,1)
fd3_C2 = data3_C2['fd'][0][0].reshape(8192,1)


e3_C3 = data3_C3['e'][0][0].reshape(8192, 5)
u3_C3 = data3_C3['u'][0][0].reshape(8192, 5)
x3_C3 = data3_C3['x'][0][0].reshape(8192, 5)
ft3_C3 = data3_C3['ft'][0][0].reshape(8192,1)
fd3_C3 = data3_C3['fd'][0][0].reshape(8192,1)


e3_C4 = data3_C4['e'][0][0].reshape(8192, 5)
u3_C4 = data3_C4['u'][0][0].reshape(8192, 5)
x3_C4 = data3_C4['x'][0][0].reshape(8192, 5)
ft3_C4 = data3_C4['ft'][0][0].reshape(8192,1)
fd3_C4 = data3_C4['fd'][0][0].reshape(8192,1)


e3_C5 = data3_C5['e'][0][0].reshape(8192, 5)
u3_C5 = data3_C5['u'][0][0].reshape(8192, 5)
x3_C5 = data3_C5['x'][0][0].reshape(8192, 5)
ft3_C5 = data3_C5['ft'][0][0].reshape(8192,1)
fd3_C5 = data3_C5['fd'][0][0].reshape(8192,1)


e3_C6 = data3_C6['e'][0][0].reshape(8192, 5)
u3_C6 = data3_C6['u'][0][0].reshape(8192, 5)
x3_C6 = data3_C6['x'][0][0].reshape(8192, 5)
ft3_C6 = data3_C6['ft'][0][0].reshape(8192,1)
fd3_C6 = data3_C6['fd'][0][0].reshape(8192,1)

#-----------------------------------Subject 4----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj4['t'][0]         # Time
data4_C1 = datasubj4['data_C1']      # Data Condition 1
data4_C2 = datasubj4['data_C2']      # Data Condition 2
data4_C3 = datasubj4['data_C3']      # Data Condition 3
data4_C4 = datasubj4['data_C4']      # Data Condition 4
data4_C5 = datasubj4['data_C5']      # Data Condition 5
data4_C6 = datasubj4['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e4_C1       = data4_C1['e'][0][0].reshape(8192, 5)
u4_C1       = data4_C1['u'][0][0].reshape(8192, 5)
x4_C1       = data4_C1['x'][0][0].reshape(8192, 5)
ft4_C1      = data4_C1['ft'][0][0].reshape(8192,1)
fd4_C1      = data4_C1['fd'][0][0].reshape(8192,1)


e4_C2 = data4_C2['e'][0][0].reshape(8192, 5)
u4_C2 = data4_C2['u'][0][0].reshape(8192, 5)
x4_C2 = data4_C2['x'][0][0].reshape(8192, 5)
ft4_C2 = data4_C2['ft'][0][0].reshape(8192,1)
fd4_C2 = data4_C2['fd'][0][0].reshape(8192,1)


e4_C3 = data4_C3['e'][0][0].reshape(8192, 5)
u4_C3 = data4_C3['u'][0][0].reshape(8192, 5)
x4_C3 = data4_C3['x'][0][0].reshape(8192, 5)
ft4_C3 = data4_C3['ft'][0][0].reshape(8192,1)
fd4_C3 = data4_C3['fd'][0][0].reshape(8192,1)


e4_C4 = data4_C4['e'][0][0].reshape(8192, 5)
u4_C4 = data4_C4['u'][0][0].reshape(8192, 5)
x4_C4 = data4_C4['x'][0][0].reshape(8192, 5)
ft4_C4 = data4_C4['ft'][0][0].reshape(8192,1)
fd4_C4 = data4_C4['fd'][0][0].reshape(8192,1)


e4_C5 = data4_C5['e'][0][0].reshape(8192, 5)
u4_C5 = data4_C5['u'][0][0].reshape(8192, 5)
x4_C5 = data4_C5['x'][0][0].reshape(8192, 5)
ft4_C5 = data4_C5['ft'][0][0].reshape(8192,1)
fd4_C5 = data4_C5['fd'][0][0].reshape(8192,1)


e4_C6 = data4_C6['e'][0][0].reshape(8192, 5)
u4_C6 = data4_C6['u'][0][0].reshape(8192, 5)
x4_C6 = data4_C6['x'][0][0].reshape(8192, 5)
ft4_C6 = data4_C6['ft'][0][0].reshape(8192,1)
fd4_C6 = data4_C6['fd'][0][0].reshape(8192,1)

#-----------------------------------Subject 5----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj5['t'][0]         # Time
data5_C1 = datasubj5['data_C1']      # Data Condition 1
data5_C2 = datasubj5['data_C2']      # Data Condition 2
data5_C3 = datasubj5['data_C3']      # Data Condition 3
data5_C4 = datasubj5['data_C4']      # Data Condition 4
data5_C5 = datasubj5['data_C5']      # Data Condition 5
data5_C6 = datasubj5['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e5_C1       = data5_C1['e'][0][0].reshape(8192, 5)
u5_C1       = data5_C1['u'][0][0].reshape(8192, 5)
x5_C1       = data5_C1['x'][0][0].reshape(8192, 5)
ft5_C1      = data5_C1['ft'][0][0].reshape(8192,1)
fd5_C1      = data5_C1['fd'][0][0].reshape(8192,1)


e5_C2 = data5_C2['e'][0][0].reshape(8192, 5)
u5_C2 = data5_C2['u'][0][0].reshape(8192, 5)
x5_C2 = data5_C2['x'][0][0].reshape(8192, 5)
ft5_C2 = data5_C2['ft'][0][0].reshape(8192,1)
fd5_C2 = data5_C2['fd'][0][0].reshape(8192,1)


e5_C3 = data5_C3['e'][0][0].reshape(8192, 5)
u5_C3 = data5_C3['u'][0][0].reshape(8192, 5)
x5_C3 = data5_C3['x'][0][0].reshape(8192, 5)
ft5_C3 = data5_C3['ft'][0][0].reshape(8192,1)
fd5_C3 = data5_C3['fd'][0][0].reshape(8192,1)


e5_C4 = data5_C4['e'][0][0].reshape(8192, 5)
u5_C4 = data5_C4['u'][0][0].reshape(8192, 5)
x5_C4 = data5_C4['x'][0][0].reshape(8192, 5)
ft5_C4 = data5_C4['ft'][0][0].reshape(8192,1)
fd5_C4 = data5_C4['fd'][0][0].reshape(8192,1)


e5_C5 = data5_C5['e'][0][0].reshape(8192, 5)
u5_C5 = data5_C5['u'][0][0].reshape(8192, 5)
x5_C5 = data5_C5['x'][0][0].reshape(8192, 5)
ft5_C5 = data5_C5['ft'][0][0].reshape(8192,1)
fd5_C5 = data5_C5['fd'][0][0].reshape(8192,1)


e5_C6 = data5_C6['e'][0][0].reshape(8192, 5)
u5_C6 = data5_C6['u'][0][0].reshape(8192, 5)
x5_C6 = data5_C6['x'][0][0].reshape(8192, 5)
ft5_C6 = data5_C6['ft'][0][0].reshape(8192,1)
fd5_C6 = data5_C6['fd'][0][0].reshape(8192,1)

#-----------------------------------Subject 6----------------------------------------

# ---------------------------------- Variables ---------------------------------
t        = datasubj6['t'][0]         # Time
data6_C1 = datasubj6['data_C1']      # Data Condition 1
data6_C2 = datasubj6['data_C2']      # Data Condition 2
data6_C3 = datasubj6['data_C3']      # Data Condition 3
data6_C4 = datasubj6['data_C4']      # Data Condition 4
data6_C5 = datasubj6['data_C5']      # Data Condition 5
data6_C6 = datasubj6['data_C6']      # Data Condition 6

# Subvariables for each Data Condition
e6_C1       = data6_C1['e'][0][0].reshape(8192, 5)
u6_C1       = data6_C1['u'][0][0].reshape(8192, 5)
x6_C1       = data6_C1['x'][0][0].reshape(8192, 5)
ft6_C1      = data6_C1['ft'][0][0].reshape(8192,1)
fd6_C1      = data6_C1['fd'][0][0].reshape(8192,1)


e6_C2 = data6_C2['e'][0][0].reshape(8192, 5)
u6_C2 = data6_C2['u'][0][0].reshape(8192, 5)
x6_C2 = data6_C2['x'][0][0].reshape(8192, 5)
ft6_C2 = data6_C2['ft'][0][0].reshape(8192,1)
fd6_C2 = data6_C2['fd'][0][0].reshape(8192,1)


e6_C3 = data6_C3['e'][0][0].reshape(8192, 5)
u6_C3 = data6_C3['u'][0][0].reshape(8192, 5)
x6_C3 = data6_C3['x'][0][0].reshape(8192, 5)
ft6_C3 = data6_C3['ft'][0][0].reshape(8192,1)
fd6_C3 = data6_C3['fd'][0][0].reshape(8192,1)


e6_C4 = data6_C4['e'][0][0].reshape(8192, 5)
u6_C4 = data6_C4['u'][0][0].reshape(8192, 5)
x6_C4 = data6_C4['x'][0][0].reshape(8192, 5)
ft6_C4 = data6_C4['ft'][0][0].reshape(8192,1)
fd6_C4 = data6_C4['fd'][0][0].reshape(8192,1)


e6_C5 = data6_C5['e'][0][0].reshape(8192, 5)
u6_C5 = data6_C5['u'][0][0].reshape(8192, 5)
x6_C5 = data6_C5['x'][0][0].reshape(8192, 5)
ft6_C5 = data6_C5['ft'][0][0].reshape(8192,1)
fd6_C5 = data6_C5['fd'][0][0].reshape(8192,1)


e6_C6 = data6_C6['e'][0][0].reshape(8192, 5)
u6_C6 = data6_C6['u'][0][0].reshape(8192, 5)
x6_C6 = data6_C6['x'][0][0].reshape(8192, 5)
ft6_C6 = data6_C6['ft'][0][0].reshape(8192,1)
fd6_C6 = data6_C6['fd'][0][0].reshape(8192,1)

# ---------------------------- RMS and Variance --------------------------------


e1_C1_RMS = RMS_calculate_8192x5(e1_C1)
e1_C1_VAR = VAR_calculate_8192x5(e1_C1)

e1_C1_RMS_overall = RMS_calculate_1x5(e1_C1_RMS)
e1_C1_VAR_overall = VAR_calculate_1x5(e1_C1_VAR)

'''e2_C1_RMS = RMS_calculate_8192x5(e2_C2)
e2_C1_VAR = VAR_calculate_8192x5(e2_C2)

e2_C1_RMS_overall = RMS_calculate_1x5(e2_C1_RMS)
e2_C1_VAR_overall = VAR_calculate_1x5(e2_C1_VAR)

e3_C3_RMS = RMS_calculate_8192x5(e3_C3)
e3_C3_VAR = VAR_calculate_8192x5(e3_C3)

e3_C1_RMS_overall = RMS_calculate_1x5(e3_C3_RMS)
e3_C1_VAR_overall = VAR_calculate_1x5(e3_C3_VAR)

e4_C4_RMS = RMS_calculate_8192x5(e4_C4)
e4_C4_VAR = VAR_calculate_8192x5(e4_C4)

e4_C4_RMS_overall = RMS_calculate_1x5(e4_C4_RMS)
e4_C4_VAR_overall = VAR_calculate_1x5(e4_C4_VAR)

e2_C2_RMS = RMS_calculate_8192x5(e2_C2)
e2_C2_VAR = VAR_calculate_8192x5(e2_C2)

e1_C1_RMS_overall = RMS_calculate_1x5(e1_C1_RMS)
e1_C1_VAR_overall = VAR_calculate_1x5(e1_C1_VAR)

e2_C2_RMS = RMS_calculate_8192x5(e2_C2)
e2_C2_VAR = VAR_calculate_8192x5(e2_C2)

e1_C1_RMS_overall = RMS_calculate_1x5(e1_C1_RMS)
e1_C1_VAR_overall = VAR_calculate_1x5(e1_C1_VAR)

print(e1_C1_RMS)
print(e1_C1_RMS_overall)
print(e1_C1_VAR)
print(e1_C1_VAR_overall)'''

# --------------------------- Maximum and Minimum --------------------------------


e1_C1_max = maximum(e1_C1,t)
e1_C1_min = minimum(e1_C1,t)
print(e1_C1_max,e1_C1_min)
a=[]
b=[]
for i in range (5):
  a.append(e1_C1_max[i][0])
  b.append(e1_C1_max[i][1])
plt.subplot(321)
plt.title("Error signal maximum values")
plt.plot(b,a,'o')

a1=[]
b1=[]
for i in range (5):
  a1.append(e1_C1_min[i][0])
  b1.append(e1_C1_min[i][1])
plt.subplot(322)
plt.title("Error signal minimum values")
plt.plot(b1,a1,'o')  
"""
e1_C2_max = maximum(e1_C2,t)
e1_C2_min = minimum(e1_C2,t)
print(e1_C2_max,e1_C2_min)

e1_C3_max = maximum(e1_C3,t)
e1_C3_min = minimum(e1_C3,t)
print(e1_C3_max,e1_C3_min)

e1_C4_max = maximum(e1_C4,t)
e1_C4_min = minimum(e1_C4,t)
print(e1_C4_max,e1_C4_min)

e1_C5_max = maximum(e1_C5,t)
e1_C5_min = minimum(e1_C5,t)
print(e1_C5_max,e1_C5_min)

e1_C6_max = maximum(e1_C6,t)
e1_C6_min = minimum(e1_C6,t)
print(e1_C6_max,e1_C6_min)
"""
u1_C1_max = maximum(u1_C1,t)
u1_C1_min = minimum(u1_C1,t)
print(u1_C1_max,u1_C1_min)
a2=[]
b2=[]
for i in range (5):
  a2.append(u1_C1_max[i][0])
  b2.append(u1_C1_max[i][1])
plt.subplot(323)
plt.title("Human input maximum values")
plt.plot(b2,a2,'o')

a3=[]
b3=[]
for i in range (5):
  a3.append(e1_C1_min[i][0])
  b3.append(e1_C1_min[i][1])
plt.subplot(324)
plt.title("Human input minimum values")
plt.plot(b3,a3,'o')  
"""
u1_C2_max = maximum(u1_C2,t)
u1_C2_min = minimum(u1_C2,t)
print(u1_C2_max,u1_C2_min)

u1_C3_max = maximum(u1_C3,t)
u1_C3_min = minimum(u1_C3,t)
print(u1_C3_max,u1_C3_min)

u1_C4_max = maximum(u1_C4,t)
u1_C4_min = minimum(u1_C4,t)
print(u1_C4_max,u1_C4_min)

u1_C5_max = maximum(u1_C5,t)
u1_C5_min = minimum(u1_C5,t)
print(u1_C5_max,u1_C5_min)

u1_C6_max = maximum(u1_C6,t)
u1_C6_min = minimum(u1_C6,t)
print(u1_C6_max,u1_C6_min)
"""
x1_C1_max = maximum(x1_C1,t)
x1_C1_min = minimum(x1_C1,t)
print(x1_C1_max,x1_C1_min)
a4=[]
b4=[]
for i in range (5):
  a4.append(x1_C1_max[i][0])
  b4.append(x1_C1_max[i][1])
plt.subplot(325)
plt.title("Pitch input maximum values")
plt.plot(b4,a4,'o')

a5=[]
b5=[]
for i in range (5):
  a5.append(x1_C1_min[i][0])
  b5.append(x1_C1_min[i][1])
plt.subplot(326)
plt.title("Pitch input minimum values")
plt.plot(b5,a5,'o')
plt.show()
"""
x1_C2_max = maximum(x1_C2,t)
x1_C2_min = minimum(x1_C2,t)
print(x1_C2_max,x1_C2_min)

x1_C3_max = maximum(x1_C3,t)
x1_C3_min = minimum(x1_C3,t)
print(x1_C3_max,x1_C3_min)

x1_C4_max = maximum(x1_C4,t)
x1_C4_min = minimum(x1_C4,t)
print(x1_C4_max,x1_C4_min)

x1_C5_max = maximum(x1_C5,t)
x1_C5_min = minimum(x1_C5,t)
print(x1_C5_max,x1_C5_min)

x1_C6_max = maximum(x1_C6,t)
x1_C6_min = minimum(x1_C6,t)
print(x1_C6_max,x1_C6_min)
"""

# --------------------------- Steepest and Maximum Change ----------------------------

e1_C1_change = steepest_change(e1_C1,t)
print(e1_C1_change)
a=[]
b=[]
c=[]
for i in range (5):
  a.append(e1_C1_change[i][0])
  b.append(e1_C1_change[i][1])
  c.append(e1_C1_change[i][2])
plt.subplot(321)
plt.title("Error signal steepest change values")
plt.plot(b,a,'o')
plt.subplot(322)
plt.title("Error signal maximum slope values")
plt.plot(b,c,'o')
"""
e1_C2_change = steepest_change(e1_C2,t)
e1_C3_change = steepest_change(e1_C3,t)
e1_C4_change = steepest_change(e1_C4,t)
e1_C5_change = steepest_change(e1_C5,t)
e1_C6_change = steepest_change(e1_C6,t)
"""
u1_C1_change = steepest_change(u1_C1,t)
print(u1_C1_change)
a1=[]
b1=[]
c1=[]
for i in range (5):
  a1.append(u1_C1_change[i][0])
  b1.append(u1_C1_change[i][1])
  c1.append(u1_C1_change[i][2])
plt.subplot(323)
plt.title("Human input steepest change values")
plt.plot(b1,a1,'o')
plt.subplot(324)
plt.title("Human input maximum slope values")
plt.plot(b1,c1,'o')
"""
u1_C2_change = steepest_change(u1_C2,t)
u1_C3_change = steepest_change(u1_C3,t)
u1_C4_change = steepest_change(u1_C4,t)
u1_C5_change = steepest_change(u1_C5,t)
u1_C6_change = steepest_change(u1_C6,t)
"""
x1_C1_change = steepest_change(x1_C1,t)
print(x1_C1_change)
a2=[]
b2=[]
c2=[]
for i in range (5):
  a2.append(x1_C1_change[i][0])
  b2.append(x1_C1_change[i][1])
  c2.append(x1_C1_change[i][2])
plt.subplot(325)
plt.title("Pitch input steepest change values")
plt.plot(b2,a2,'o')
plt.subplot(326)
plt.title("Pitch input maximum slope values")
plt.plot(b2,c2,'o')
plt.show()
"""
x1_C2_change = steepest_change(x1_C2,t)
x1_C3_change = steepest_change(x1_C3,t)
x1_C4_change = steepest_change(x1_C4,t)
x1_C5_change = steepest_change(x1_C5,t)
x1_C6_change = steepest_change(x1_C6,t)
"""

# ---------------------------- Plot --------------------------------

"""
# Error as a function of time
plt.subplot(231)
plt.plot(t, e1_C1)
plt.title('e; pos. control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(232)
plt.plot(t, e1_C2)
plt.title('e; vel. control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(233)
plt.plot(t, e1_C3)
plt.title('e; acc. control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(234)
plt.plot(t, e1_C4)
plt.title('e; pos. control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(235)
plt.plot(t, e1_C5)
plt.title('e; vel. control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(236)
plt.plot(t, e1_C6)
plt.title('e; acc. control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Human operator control input as a function of time

plt.subplot(231)
plt.plot(t, u1_C1)
plt.title('Human input; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(232)
plt.plot(t, u1_C2)
plt.title('Human input; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(233)
plt.plot(t, u1_C3)
plt.title('Human input; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(234)
plt.plot(t, u1_C4)
plt.title('Human input; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(235)
plt.plot(t, u1_C5)
plt.title('Human input; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(236)
plt.plot(t, u1_C6)
plt.title('Human input; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Pitch input (u) as a function of time

plt.subplot(231)
plt.plot(t, x1_C1)
plt.title('Pitch input; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(232)
plt.plot(t, x1_C2)
plt.title('Pitch input; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(233)
plt.plot(t, x1_C3)
plt.title('Pitch input; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s2]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(234)
plt.plot(t, x1_C4)
plt.title('Pitch input; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(235)
plt.plot(t, x1_C5)
plt.title('Pitch input; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

plt.subplot(236)
plt.plot(t, x1_C6)
plt.title('Pitch input; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s2]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Target forcing function as a function of time

plt.subplot(231)
plt.plot(t,ft1_C1)
plt.title('Target forcing function; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")

plt.subplot(232)
plt.plot(t, ft1_C2)
plt.title('Target forcing function; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")

plt.subplot(233)
plt.plot(t, ft1_C3)
plt.title('Target forcing function; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")

plt.subplot(234)
plt.plot(t, ft1_C4)
plt.title('Target forcing function; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")

plt.subplot(235)
plt.plot(t, ft1_C5)
plt.title('Target forcing function; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")

plt.subplot(236)
plt.plot(t, ft1_C6)
plt.title('Target forcing function; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

# Disturbance forcing function as a function of time

plt.subplot(231)
plt.plot(t,fd1_C1)
plt.title('Disturbance forcing function; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")

plt.subplot(232)
plt.plot(t, fd1_C2)
plt.title('Disturbance forcing function; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")

plt.subplot(233)
plt.plot(t, fd1_C3)
plt.title('Disturbance forcing function; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")

plt.subplot(234)
plt.plot(t, fd1_C4)
plt.title('Disturbance forcing function; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")

plt.subplot(235)
plt.plot(t, fd1_C5)
plt.title('Disturbance forcing function; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")

plt.subplot(236)
plt.plot(t, fd1_C6)
plt.title('Disturbance forcing function; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()
"""
