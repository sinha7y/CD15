
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
from scipy.signal import correlate
#<<<<<<< HEAD
#from statsmodels.stats.weightstats import ttest_ind
#=======
#from statsmodels.stats.weightstats import ttest_ind
#>>>>>>> ac5b7a6feddf200a261bf29207f5e30750184b21


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

  RMS_array = ((np.sum(np.square(input_array)))/5)**.5
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

# RMS calcualtor given a 1 by 6 array
def RMS_calculate_1x6(input_array):

  RMS_array = ((np.sum(np.square(input_array)))/6)**.5
  return RMS_array

# Variance calculator given a 1 by 6 array
def VAR_calculate_1x6(input_array):

  total = 0
  mean = np.sum(input_array)/6
  for element in input_array:
    value = (element-mean)**2
    total = total + value
  Var = total/6

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

"""
# ---------------------------- RMS and Variance for Error "e" --------------------------------
# --- Subject 1 ---
# single runs
e1_C1_RMS = RMS_calculate_8192x5(e1_C1)
e1_C1_VAR = VAR_calculate_8192x5(e1_C1)
e1_C2_RMS = RMS_calculate_8192x5(e1_C2)
e1_C2_VAR = VAR_calculate_8192x5(e1_C2)
e1_C3_RMS = RMS_calculate_8192x5(e1_C3)
e1_C3_VAR = VAR_calculate_8192x5(e1_C3)
e1_C4_RMS = RMS_calculate_8192x5(e1_C4)
e1_C4_VAR = VAR_calculate_8192x5(e1_C4)
e1_C5_RMS = RMS_calculate_8192x5(e1_C5)
e1_C5_VAR = VAR_calculate_8192x5(e1_C5)
e1_C6_RMS = RMS_calculate_8192x5(e1_C6)
e1_C6_VAR = VAR_calculate_8192x5(e1_C6)
# rms and variance over the 5 runs
e1_C1_RMS_overall = RMS_calculate_1x5(e1_C1_RMS)
e1_C1_VAR_overall = VAR_calculate_1x5(e1_C1_VAR)
e1_C2_RMS_overall = RMS_calculate_1x5(e1_C2_RMS)
e1_C2_VAR_overall = VAR_calculate_1x5(e1_C2_VAR)
e1_C3_RMS_overall = RMS_calculate_1x5(e1_C3_RMS)
e1_C3_VAR_overall = VAR_calculate_1x5(e1_C3_VAR)
e1_C4_RMS_overall = RMS_calculate_1x5(e1_C4_RMS)
e1_C4_VAR_overall = VAR_calculate_1x5(e1_C4_VAR)
e1_C5_RMS_overall = RMS_calculate_1x5(e1_C5_RMS)
e1_C5_VAR_overall = VAR_calculate_1x5(e1_C5_VAR)
e1_C6_RMS_overall = RMS_calculate_1x5(e1_C6_RMS)
e1_C6_VAR_overall = VAR_calculate_1x5(e1_C6_VAR)
# --- Subject 2 ---
# single runs
e2_C1_RMS = RMS_calculate_8192x5(e2_C1)
e2_C1_VAR = VAR_calculate_8192x5(e2_C1)
e2_C2_RMS = RMS_calculate_8192x5(e2_C2)
e2_C2_VAR = VAR_calculate_8192x5(e2_C2)
e2_C3_RMS = RMS_calculate_8192x5(e2_C3)
e2_C3_VAR = VAR_calculate_8192x5(e2_C3)
e2_C4_RMS = RMS_calculate_8192x5(e2_C4)
e2_C4_VAR = VAR_calculate_8192x5(e2_C4)
e2_C5_RMS = RMS_calculate_8192x5(e2_C5)
e2_C5_VAR = VAR_calculate_8192x5(e2_C5)
e2_C6_RMS = RMS_calculate_8192x5(e2_C6)
e2_C6_VAR = VAR_calculate_8192x5(e2_C6)
# rms and variance over the 5 runs
e2_C1_RMS_overall = RMS_calculate_1x5(e2_C1_RMS)
e2_C1_VAR_overall = VAR_calculate_1x5(e2_C1_VAR)
e2_C2_RMS_overall = RMS_calculate_1x5(e2_C2_RMS)
e2_C2_VAR_overall = VAR_calculate_1x5(e2_C2_VAR)
e2_C3_RMS_overall = RMS_calculate_1x5(e2_C3_RMS)
e2_C3_VAR_overall = VAR_calculate_1x5(e2_C3_VAR)
e2_C4_RMS_overall = RMS_calculate_1x5(e2_C4_RMS)
e2_C4_VAR_overall = VAR_calculate_1x5(e2_C4_VAR)
e2_C5_RMS_overall = RMS_calculate_1x5(e2_C5_RMS)
e2_C5_VAR_overall = VAR_calculate_1x5(e2_C5_VAR)
e2_C6_RMS_overall = RMS_calculate_1x5(e2_C6_RMS)
e2_C6_VAR_overall = VAR_calculate_1x5(e2_C6_VAR)
# --- Subject 3 ---
# single runs
e3_C1_RMS = RMS_calculate_8192x5(e3_C1)
e3_C1_VAR = VAR_calculate_8192x5(e3_C1)
e3_C2_RMS = RMS_calculate_8192x5(e3_C2)
e3_C2_VAR = VAR_calculate_8192x5(e3_C2)
e3_C3_RMS = RMS_calculate_8192x5(e3_C3)
e3_C3_VAR = VAR_calculate_8192x5(e3_C3)
e3_C4_RMS = RMS_calculate_8192x5(e3_C4)
e3_C4_VAR = VAR_calculate_8192x5(e3_C4)
e3_C5_RMS = RMS_calculate_8192x5(e3_C5)
e3_C5_VAR = VAR_calculate_8192x5(e3_C5)
e3_C6_RMS = RMS_calculate_8192x5(e3_C6)
e3_C6_VAR = VAR_calculate_8192x5(e3_C6)
# rms and variance over the 5 runs
e3_C1_RMS_overall = RMS_calculate_1x5(e3_C1_RMS)
e3_C1_VAR_overall = VAR_calculate_1x5(e3_C1_VAR)
e3_C2_RMS_overall = RMS_calculate_1x5(e3_C2_RMS)
e3_C2_VAR_overall = VAR_calculate_1x5(e3_C2_VAR)
e3_C3_RMS_overall = RMS_calculate_1x5(e3_C3_RMS)
e3_C3_VAR_overall = VAR_calculate_1x5(e3_C3_VAR)
e3_C4_RMS_overall = RMS_calculate_1x5(e3_C4_RMS)
e3_C4_VAR_overall = VAR_calculate_1x5(e3_C4_VAR)
e3_C5_RMS_overall = RMS_calculate_1x5(e3_C5_RMS)
e3_C5_VAR_overall = VAR_calculate_1x5(e3_C5_VAR)
e3_C6_RMS_overall = RMS_calculate_1x5(e3_C6_RMS)
e3_C6_VAR_overall = VAR_calculate_1x5(e3_C6_VAR)
# --- Subject 4 ---
# single runs
e4_C1_RMS = RMS_calculate_8192x5(e4_C1)
e4_C1_VAR = VAR_calculate_8192x5(e4_C1)
e4_C2_RMS = RMS_calculate_8192x5(e4_C2)
e4_C2_VAR = VAR_calculate_8192x5(e4_C2)
e4_C3_RMS = RMS_calculate_8192x5(e4_C3)
e4_C3_VAR = VAR_calculate_8192x5(e4_C3)
e4_C4_RMS = RMS_calculate_8192x5(e4_C4)
e4_C4_VAR = VAR_calculate_8192x5(e4_C4)
e4_C5_RMS = RMS_calculate_8192x5(e4_C5)
e4_C5_VAR = VAR_calculate_8192x5(e4_C5)
e4_C6_RMS = RMS_calculate_8192x5(e4_C6)
e4_C6_VAR = VAR_calculate_8192x5(e4_C6)
# rms and variance over the 5 runs
e4_C1_RMS_overall = RMS_calculate_1x5(e4_C1_RMS)
e4_C1_VAR_overall = VAR_calculate_1x5(e4_C1_VAR)
e4_C2_RMS_overall = RMS_calculate_1x5(e4_C2_RMS)
e4_C2_VAR_overall = VAR_calculate_1x5(e4_C2_VAR)
e4_C3_RMS_overall = RMS_calculate_1x5(e4_C3_RMS)
e4_C3_VAR_overall = VAR_calculate_1x5(e4_C3_VAR)
e4_C4_RMS_overall = RMS_calculate_1x5(e4_C4_RMS)
e4_C4_VAR_overall = VAR_calculate_1x5(e4_C4_VAR)
e4_C5_RMS_overall = RMS_calculate_1x5(e4_C5_RMS)
e4_C5_VAR_overall = VAR_calculate_1x5(e4_C5_VAR)
e4_C6_RMS_overall = RMS_calculate_1x5(e4_C6_RMS)
e4_C6_VAR_overall = VAR_calculate_1x5(e4_C6_VAR)
# --- Subject 5 ---
# single runs
e5_C1_RMS = RMS_calculate_8192x5(e5_C1)
e5_C1_VAR = VAR_calculate_8192x5(e5_C1)
e5_C2_RMS = RMS_calculate_8192x5(e5_C2)
e5_C2_VAR = VAR_calculate_8192x5(e5_C2)
e5_C3_RMS = RMS_calculate_8192x5(e5_C3)
e5_C3_VAR = VAR_calculate_8192x5(e5_C3)
e5_C4_RMS = RMS_calculate_8192x5(e5_C4)
e5_C4_VAR = VAR_calculate_8192x5(e5_C4)
e5_C5_RMS = RMS_calculate_8192x5(e5_C5)
e5_C5_VAR = VAR_calculate_8192x5(e5_C5)
e5_C6_RMS = RMS_calculate_8192x5(e5_C6)
e5_C6_VAR = VAR_calculate_8192x5(e5_C6)
# rms and variance over the 5 runs
e5_C1_RMS_overall = RMS_calculate_1x5(e5_C1_RMS)
e5_C1_VAR_overall = VAR_calculate_1x5(e5_C1_VAR)
e5_C2_RMS_overall = RMS_calculate_1x5(e5_C2_RMS)
e5_C2_VAR_overall = VAR_calculate_1x5(e5_C2_VAR)
e5_C3_RMS_overall = RMS_calculate_1x5(e5_C3_RMS)
e5_C3_VAR_overall = VAR_calculate_1x5(e5_C3_VAR)
e5_C4_RMS_overall = RMS_calculate_1x5(e5_C4_RMS)
e5_C4_VAR_overall = VAR_calculate_1x5(e5_C4_VAR)
e5_C5_RMS_overall = RMS_calculate_1x5(e5_C5_RMS)
e5_C5_VAR_overall = VAR_calculate_1x5(e5_C5_VAR)
e5_C6_RMS_overall = RMS_calculate_1x5(e5_C6_RMS)
e5_C6_VAR_overall = VAR_calculate_1x5(e5_C6_VAR)
# --- Subject 6 ---
# single runs
e6_C1_RMS = RMS_calculate_8192x5(e6_C1)
e6_C1_VAR = VAR_calculate_8192x5(e6_C1)
e6_C2_RMS = RMS_calculate_8192x5(e6_C2)
e6_C2_VAR = VAR_calculate_8192x5(e6_C2)
e6_C3_RMS = RMS_calculate_8192x5(e6_C3)
e6_C3_VAR = VAR_calculate_8192x5(e6_C3)
e6_C4_RMS = RMS_calculate_8192x5(e6_C4)
e6_C4_VAR = VAR_calculate_8192x5(e6_C4)
e6_C5_RMS = RMS_calculate_8192x5(e6_C5)
e6_C5_VAR = VAR_calculate_8192x5(e6_C5)
e6_C6_RMS = RMS_calculate_8192x5(e6_C6)
e6_C6_VAR = VAR_calculate_8192x5(e6_C6)
# rms and variance over the 5 runs
e6_C1_RMS_overall = RMS_calculate_1x5(e6_C1_RMS)
e6_C1_VAR_overall = VAR_calculate_1x5(e6_C1_VAR)
e6_C2_RMS_overall = RMS_calculate_1x5(e6_C2_RMS)
e6_C2_VAR_overall = VAR_calculate_1x5(e6_C2_VAR)
e6_C3_RMS_overall = RMS_calculate_1x5(e6_C3_RMS)
e6_C3_VAR_overall = VAR_calculate_1x5(e6_C3_VAR)
e6_C4_RMS_overall = RMS_calculate_1x5(e6_C4_RMS)
e6_C4_VAR_overall = VAR_calculate_1x5(e6_C4_VAR)
e6_C5_RMS_overall = RMS_calculate_1x5(e6_C5_RMS)
e6_C5_VAR_overall = VAR_calculate_1x5(e6_C5_VAR)
e6_C6_RMS_overall = RMS_calculate_1x5(e6_C6_RMS)
e6_C6_VAR_overall = VAR_calculate_1x5(e6_C6_VAR)
# --- Rms and var across the different subjects ---
# C1
overall_array_e_C1_RMS = [e1_C1_RMS_overall, e2_C1_RMS_overall, e3_C1_RMS_overall, e4_C1_RMS_overall, e5_C1_RMS_overall, e6_C1_RMS_overall]
e_C1_RMS = RMS_calculate_1x6(overall_array_e_C1_RMS)
overall_array_e_C1_VAR = [e1_C1_VAR_overall, e2_C1_VAR_overall, e3_C1_VAR_overall, e4_C1_VAR_overall, e5_C1_VAR_overall, e6_C1_VAR_overall]
e_C1_VAR = VAR_calculate_1x6(overall_array_e_C1_VAR)
# C2
overall_array_e_C2_RMS = [e1_C2_RMS_overall, e2_C2_RMS_overall, e3_C2_RMS_overall, e4_C2_RMS_overall, e5_C2_RMS_overall, e6_C2_RMS_overall]
e_C2_RMS = RMS_calculate_1x6(overall_array_e_C2_RMS)
overall_array_e_C2_VAR = [e1_C2_VAR_overall, e2_C2_VAR_overall, e3_C2_VAR_overall, e4_C2_VAR_overall, e5_C2_VAR_overall, e6_C2_VAR_overall]
e_C2_VAR = VAR_calculate_1x6(overall_array_e_C2_VAR)
# C3
overall_array_e_C3_RMS = [e1_C3_RMS_overall, e2_C3_RMS_overall, e3_C3_RMS_overall, e4_C3_RMS_overall, e5_C3_RMS_overall, e6_C3_RMS_overall]
e_C3_RMS = RMS_calculate_1x6(overall_array_e_C3_RMS)
overall_array_e_C3_VAR = [e1_C3_VAR_overall, e2_C3_VAR_overall, e3_C3_VAR_overall, e4_C3_VAR_overall, e5_C3_VAR_overall, e6_C3_VAR_overall]
e_C3_VAR = VAR_calculate_1x6(overall_array_e_C3_VAR)
# C4
overall_array_e_C4_RMS = [e1_C4_RMS_overall, e2_C4_RMS_overall, e3_C4_RMS_overall, e4_C4_RMS_overall, e5_C4_RMS_overall, e6_C4_RMS_overall]
e_C4_RMS = RMS_calculate_1x6(overall_array_e_C4_RMS)
overall_array_e_C4_VAR = [e1_C4_VAR_overall, e2_C4_VAR_overall, e3_C4_VAR_overall, e4_C4_VAR_overall, e5_C4_VAR_overall, e6_C4_VAR_overall]
e_C4_VAR = VAR_calculate_1x6(overall_array_e_C4_VAR)
# C5
overall_array_e_C5_RMS = [e1_C5_RMS_overall, e2_C5_RMS_overall, e3_C5_RMS_overall, e4_C5_RMS_overall, e5_C5_RMS_overall, e6_C5_RMS_overall]
e_C5_RMS = RMS_calculate_1x6(overall_array_e_C5_RMS)
overall_array_e_C5_VAR = [e1_C5_VAR_overall, e2_C5_VAR_overall, e3_C5_VAR_overall, e4_C5_VAR_overall, e5_C5_VAR_overall, e6_C5_VAR_overall]
e_C5_VAR = VAR_calculate_1x6(overall_array_e_C5_VAR)
# C6
overall_array_e_C6_RMS = [e1_C6_RMS_overall, e2_C6_RMS_overall, e3_C6_RMS_overall, e4_C6_RMS_overall, e5_C6_RMS_overall, e6_C6_RMS_overall]
e_C6_RMS = RMS_calculate_1x6(overall_array_e_C6_RMS)
overall_array_e_C6_VAR = [e1_C6_VAR_overall, e2_C6_VAR_overall, e3_C6_VAR_overall, e4_C6_VAR_overall, e5_C6_VAR_overall, e6_C6_VAR_overall]
e_C6_VAR = VAR_calculate_1x6(overall_array_e_C6_VAR)
print("RMS of error in scenario 1 is:",e_C1_RMS,"VAR is:", e_C1_VAR)
print("RMS of error in scenario 2 is:",e_C2_RMS,"VAR is:", e_C2_VAR)
print("RMS of error in scenario 3 is:",e_C3_RMS,"VAR is:", e_C3_VAR)
print("RMS of error in scenario 4 is:",e_C4_RMS,"VAR is:", e_C4_VAR)
print("RMS of error in scenario 5 is:",e_C5_RMS,"VAR is:", e_C5_VAR)
print("RMS of error in scenario 6 is:",e_C6_RMS,"VAR is:", e_C6_VAR)
# ---------------------------- RMS and Variance for Human Input "u" --------------------------------
# --- Subject 1 ---
# single runs
u1_C1_RMS = RMS_calculate_8192x5(u1_C1)
u1_C1_VAR = VAR_calculate_8192x5(u1_C1)
u1_C2_RMS = RMS_calculate_8192x5(u1_C2)
u1_C2_VAR = VAR_calculate_8192x5(u1_C2)
u1_C3_RMS = RMS_calculate_8192x5(u1_C3)
u1_C3_VAR = VAR_calculate_8192x5(u1_C3)
u1_C4_RMS = RMS_calculate_8192x5(u1_C4)
u1_C4_VAR = VAR_calculate_8192x5(u1_C4)
u1_C5_RMS = RMS_calculate_8192x5(u1_C5)
u1_C5_VAR = VAR_calculate_8192x5(u1_C5)
u1_C6_RMS = RMS_calculate_8192x5(u1_C6)
u1_C6_VAR = VAR_calculate_8192x5(u1_C6)
# rms and variance over the 5 runs
u1_C1_RMS_overall = RMS_calculate_1x5(u1_C1_RMS)
u1_C1_VAR_overall = VAR_calculate_1x5(u1_C1_VAR)
u1_C2_RMS_overall = RMS_calculate_1x5(u1_C2_RMS)
u1_C2_VAR_overall = VAR_calculate_1x5(u1_C2_VAR)
u1_C3_RMS_overall = RMS_calculate_1x5(u1_C3_RMS)
u1_C3_VAR_overall = VAR_calculate_1x5(u1_C3_VAR)
u1_C4_RMS_overall = RMS_calculate_1x5(u1_C4_RMS)
u1_C4_VAR_overall = VAR_calculate_1x5(u1_C4_VAR)
u1_C5_RMS_overall = RMS_calculate_1x5(u1_C5_RMS)
u1_C5_VAR_overall = VAR_calculate_1x5(u1_C5_VAR)
u1_C6_RMS_overall = RMS_calculate_1x5(u1_C6_RMS)
u1_C6_VAR_overall = VAR_calculate_1x5(u1_C6_VAR)
# --- Subject 2 ---
# single runs
u2_C1_RMS = RMS_calculate_8192x5(u2_C1)
u2_C1_VAR = VAR_calculate_8192x5(u2_C1)
u2_C2_RMS = RMS_calculate_8192x5(u2_C2)
u2_C2_VAR = VAR_calculate_8192x5(u2_C2)
u2_C3_RMS = RMS_calculate_8192x5(u2_C3)
u2_C3_VAR = VAR_calculate_8192x5(u2_C3)
u2_C4_RMS = RMS_calculate_8192x5(u2_C4)
u2_C4_VAR = VAR_calculate_8192x5(u2_C4)
u2_C5_RMS = RMS_calculate_8192x5(u2_C5)
u2_C5_VAR = VAR_calculate_8192x5(u2_C5)
u2_C6_RMS = RMS_calculate_8192x5(u2_C6)
u2_C6_VAR = VAR_calculate_8192x5(u2_C6)
# rms and variance over the 5 runs
u2_C1_RMS_overall = RMS_calculate_1x5(u2_C1_RMS)
u2_C1_VAR_overall = VAR_calculate_1x5(u2_C1_VAR)
u2_C2_RMS_overall = RMS_calculate_1x5(u2_C2_RMS)
u2_C2_VAR_overall = VAR_calculate_1x5(u2_C2_VAR)
u2_C3_RMS_overall = RMS_calculate_1x5(u2_C3_RMS)
u2_C3_VAR_overall = VAR_calculate_1x5(u2_C3_VAR)
u2_C4_RMS_overall = RMS_calculate_1x5(u2_C4_RMS)
u2_C4_VAR_overall = VAR_calculate_1x5(u2_C4_VAR)
u2_C5_RMS_overall = RMS_calculate_1x5(u2_C5_RMS)
u2_C5_VAR_overall = VAR_calculate_1x5(u2_C5_VAR)
u2_C6_RMS_overall = RMS_calculate_1x5(u2_C6_RMS)
u2_C6_VAR_overall = VAR_calculate_1x5(u2_C6_VAR)
# --- Subject 3 ---
# single runs
u3_C1_RMS = RMS_calculate_8192x5(u3_C1)
u3_C1_VAR = VAR_calculate_8192x5(u3_C1)
u3_C2_RMS = RMS_calculate_8192x5(u3_C2)
u3_C2_VAR = VAR_calculate_8192x5(u3_C2)
u3_C3_RMS = RMS_calculate_8192x5(u3_C3)
u3_C3_VAR = VAR_calculate_8192x5(u3_C3)
u3_C4_RMS = RMS_calculate_8192x5(u3_C4)
u3_C4_VAR = VAR_calculate_8192x5(u3_C4)
u3_C5_RMS = RMS_calculate_8192x5(u3_C5)
u3_C5_VAR = VAR_calculate_8192x5(u3_C5)
u3_C6_RMS = RMS_calculate_8192x5(u3_C6)
u3_C6_VAR = VAR_calculate_8192x5(u3_C6)
# rms and variance over the 5 runs
u3_C1_RMS_overall = RMS_calculate_1x5(u3_C1_RMS)
u3_C1_VAR_overall = VAR_calculate_1x5(u3_C1_VAR)
u3_C2_RMS_overall = RMS_calculate_1x5(u3_C2_RMS)
u3_C2_VAR_overall = VAR_calculate_1x5(u3_C2_VAR)
u3_C3_RMS_overall = RMS_calculate_1x5(u3_C3_RMS)
u3_C3_VAR_overall = VAR_calculate_1x5(u3_C3_VAR)
u3_C4_RMS_overall = RMS_calculate_1x5(u3_C4_RMS)
u3_C4_VAR_overall = VAR_calculate_1x5(u3_C4_VAR)
u3_C5_RMS_overall = RMS_calculate_1x5(u3_C5_RMS)
u3_C5_VAR_overall = VAR_calculate_1x5(u3_C5_VAR)
u3_C6_RMS_overall = RMS_calculate_1x5(u3_C6_RMS)
u3_C6_VAR_overall = VAR_calculate_1x5(u3_C6_VAR)
# --- Subject 4 ---
# single runs
u4_C1_RMS = RMS_calculate_8192x5(u4_C1)
u4_C1_VAR = VAR_calculate_8192x5(u4_C1)
u4_C2_RMS = RMS_calculate_8192x5(u4_C2)
u4_C2_VAR = VAR_calculate_8192x5(u4_C2)
u4_C3_RMS = RMS_calculate_8192x5(u4_C3)
u4_C3_VAR = VAR_calculate_8192x5(u4_C3)
u4_C4_RMS = RMS_calculate_8192x5(u4_C4)
u4_C4_VAR = VAR_calculate_8192x5(u4_C4)
u4_C5_RMS = RMS_calculate_8192x5(u4_C5)
u4_C5_VAR = VAR_calculate_8192x5(u4_C5)
u4_C6_RMS = RMS_calculate_8192x5(u4_C6)
u4_C6_VAR = VAR_calculate_8192x5(u4_C6)
# rms and variance over the 5 runs
u4_C1_RMS_overall = RMS_calculate_1x5(u4_C1_RMS)
u4_C1_VAR_overall = VAR_calculate_1x5(u4_C1_VAR)
u4_C2_RMS_overall = RMS_calculate_1x5(u4_C2_RMS)
u4_C2_VAR_overall = VAR_calculate_1x5(u4_C2_VAR)
u4_C3_RMS_overall = RMS_calculate_1x5(u4_C3_RMS)
u4_C3_VAR_overall = VAR_calculate_1x5(u4_C3_VAR)
u4_C4_RMS_overall = RMS_calculate_1x5(u4_C4_RMS)
u4_C4_VAR_overall = VAR_calculate_1x5(u4_C4_VAR)
u4_C5_RMS_overall = RMS_calculate_1x5(u4_C5_RMS)
u4_C5_VAR_overall = VAR_calculate_1x5(u4_C5_VAR)
u4_C6_RMS_overall = RMS_calculate_1x5(u4_C6_RMS)
u4_C6_VAR_overall = VAR_calculate_1x5(u4_C6_VAR)
# --- Subject 5 ---
# single runs
u5_C1_RMS = RMS_calculate_8192x5(u5_C1)
u5_C1_VAR = VAR_calculate_8192x5(u5_C1)
u5_C2_RMS = RMS_calculate_8192x5(u5_C2)
u5_C2_VAR = VAR_calculate_8192x5(u5_C2)
u5_C3_RMS = RMS_calculate_8192x5(u5_C3)
u5_C3_VAR = VAR_calculate_8192x5(u5_C3)
u5_C4_RMS = RMS_calculate_8192x5(u5_C4)
u5_C4_VAR = VAR_calculate_8192x5(u5_C4)
u5_C5_RMS = RMS_calculate_8192x5(u5_C5)
u5_C5_VAR = VAR_calculate_8192x5(u5_C5)
u5_C6_RMS = RMS_calculate_8192x5(u5_C6)
u5_C6_VAR = VAR_calculate_8192x5(u5_C6)
# rms and variance over the 5 runs
u5_C1_RMS_overall = RMS_calculate_1x5(u5_C1_RMS)
u5_C1_VAR_overall = VAR_calculate_1x5(u5_C1_VAR)
u5_C2_RMS_overall = RMS_calculate_1x5(u5_C2_RMS)
u5_C2_VAR_overall = VAR_calculate_1x5(u5_C2_VAR)
u5_C3_RMS_overall = RMS_calculate_1x5(u5_C3_RMS)
u5_C3_VAR_overall = VAR_calculate_1x5(u5_C3_VAR)
u5_C4_RMS_overall = RMS_calculate_1x5(u5_C4_RMS)
u5_C4_VAR_overall = VAR_calculate_1x5(u5_C4_VAR)
u5_C5_RMS_overall = RMS_calculate_1x5(u5_C5_RMS)
u5_C5_VAR_overall = VAR_calculate_1x5(u5_C5_VAR)
u5_C6_RMS_overall = RMS_calculate_1x5(u5_C6_RMS)
u5_C6_VAR_overall = VAR_calculate_1x5(u5_C6_VAR)
# --- Subject 6 ---
# single runs
u6_C1_RMS = RMS_calculate_8192x5(u6_C1)
u6_C1_VAR = VAR_calculate_8192x5(u6_C1)
u6_C2_RMS = RMS_calculate_8192x5(u6_C2)
u6_C2_VAR = VAR_calculate_8192x5(u6_C2)
u6_C3_RMS = RMS_calculate_8192x5(u6_C3)
u6_C3_VAR = VAR_calculate_8192x5(u6_C3)
u6_C4_RMS = RMS_calculate_8192x5(u6_C4)
u6_C4_VAR = VAR_calculate_8192x5(u6_C4)
u6_C5_RMS = RMS_calculate_8192x5(u6_C5)
u6_C5_VAR = VAR_calculate_8192x5(u6_C5)
u6_C6_RMS = RMS_calculate_8192x5(u6_C6)
u6_C6_VAR = VAR_calculate_8192x5(u6_C6)
# rms and variance over the 5 runs
u6_C1_RMS_overall = RMS_calculate_1x5(u6_C1_RMS)
u6_C1_VAR_overall = VAR_calculate_1x5(u6_C1_VAR)
u6_C2_RMS_overall = RMS_calculate_1x5(u6_C2_RMS)
u6_C2_VAR_overall = VAR_calculate_1x5(u6_C2_VAR)
u6_C3_RMS_overall = RMS_calculate_1x5(u6_C3_RMS)
u6_C3_VAR_overall = VAR_calculate_1x5(u6_C3_VAR)
u6_C4_RMS_overall = RMS_calculate_1x5(u6_C4_RMS)
u6_C4_VAR_overall = VAR_calculate_1x5(u6_C4_VAR)
u6_C5_RMS_overall = RMS_calculate_1x5(u6_C5_RMS)
u6_C5_VAR_overall = VAR_calculate_1x5(u6_C5_VAR)
u6_C6_RMS_overall = RMS_calculate_1x5(u6_C6_RMS)
u6_C6_VAR_overall = VAR_calculate_1x5(u6_C6_VAR)
# --- Rms and var across the different subjects ---
# C1
overall_array_u_C1_RMS = [u1_C1_RMS_overall, u2_C1_RMS_overall, u3_C1_RMS_overall, u4_C1_RMS_overall, u5_C1_RMS_overall, u6_C1_RMS_overall]
u_C1_RMS = RMS_calculate_1x6(overall_array_u_C1_RMS)
overall_array_u_C1_VAR = [u1_C1_VAR_overall, u2_C1_VAR_overall, u3_C1_VAR_overall, u4_C1_VAR_overall, u5_C1_VAR_overall, u6_C1_VAR_overall]
u_C1_VAR = VAR_calculate_1x6(overall_array_u_C1_VAR)
# C2
overall_array_u_C2_RMS = [u1_C2_RMS_overall, u2_C2_RMS_overall, u3_C2_RMS_overall, u4_C2_RMS_overall, u5_C2_RMS_overall, u6_C2_RMS_overall]
u_C2_RMS = RMS_calculate_1x6(overall_array_u_C2_RMS)
overall_array_u_C2_VAR = [u1_C2_VAR_overall, u2_C2_VAR_overall, u3_C2_VAR_overall, u4_C2_VAR_overall, u5_C2_VAR_overall, u6_C2_VAR_overall]
u_C2_VAR = VAR_calculate_1x6(overall_array_u_C2_VAR)
# C3
overall_array_u_C3_RMS = [u1_C3_RMS_overall, u2_C3_RMS_overall, u3_C3_RMS_overall, u4_C3_RMS_overall, u5_C3_RMS_overall, u6_C3_RMS_overall]
u_C3_RMS = RMS_calculate_1x6(overall_array_u_C3_RMS)
overall_array_u_C3_VAR = [u1_C3_VAR_overall, u2_C3_VAR_overall, u3_C3_VAR_overall, u4_C3_VAR_overall, u5_C3_VAR_overall, u6_C3_VAR_overall]
u_C3_VAR = VAR_calculate_1x6(overall_array_u_C3_VAR)
# C4
overall_array_u_C4_RMS = [u1_C4_RMS_overall, u2_C4_RMS_overall, u3_C4_RMS_overall, u4_C4_RMS_overall, u5_C4_RMS_overall, u6_C4_RMS_overall]
u_C4_RMS = RMS_calculate_1x6(overall_array_u_C4_RMS)
overall_array_u_C4_VAR = [u1_C4_VAR_overall, u2_C4_VAR_overall, u3_C4_VAR_overall, u4_C4_VAR_overall, u5_C4_VAR_overall, u6_C4_VAR_overall]
u_C4_VAR = VAR_calculate_1x6(overall_array_u_C4_VAR)
# C5
overall_array_u_C5_RMS = [u1_C5_RMS_overall, u2_C5_RMS_overall, u3_C5_RMS_overall, u4_C5_RMS_overall, u5_C5_RMS_overall, u6_C5_RMS_overall]
u_C5_RMS = RMS_calculate_1x6(overall_array_u_C5_RMS)
overall_array_u_C5_VAR = [u1_C5_VAR_overall, u2_C5_VAR_overall, u3_C5_VAR_overall, u4_C5_VAR_overall, u5_C5_VAR_overall, u6_C5_VAR_overall]
u_C5_VAR = VAR_calculate_1x6(overall_array_u_C5_VAR)
# C6
overall_array_u_C6_RMS = [u1_C6_RMS_overall, u2_C6_RMS_overall, u3_C6_RMS_overall, u4_C6_RMS_overall, u5_C6_RMS_overall, u6_C6_RMS_overall]
u_C6_RMS = RMS_calculate_1x6(overall_array_u_C6_RMS)
overall_array_u_C6_VAR = [u1_C6_VAR_overall, u2_C6_VAR_overall, u3_C6_VAR_overall, u4_C6_VAR_overall, u5_C6_VAR_overall, u6_C6_VAR_overall]
u_C6_VAR = VAR_calculate_1x6(overall_array_u_C6_VAR)
print("RMS of human input in scenario 1 is:",u_C1_RMS,"VAR is:", u_C1_VAR)
print("RMS of human input in scenario 2 is:",u_C2_RMS,"VAR is:", u_C2_VAR)
print("RMS of human input in scenario 3 is:",u_C3_RMS,"VAR is:", u_C3_VAR)
print("RMS of human input in scenario 4 is:",u_C4_RMS,"VAR is:", u_C4_VAR)
print("RMS of human input in scenario 5 is:",u_C5_RMS,"VAR is:", u_C5_VAR)
print("RMS of human input in scenario 6 is:",u_C6_RMS,"VAR is:", u_C6_VAR)
# ---------------------------- RMS and Variance for Vehicle Output "x" --------------------------------
# --- Subject 1 ---
# single runs
x1_C1_RMS = RMS_calculate_8192x5(x1_C1)
x1_C1_VAR = VAR_calculate_8192x5(x1_C1)
x1_C2_RMS = RMS_calculate_8192x5(x1_C2)
x1_C2_VAR = VAR_calculate_8192x5(x1_C2)
x1_C3_RMS = RMS_calculate_8192x5(x1_C3)
x1_C3_VAR = VAR_calculate_8192x5(x1_C3)
x1_C4_RMS = RMS_calculate_8192x5(x1_C4)
x1_C4_VAR = VAR_calculate_8192x5(x1_C4)
x1_C5_RMS = RMS_calculate_8192x5(x1_C5)
x1_C5_VAR = VAR_calculate_8192x5(x1_C5)
x1_C6_RMS = RMS_calculate_8192x5(x1_C6)
x1_C6_VAR = VAR_calculate_8192x5(x1_C6)
# rms and variance over the 5 runs
x1_C1_RMS_overall = RMS_calculate_1x5(x1_C1_RMS)
x1_C1_VAR_overall = VAR_calculate_1x5(x1_C1_VAR)
x1_C2_RMS_overall = RMS_calculate_1x5(x1_C2_RMS)
x1_C2_VAR_overall = VAR_calculate_1x5(x1_C2_VAR)
x1_C3_RMS_overall = RMS_calculate_1x5(x1_C3_RMS)
x1_C3_VAR_overall = VAR_calculate_1x5(x1_C3_VAR)
x1_C4_RMS_overall = RMS_calculate_1x5(x1_C4_RMS)
x1_C4_VAR_overall = VAR_calculate_1x5(x1_C4_VAR)
x1_C5_RMS_overall = RMS_calculate_1x5(x1_C5_RMS)
x1_C5_VAR_overall = VAR_calculate_1x5(x1_C5_VAR)
x1_C6_RMS_overall = RMS_calculate_1x5(x1_C6_RMS)
x1_C6_VAR_overall = VAR_calculate_1x5(x1_C6_VAR)
# --- Subject 2 ---
# single runs
x2_C1_RMS = RMS_calculate_8192x5(x2_C1)
x2_C1_VAR = VAR_calculate_8192x5(x2_C1)
x2_C2_RMS = RMS_calculate_8192x5(x2_C2)
x2_C2_VAR = VAR_calculate_8192x5(x2_C2)
x2_C3_RMS = RMS_calculate_8192x5(x2_C3)
x2_C3_VAR = VAR_calculate_8192x5(x2_C3)
x2_C4_RMS = RMS_calculate_8192x5(x2_C4)
x2_C4_VAR = VAR_calculate_8192x5(x2_C4)
x2_C5_RMS = RMS_calculate_8192x5(x2_C5)
x2_C5_VAR = VAR_calculate_8192x5(x2_C5)
x2_C6_RMS = RMS_calculate_8192x5(x2_C6)
x2_C6_VAR = VAR_calculate_8192x5(x2_C6)
# rms and variance over the 5 runs
x2_C1_RMS_overall = RMS_calculate_1x5(x2_C1_RMS)
x2_C1_VAR_overall = VAR_calculate_1x5(x2_C1_VAR)
x2_C2_RMS_overall = RMS_calculate_1x5(x2_C2_RMS)
x2_C2_VAR_overall = VAR_calculate_1x5(x2_C2_VAR)
x2_C3_RMS_overall = RMS_calculate_1x5(x2_C3_RMS)
x2_C3_VAR_overall = VAR_calculate_1x5(x2_C3_VAR)
x2_C4_RMS_overall = RMS_calculate_1x5(x2_C4_RMS)
x2_C4_VAR_overall = VAR_calculate_1x5(x2_C4_VAR)
x2_C5_RMS_overall = RMS_calculate_1x5(x2_C5_RMS)
x2_C5_VAR_overall = VAR_calculate_1x5(x2_C5_VAR)
x2_C6_RMS_overall = RMS_calculate_1x5(x2_C6_RMS)
x2_C6_VAR_overall = VAR_calculate_1x5(x2_C6_VAR)
# --- Subject 3 ---
# single runs
x3_C1_RMS = RMS_calculate_8192x5(x3_C1)
x3_C1_VAR = VAR_calculate_8192x5(x3_C1)
x3_C2_RMS = RMS_calculate_8192x5(x3_C2)
x3_C2_VAR = VAR_calculate_8192x5(x3_C2)
x3_C3_RMS = RMS_calculate_8192x5(x3_C3)
x3_C3_VAR = VAR_calculate_8192x5(x3_C3)
x3_C4_RMS = RMS_calculate_8192x5(x3_C4)
x3_C4_VAR = VAR_calculate_8192x5(x3_C4)
x3_C5_RMS = RMS_calculate_8192x5(x3_C5)
x3_C5_VAR = VAR_calculate_8192x5(x3_C5)
x3_C6_RMS = RMS_calculate_8192x5(x3_C6)
x3_C6_VAR = VAR_calculate_8192x5(x3_C6)
# rms and variance over the 5 runs
x3_C1_RMS_overall = RMS_calculate_1x5(x3_C1_RMS)
x3_C1_VAR_overall = VAR_calculate_1x5(x3_C1_VAR)
x3_C2_RMS_overall = RMS_calculate_1x5(x3_C2_RMS)
x3_C2_VAR_overall = VAR_calculate_1x5(x3_C2_VAR)
x3_C3_RMS_overall = RMS_calculate_1x5(x3_C3_RMS)
x3_C3_VAR_overall = VAR_calculate_1x5(x3_C3_VAR)
x3_C4_RMS_overall = RMS_calculate_1x5(x3_C4_RMS)
x3_C4_VAR_overall = VAR_calculate_1x5(x3_C4_VAR)
x3_C5_RMS_overall = RMS_calculate_1x5(x3_C5_RMS)
x3_C5_VAR_overall = VAR_calculate_1x5(x3_C5_VAR)
x3_C6_RMS_overall = RMS_calculate_1x5(x3_C6_RMS)
x3_C6_VAR_overall = VAR_calculate_1x5(x3_C6_VAR)
# --- Subject 4 ---
# single runs
x4_C1_RMS = RMS_calculate_8192x5(x4_C1)
x4_C1_VAR = VAR_calculate_8192x5(x4_C1)
x4_C2_RMS = RMS_calculate_8192x5(x4_C2)
x4_C2_VAR = VAR_calculate_8192x5(x4_C2)
x4_C3_RMS = RMS_calculate_8192x5(x4_C3)
x4_C3_VAR = VAR_calculate_8192x5(x4_C3)
x4_C4_RMS = RMS_calculate_8192x5(x4_C4)
x4_C4_VAR = VAR_calculate_8192x5(x4_C4)
x4_C5_RMS = RMS_calculate_8192x5(x4_C5)
x4_C5_VAR = VAR_calculate_8192x5(x4_C5)
x4_C6_RMS = RMS_calculate_8192x5(x4_C6)
x4_C6_VAR = VAR_calculate_8192x5(x4_C6)
# rms and variance over the 5 runs
x4_C1_RMS_overall = RMS_calculate_1x5(x4_C1_RMS)
x4_C1_VAR_overall = VAR_calculate_1x5(x4_C1_VAR)
x4_C2_RMS_overall = RMS_calculate_1x5(x4_C2_RMS)
x4_C2_VAR_overall = VAR_calculate_1x5(x4_C2_VAR)
x4_C3_RMS_overall = RMS_calculate_1x5(x4_C3_RMS)
x4_C3_VAR_overall = VAR_calculate_1x5(x4_C3_VAR)
x4_C4_RMS_overall = RMS_calculate_1x5(x4_C4_RMS)
x4_C4_VAR_overall = VAR_calculate_1x5(x4_C4_VAR)
x4_C5_RMS_overall = RMS_calculate_1x5(x4_C5_RMS)
x4_C5_VAR_overall = VAR_calculate_1x5(x4_C5_VAR)
x4_C6_RMS_overall = RMS_calculate_1x5(x4_C6_RMS)
x4_C6_VAR_overall = VAR_calculate_1x5(x4_C6_VAR)
# --- Subject 5 ---
# single runs
x5_C1_RMS = RMS_calculate_8192x5(x5_C1)
x5_C1_VAR = VAR_calculate_8192x5(x5_C1)
x5_C2_RMS = RMS_calculate_8192x5(x5_C2)
x5_C2_VAR = VAR_calculate_8192x5(x5_C2)
x5_C3_RMS = RMS_calculate_8192x5(x5_C3)
x5_C3_VAR = VAR_calculate_8192x5(x5_C3)
x5_C4_RMS = RMS_calculate_8192x5(x5_C4)
x5_C4_VAR = VAR_calculate_8192x5(x5_C4)
x5_C5_RMS = RMS_calculate_8192x5(x5_C5)
x5_C5_VAR = VAR_calculate_8192x5(x5_C5)
x5_C6_RMS = RMS_calculate_8192x5(x5_C6)
x5_C6_VAR = VAR_calculate_8192x5(x5_C6)
# rms and variance over the 5 runs
x5_C1_RMS_overall = RMS_calculate_1x5(x5_C1_RMS)
x5_C1_VAR_overall = VAR_calculate_1x5(x5_C1_VAR)
x5_C2_RMS_overall = RMS_calculate_1x5(x5_C2_RMS)
x5_C2_VAR_overall = VAR_calculate_1x5(x5_C2_VAR)
x5_C3_RMS_overall = RMS_calculate_1x5(x5_C3_RMS)
x5_C3_VAR_overall = VAR_calculate_1x5(x5_C3_VAR)
x5_C4_RMS_overall = RMS_calculate_1x5(x5_C4_RMS)
x5_C4_VAR_overall = VAR_calculate_1x5(x5_C4_VAR)
x5_C5_RMS_overall = RMS_calculate_1x5(x5_C5_RMS)
x5_C5_VAR_overall = VAR_calculate_1x5(x5_C5_VAR)
x5_C6_RMS_overall = RMS_calculate_1x5(x5_C6_RMS)
x5_C6_VAR_overall = VAR_calculate_1x5(x5_C6_VAR)
# --- Subject 6 ---
# single runs
x6_C1_RMS = RMS_calculate_8192x5(x6_C1)
x6_C1_VAR = VAR_calculate_8192x5(x6_C1)
x6_C2_RMS = RMS_calculate_8192x5(x6_C2)
x6_C2_VAR = VAR_calculate_8192x5(x6_C2)
x6_C3_RMS = RMS_calculate_8192x5(x6_C3)
x6_C3_VAR = VAR_calculate_8192x5(x6_C3)
x6_C4_RMS = RMS_calculate_8192x5(x6_C4)
x6_C4_VAR = VAR_calculate_8192x5(x6_C4)
x6_C5_RMS = RMS_calculate_8192x5(x6_C5)
x6_C5_VAR = VAR_calculate_8192x5(x6_C5)
x6_C6_RMS = RMS_calculate_8192x5(x6_C6)
x6_C6_VAR = VAR_calculate_8192x5(x6_C6)
# rms and variance over the 5 runs
x6_C1_RMS_overall = RMS_calculate_1x5(x6_C1_RMS)
x6_C1_VAR_overall = VAR_calculate_1x5(x6_C1_VAR)
x6_C2_RMS_overall = RMS_calculate_1x5(x6_C2_RMS)
x6_C2_VAR_overall = VAR_calculate_1x5(x6_C2_VAR)
x6_C3_RMS_overall = RMS_calculate_1x5(x6_C3_RMS)
x6_C3_VAR_overall = VAR_calculate_1x5(x6_C3_VAR)
x6_C4_RMS_overall = RMS_calculate_1x5(x6_C4_RMS)
x6_C4_VAR_overall = VAR_calculate_1x5(x6_C4_VAR)
x6_C5_RMS_overall = RMS_calculate_1x5(x6_C5_RMS)
x6_C5_VAR_overall = VAR_calculate_1x5(x6_C5_VAR)
x6_C6_RMS_overall = RMS_calculate_1x5(x6_C6_RMS)
x6_C6_VAR_overall = VAR_calculate_1x5(x6_C6_VAR)
# --- Rms and var across the different subjects ---
# C1
overall_array_x_C1_RMS = [x1_C1_RMS_overall, x2_C1_RMS_overall, x3_C1_RMS_overall, x4_C1_RMS_overall, x5_C1_RMS_overall, x6_C1_RMS_overall]
x_C1_RMS = RMS_calculate_1x6(overall_array_x_C1_RMS)
overall_array_x_C1_VAR = [x1_C1_VAR_overall, x2_C1_VAR_overall, x3_C1_VAR_overall, x4_C1_VAR_overall, x5_C1_VAR_overall, x6_C1_VAR_overall]
x_C1_VAR = VAR_calculate_1x6(overall_array_x_C1_VAR)
# C2
overall_array_x_C2_RMS = [x1_C2_RMS_overall, x2_C2_RMS_overall, x3_C2_RMS_overall, x4_C2_RMS_overall, x5_C2_RMS_overall, x6_C2_RMS_overall]
x_C2_RMS = RMS_calculate_1x6(overall_array_x_C2_RMS)
overall_array_x_C2_VAR = [x1_C2_VAR_overall, x2_C2_VAR_overall, x3_C2_VAR_overall, x4_C2_VAR_overall, x5_C2_VAR_overall, x6_C2_VAR_overall]
x_C2_VAR = VAR_calculate_1x6(overall_array_x_C2_VAR)
# C3
overall_array_x_C3_RMS = [x1_C3_RMS_overall, x2_C3_RMS_overall, x3_C3_RMS_overall, x4_C3_RMS_overall, x5_C3_RMS_overall, x6_C3_RMS_overall]
x_C3_RMS = RMS_calculate_1x6(overall_array_x_C3_RMS)
overall_array_x_C3_VAR = [x1_C3_VAR_overall, x2_C3_VAR_overall, x3_C3_VAR_overall, x4_C3_VAR_overall, x5_C3_VAR_overall, x6_C3_VAR_overall]
x_C3_VAR = VAR_calculate_1x6(overall_array_x_C3_VAR)
# C4
overall_array_x_C4_RMS = [x1_C4_RMS_overall, x2_C4_RMS_overall, x3_C4_RMS_overall, x4_C4_RMS_overall, x5_C4_RMS_overall, x6_C4_RMS_overall]
x_C4_RMS = RMS_calculate_1x6(overall_array_x_C4_RMS)
overall_array_x_C4_VAR = [x1_C4_VAR_overall, x2_C4_VAR_overall, x3_C4_VAR_overall, x4_C4_VAR_overall, x5_C4_VAR_overall, x6_C4_VAR_overall]
x_C4_VAR = VAR_calculate_1x6(overall_array_x_C4_VAR)
# C5
overall_array_x_C5_RMS = [x1_C5_RMS_overall, x2_C5_RMS_overall, x3_C5_RMS_overall, x4_C5_RMS_overall, x5_C5_RMS_overall, x6_C5_RMS_overall]
x_C5_RMS = RMS_calculate_1x6(overall_array_x_C5_RMS)
overall_array_x_C5_VAR = [x1_C5_VAR_overall, x2_C5_VAR_overall, x3_C5_VAR_overall, x4_C5_VAR_overall, x5_C5_VAR_overall, x6_C5_VAR_overall]
x_C5_VAR = VAR_calculate_1x6(overall_array_x_C5_VAR)
# C6
overall_array_x_C6_RMS = [x1_C6_RMS_overall, x2_C6_RMS_overall, x3_C6_RMS_overall, x4_C6_RMS_overall, x5_C6_RMS_overall, x6_C6_RMS_overall]
x_C6_RMS = RMS_calculate_1x6(overall_array_x_C6_RMS)
overall_array_x_C6_VAR = [x1_C6_VAR_overall, x2_C6_VAR_overall, x3_C6_VAR_overall, x4_C6_VAR_overall, x5_C6_VAR_overall, x6_C6_VAR_overall]
x_C6_VAR = VAR_calculate_1x6(overall_array_x_C6_VAR)
print("RMS of vehicle output in scenario 1 is:",x_C1_RMS,"VAR is:", x_C1_VAR)
print("RMS of vehicle output in scenario 2 is:",x_C2_RMS,"VAR is:", x_C2_VAR)
print("RMS of vehicle output in scenario 3 is:",x_C3_RMS,"VAR is:", x_C3_VAR)
print("RMS of vehicle output in scenario 4 is:",x_C4_RMS,"VAR is:", x_C4_VAR)
print("RMS of vehicle output in scenario 5 is:",x_C5_RMS,"VAR is:", x_C5_VAR)
print("RMS of vehicle output in scenario 6 is:",x_C6_RMS,"VAR is:", x_C6_VAR)
"""

# --------------------------- Maximum and Minimum --------------------------------
'''
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
'''
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
<<<<<<< HEAD
=======
"""


#------------------------- TIME RESPONSE DELAY ---------------------------------
#Find the delay in ft (forcing function) and u (pilot output)


# Human operator control input and forcign function as a function of time
#plt.subplot(131)

scattertab1 = []
scattertab2 = []
scattertab3 = []
scattertab4 = []
scattertab5 = []
scattertab6 = []

#-----------------------Pilot 1----------------------#
print("Pilot 1")
aa1= u1_C1[:,0]
ba1= u1_C1[:,1]
ca1= u1_C1[:,2]
da1= u1_C1[:,3]
ea1= u1_C1[:,4]

aa2= u1_C2[:,0]
ba2= u1_C2[:,1]
ca2= u1_C2[:,2]
da2= u1_C2[:,3]
ea2= u1_C2[:,4]

aa3= u1_C3[:,0]
ba3= u1_C3[:,1]
ca3= u1_C3[:,2]
da3= u1_C3[:,3]
ea3= u1_C3[:,4]

aa4= u1_C4[:,0]
ba4= u1_C4[:,1]
ca4= u1_C4[:,2]
da4= u1_C4[:,3]
ea4= u1_C4[:,4]

aa5= u1_C5[:,0]
ba5= u1_C5[:,1]
ca5= u1_C5[:,2]
da5= u1_C5[:,3]
ea5= u1_C5[:,4]

aa6= u1_C6[:,0]
ba6= u1_C6[:,1]
ca6= u1_C6[:,2]
da6= u1_C6[:,3]
ea6= u1_C6[:,4]


ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ua11ttab = []
ua12ttab = []
ua13ttab = []
ua14ttab = []
ua15ttab = []

ua21ttab = []
ua22ttab = []
ua23ttab = []
ua24ttab = []
ua25ttab = []

ua31ttab = []
ua32ttab = []
ua33ttab = []
ua34ttab = []
ua35ttab = []

ua41ttab = []
ua42ttab = []
ua43ttab = []
ua44ttab = []
ua45ttab = []

ua51ttab = []
ua52ttab = []
ua53ttab = []
ua54ttab = []
ua55ttab = []

ua61ttab = []
ua62ttab = []
ua63ttab = []
ua64ttab = []
ua65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

ua11ttab.remove(1523)


qa1tab = []
ra1tab = []
sa1tab = []
ta1tab = []
ua1tab = []

qa2tab = []
ra2tab = []
sa2tab = []
ta2tab = []
ua2tab = []

qa3tab = []
ra3tab = []
sa3tab = []
ta3tab = []
ua3tab = []

qa4tab = []
ra4tab = []
sa4tab = []
ta4tab = []
ua4tab = []

qa5tab = []
ra5tab = []
sa5tab = []
ta5tab = []
ua5tab = []

qa6tab = []
ra6tab = []
sa6tab = []
ta6tab = []
ua6tab = []

for i in range(len(ft1ttab)):
  va1 = abs(ft1ttab[i] - ua11ttab[i])
  wa1 = abs(ft1ttab[i] - ua12ttab[i])
  xa1 = abs(ft1ttab[i] - ua13ttab[i])
  ya1 = abs(ft1ttab[i] - ua14ttab[i])
  za1 = abs(ft1ttab[i] - ua15ttab[i])

  va2 = abs(ft1ttab[i] - ua21ttab[i])
  wa2 = abs(ft1ttab[i] - ua22ttab[i])
  xa2 = abs(ft1ttab[i] - ua23ttab[i])
  ya2 = abs(ft1ttab[i] - ua24ttab[i])
  za2 = abs(ft1ttab[i] - ua25ttab[i])

  va3 = abs(ft1ttab[i] - ua31ttab[i])
  wa3 = abs(ft1ttab[i] - ua32ttab[i])
  xa3 = abs(ft1ttab[i] - ua33ttab[i])
  ya3 = abs(ft1ttab[i] - ua34ttab[i])
  za3 = abs(ft1ttab[i] - ua35ttab[i])

  va4 = abs(ft1ttab[i] - ua41ttab[i])
  wa4 = abs(ft1ttab[i] - ua42ttab[i])
  xa4 = abs(ft1ttab[i] - ua43ttab[i])
  ya4 = abs(ft1ttab[i] - ua44ttab[i])
  za4 = abs(ft1ttab[i] - ua45ttab[i])

  va5 = abs(ft1ttab[i] - ua51ttab[i])
  wa5 = abs(ft1ttab[i] - ua52ttab[i])
  xa5 = abs(ft1ttab[i] - ua53ttab[i])
  ya5 = abs(ft1ttab[i] - ua54ttab[i])
  za5 = abs(ft1ttab[i] - ua55ttab[i])

  va6 = abs(ft1ttab[i] - ua61ttab[i])
  wa6 = abs(ft1ttab[i] - ua62ttab[i])
  xa6 = abs(ft1ttab[i] - ua63ttab[i])
  ya6 = abs(ft1ttab[i] - ua64ttab[i])
  za6 = abs(ft1ttab[i] - ua65ttab[i])

  qa1tab.append(va1)
  ra1tab.append(wa1)
  sa1tab.append(xa1)
  ta1tab.append(ya1)
  ua1tab.append(za1)

  qa2tab.append(va2)
  ra2tab.append(wa2)
  sa2tab.append(xa2)
  ta2tab.append(ya2)
  ua2tab.append(za2)
  
  qa3tab.append(va3)
  ra3tab.append(wa3)
  sa3tab.append(xa3)
  ta3tab.append(ya3)
  ua3tab.append(za3)

  qa4tab.append(va4)
  ra4tab.append(wa4)
  sa4tab.append(xa4)
  ta4tab.append(ya4)
  ua4tab.append(za4)

  qa5tab.append(va5)
  ra5tab.append(wa5)
  sa5tab.append(xa5)
  ta5tab.append(ya5)
  ua5tab.append(za5)

  qa6tab.append(va6)
  ra6tab.append(wa6)
  sa6tab.append(xa6)
  ta6tab.append(ya6)
  ua6tab.append(za6)

aaa1 = sum(qa1tab)/len(qa1tab)/100
bba1 = sum(ra1tab)/len(qa1tab)/100
cca1 = sum(sa1tab)/len(qa1tab)/100
dda1 = sum(ta1tab)/len(qa1tab)/100
eea1 = sum(ua1tab)/len(qa1tab)/100

aaa2 = sum(qa2tab)/len(qa1tab)/100
bba2 = sum(ra2tab)/len(qa1tab)/100
cca2 = sum(sa2tab)/len(qa1tab)/100
dda2 = sum(ta2tab)/len(qa1tab)/100
eea2 = sum(ua2tab)/len(qa1tab)/100

aaa3 = sum(qa3tab)/len(qa1tab)/100
bba3 = sum(ra3tab)/len(qa1tab)/100
cca3 = sum(sa3tab)/len(qa1tab)/100
dda3 = sum(ta3tab)/len(qa1tab)/100
eea3 = sum(ua3tab)/len(qa1tab)/100

aaa4 = sum(qa4tab)/len(qa1tab)/100
bba4 = sum(ra4tab)/len(qa1tab)/100
cca4 = sum(sa4tab)/len(qa1tab)/100
dda4 = sum(ta4tab)/len(qa1tab)/100
eea4 = sum(ua4tab)/len(qa1tab)/100

aaa5 = sum(qa5tab)/len(qa1tab)/100
bba5 = sum(ra5tab)/len(qa1tab)/100
cca5 = sum(sa5tab)/len(qa1tab)/100
dda5 = sum(ta5tab)/len(qa1tab)/100
eea5 = sum(ua5tab)/len(qa1tab)/100

aaa6 = sum(qa6tab)/len(qa1tab)/100
bba6 = sum(ra6tab)/len(qa1tab)/100
cca6 = sum(sa6tab)/len(qa1tab)/100
dda6 = sum(ta6tab)/len(qa1tab)/100
eea6 = sum(ua6tab)/len(qa1tab)/100

print(aaa1,bba1,cca1,dda1,eea1)
print((aaa1+bba1+cca1+dda1+eea1)/5)
scattertab1.append((aaa1+bba1+cca1+dda1+eea1)/5)

print(aaa2,bba2,cca2,dda2,eea2)
print((aaa2+bba2+cca2+dda2+eea2)/5)
scattertab1.append((aaa2+bba2+cca2+dda2+eea2)/5)

print(aaa3,bba3,cca3,dda3,eea3)
print((aaa3+bba3+cca3+dda3+eea3)/5)
scattertab1.append((aaa3+bba3+cca3+dda3+eea3)/5)

print(aaa4,bba4,cca4,dda4,eea4)
print((aaa4+bba4+cca4+dda4+eea4)/5)
scattertab1.append((aaa4+bba4+cca4+dda4+eea4)/5)

print(aaa5,bba5,cca5,dda5,eea5)
print((aaa5+bba5+cca5+dda5+eea5)/5)
scattertab1.append((aaa5+bba5+cca5+dda5+eea5)/5)

print(aaa6,bba6,cca6,dda6,eea6)
print((aaa6+bba6+cca6+dda6+eea6)/5)
scattertab1.append((aaa6+bba6+cca6+dda6+eea6)/5)

#-----------------------Pilot 2----------------------#
print("Pilot 2")
ab1= u2_C1[:,0]
bb1= u2_C1[:,1]
cb1= u2_C1[:,2]
db1= u2_C1[:,3]
eb1= u2_C1[:,4]

ab2= u2_C2[:,0]
bb2= u2_C2[:,1]
cb2= u2_C2[:,2]
db2= u2_C2[:,3]
eb2= u2_C2[:,4]

ab3= u2_C3[:,0]
bb3= u2_C3[:,1]
cb3= u2_C3[:,2]
db3= u2_C3[:,3]
eb3= u2_C3[:,4]

ab4= u2_C4[:,0]
bb4= u2_C4[:,1]
cb4= u2_C4[:,2]
db4= u2_C4[:,3]
eb4= u2_C4[:,4]

ab5= u2_C5[:,0]
bb5= u2_C5[:,1]
cb5= u2_C5[:,2]
db5= u2_C5[:,3]
eb5= u2_C5[:,4]

ab6= u2_C6[:,0]
bb6= u2_C6[:,1]
cb6= u2_C6[:,2]
db6= u2_C6[:,3]
eb6= u2_C6[:,4]

ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ub11ttab = []
ub12ttab = []
ub13ttab = []
ub14ttab = []
ub15ttab = []

ub21ttab = []
ub22ttab = []
ub23ttab = []
ub24ttab = []
ub25ttab = []

ub31ttab = []
ub32ttab = []
ub33ttab = []
ub34ttab = []
ub35ttab = []

ub41ttab = []
ub42ttab = []
ub43ttab = []
ub44ttab = []
ub45ttab = []

ub51ttab = []
ub52ttab = []
ub53ttab = []
ub54ttab = []
ub55ttab = []

ub61ttab = []
ub62ttab = []
ub63ttab = []
ub64ttab = []
ub65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1b = np.min(ab1[ft1ttab[n]:ftab[n]])
    l1b = np.min(bb1[ft1ttab[n]:ftab[n]])
    m1b = np.min(cb1[ft1ttab[n]:ftab[n]])
    o1b = np.min(db1[ft1ttab[n]:ftab[n]])
    p1b = np.min(eb1[ft1ttab[n]:ftab[n]])

    k2b = np.min(ab2[ft1ttab[n]:ftab[n]])
    l2b = np.min(bb2[ft1ttab[n]:ftab[n]])
    m2b = np.min(cb2[ft1ttab[n]:ftab[n]])
    o2b = np.min(db2[ft1ttab[n]:ftab[n]])
    p2b = np.min(eb2[ft1ttab[n]:ftab[n]])

    k3b = np.min(ab3[ft1ttab[n]:ftab[n]])
    l3b = np.min(bb3[ft1ttab[n]:ftab[n]])
    m3b = np.min(cb3[ft1ttab[n]:ftab[n]])
    o3b = np.min(db3[ft1ttab[n]:ftab[n]])
    p3b = np.min(eb3[ft1ttab[n]:ftab[n]])

    k4b = np.min(ab4[ft1ttab[n]:ftab[n]])
    l4b = np.min(bb4[ft1ttab[n]:ftab[n]])
    m4b = np.min(cb4[ft1ttab[n]:ftab[n]])
    o4b = np.min(db4[ft1ttab[n]:ftab[n]])
    p4b = np.min(eb4[ft1ttab[n]:ftab[n]])

    k5b = np.min(ab5[ft1ttab[n]:ftab[n]])
    l5b = np.min(bb5[ft1ttab[n]:ftab[n]])
    m5b = np.min(cb5[ft1ttab[n]:ftab[n]])
    o5b = np.min(db5[ft1ttab[n]:ftab[n]])
    p5b = np.min(eb5[ft1ttab[n]:ftab[n]])

    k6b = np.min(ab6[ft1ttab[n]:ftab[n]])
    l6b = np.min(bb6[ft1ttab[n]:ftab[n]])
    m6b = np.min(cb6[ft1ttab[n]:ftab[n]])
    o6b = np.min(db6[ft1ttab[n]:ftab[n]])
    p6b = np.min(eb6[ft1ttab[n]:ftab[n]])

    kab = (np.where(ab1 == k1b)[0]).tolist()
    lab = (np.where(bb1 == l1b)[0]).tolist()
    mab = (np.where(cb1 == m1b)[0]).tolist()
    oab = (np.where(db1 == o1b)[0]).tolist()
    pab = (np.where(eb1 == p1b)[0]).tolist()
    
    kbb = (np.where(ab2 == k2b)[0]).tolist()
    lbb = (np.where(bb2 == l2b)[0]).tolist()
    mbb = (np.where(cb2 == m2b)[0]).tolist()
    obb = (np.where(db2 == o2b)[0]).tolist()
    pbb = (np.where(eb2 == p2b)[0]).tolist()

    kcb = (np.where(ab3 == k3b)[0]).tolist()
    lcb = (np.where(bb3 == l3b)[0]).tolist()
    mcb = (np.where(cb3 == m3b)[0]).tolist()
    ocb = (np.where(db3 == o3b)[0]).tolist()
    pcb = (np.where(eb3 == p3b)[0]).tolist()

    kdb = (np.where(ab4 == k4b)[0]).tolist()
    ldb = (np.where(bb4 == l4b)[0]).tolist()
    mdb = (np.where(cb4 == m4b)[0]).tolist()
    odb = (np.where(db4 == o4b)[0]).tolist()
    pdb = (np.where(eb4 == p4b)[0]).tolist()
    
    keb = (np.where(ab5 == k5b)[0]).tolist()
    leb = (np.where(bb5 == l5b)[0]).tolist()
    meb = (np.where(cb5 == m5b)[0]).tolist()
    oeb = (np.where(db5 == o5b)[0]).tolist()
    peb = (np.where(eb5 == p5b)[0]).tolist()
    
    kfb = (np.where(ab6 == k6b)[0]).tolist()
    lfb = (np.where(bb6 == l6b)[0]).tolist()
    mfb = (np.where(cb6 == m6b)[0]).tolist()
    ofb = (np.where(db6 == o6b)[0]).tolist()
    pfb = (np.where(eb6 == p6b)[0]).tolist()

    ub11ttab.extend(kab)
    ub12ttab.extend(lab)
    ub13ttab.extend(mab)
    ub14ttab.extend(oab)
    ub15ttab.extend(pab)

    ub21ttab.extend(kbb)
    ub22ttab.extend(lbb)
    ub23ttab.extend(mbb)
    ub24ttab.extend(obb)
    ub25ttab.extend(pbb)

    ub31ttab.extend(kcb)
    ub32ttab.extend(lcb)
    ub33ttab.extend(mcb)
    ub34ttab.extend(ocb)
    ub35ttab.extend(pcb)

    ub41ttab.extend(kdb)
    ub42ttab.extend(ldb)
    ub43ttab.extend(mdb)
    ub44ttab.extend(odb)
    ub45ttab.extend(pdb)

    ub51ttab.extend(keb)
    ub52ttab.extend(leb)
    ub53ttab.extend(meb)
    ub54ttab.extend(oeb)
    ub55ttab.extend(peb)

    ub61ttab.extend(kfb)
    ub62ttab.extend(lfb)
    ub63ttab.extend(mfb)
    ub64ttab.extend(ofb)
    ub65ttab.extend(pfb)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1b = np.min(ab1[ft1ttab[n]:ftab[n]])
    l1b = np.min(bb1[ft1ttab[n]:ftab[n]])
    m1b = np.min(cb1[ft1ttab[n]:ftab[n]])
    o1b = np.min(db1[ft1ttab[n]:ftab[n]])
    p1b = np.min(eb1[ft1ttab[n]:ftab[n]])

    k2b = np.min(ab2[ft1ttab[n]:ftab[n]])
    l2b = np.min(bb2[ft1ttab[n]:ftab[n]])
    m2b = np.min(cb2[ft1ttab[n]:ftab[n]])
    o2b = np.min(db2[ft1ttab[n]:ftab[n]])
    p2b = np.min(eb2[ft1ttab[n]:ftab[n]])

    k3b = np.min(ab3[ft1ttab[n]:ftab[n]])
    l3b = np.min(bb3[ft1ttab[n]:ftab[n]])
    m3b = np.min(cb3[ft1ttab[n]:ftab[n]])
    o3b = np.min(db3[ft1ttab[n]:ftab[n]])
    p3b = np.min(eb3[ft1ttab[n]:ftab[n]])

    k4b = np.min(ab4[ft1ttab[n]:ftab[n]])
    l4b = np.min(bb4[ft1ttab[n]:ftab[n]])
    m4b = np.min(cb4[ft1ttab[n]:ftab[n]])
    o4b = np.min(db4[ft1ttab[n]:ftab[n]])
    p4b = np.min(eb4[ft1ttab[n]:ftab[n]])

    k5b = np.min(ab5[ft1ttab[n]:ftab[n]])
    l5b = np.min(bb5[ft1ttab[n]:ftab[n]])
    m5b = np.min(cb5[ft1ttab[n]:ftab[n]])
    o5b = np.min(db5[ft1ttab[n]:ftab[n]])
    p5b = np.min(eb5[ft1ttab[n]:ftab[n]])

    k6b = np.min(ab6[ft1ttab[n]:ftab[n]])
    l6b = np.min(bb6[ft1ttab[n]:ftab[n]])
    m6b = np.min(cb6[ft1ttab[n]:ftab[n]])
    o6b = np.min(db6[ft1ttab[n]:ftab[n]])
    p6b = np.min(eb6[ft1ttab[n]:ftab[n]])

    kab = (np.where(ab1 == k1b)[0]).tolist()
    lab = (np.where(bb1 == l1b)[0]).tolist()
    mab = (np.where(cb1 == m1b)[0]).tolist()
    oab = (np.where(db1 == o1b)[0]).tolist()
    pab = (np.where(eb1 == p1b)[0]).tolist()
    
    kbb = (np.where(ab2 == k2b)[0]).tolist()
    lbb = (np.where(bb2 == l2b)[0]).tolist()
    mbb = (np.where(cb2 == m2b)[0]).tolist()
    obb = (np.where(db2 == o2b)[0]).tolist()
    pbb = (np.where(eb2 == p2b)[0]).tolist()

    kcb = (np.where(ab3 == k3b)[0]).tolist()
    lcb = (np.where(bb3 == l3b)[0]).tolist()
    mcb = (np.where(cb3 == m3b)[0]).tolist()
    ocb = (np.where(db3 == o3b)[0]).tolist()
    pcb = (np.where(eb3 == p3b)[0]).tolist()

    kdb = (np.where(ab4 == k4b)[0]).tolist()
    ldb = (np.where(bb4 == l4b)[0]).tolist()
    mdb = (np.where(cb4 == m4b)[0]).tolist()
    odb = (np.where(db4 == o4b)[0]).tolist()
    pdb = (np.where(eb4 == p4b)[0]).tolist()
    
    keb = (np.where(ab5 == k5b)[0]).tolist()
    leb = (np.where(bb5 == l5b)[0]).tolist()
    meb = (np.where(cb5 == m5b)[0]).tolist()
    oeb = (np.where(db5 == o5b)[0]).tolist()
    peb = (np.where(eb5 == p5b)[0]).tolist()
    
    kfb = (np.where(ab6 == k6b)[0]).tolist()
    lfb = (np.where(bb6 == l6b)[0]).tolist()
    mfb = (np.where(cb6 == m6b)[0]).tolist()
    ofb = (np.where(db6 == o6b)[0]).tolist()
    pfb = (np.where(eb6 == p6b)[0]).tolist()

    ub11ttab.extend(kab)
    ub12ttab.extend(lab)
    ub13ttab.extend(mab)
    ub14ttab.extend(oab)
    ub15ttab.extend(pab)

    ub21ttab.extend(kbb)
    ub22ttab.extend(lbb)
    ub23ttab.extend(mbb)
    ub24ttab.extend(obb)
    ub25ttab.extend(pbb)

    ub31ttab.extend(kcb)
    ub32ttab.extend(lcb)
    ub33ttab.extend(mcb)
    ub34ttab.extend(ocb)
    ub35ttab.extend(pcb)

    ub41ttab.extend(kdb)
    ub42ttab.extend(ldb)
    ub43ttab.extend(mdb)
    ub44ttab.extend(odb)
    ub45ttab.extend(pdb)

    ub51ttab.extend(keb)
    ub52ttab.extend(leb)
    ub53ttab.extend(meb)
    ub54ttab.extend(oeb)
    ub55ttab.extend(peb)

    ub61ttab.extend(kfb)
    ub62ttab.extend(lfb)
    ub63ttab.extend(mfb)
    ub64ttab.extend(ofb)
    ub65ttab.extend(pfb)

#ub11ttab.remove(1523)
ub43ttab.remove(1416)


qb1tab = []
rb1tab = []
sb1tab = []
tb1tab = []
ub1tab = []

qb2tab = []
rb2tab = []
sb2tab = []
tb2tab = []
ub2tab = []

qb3tab = []
rb3tab = []
sb3tab = []
tb3tab = []
ub3tab = []

qb4tab = []
rb4tab = []
sb4tab = []
tb4tab = []
ub4tab = []

qb5tab = []
rb5tab = []
sb5tab = []
tb5tab = []
ub5tab = []

qb6tab = []
rb6tab = []
sb6tab = []
tb6tab = []
ub6tab = []

for i in range(len(ft1ttab)):
  vb1 = abs(ft1ttab[i] - ub11ttab[i])
  wb1 = abs(ft1ttab[i] - ub12ttab[i])
  xb1 = abs(ft1ttab[i] - ub13ttab[i])
  yb1 = abs(ft1ttab[i] - ub14ttab[i])
  zb1 = abs(ft1ttab[i] - ub15ttab[i])

  vb2 = abs(ft1ttab[i] - ub21ttab[i])
  wb2 = abs(ft1ttab[i] - ub22ttab[i])
  xb2 = abs(ft1ttab[i] - ub23ttab[i])
  yb2 = abs(ft1ttab[i] - ub24ttab[i])
  zb2 = abs(ft1ttab[i] - ub25ttab[i])

  vb3 = abs(ft1ttab[i] - ub31ttab[i])
  wb3 = abs(ft1ttab[i] - ub32ttab[i])
  xb3 = abs(ft1ttab[i] - ub33ttab[i])
  yb3 = abs(ft1ttab[i] - ub34ttab[i])
  zb3 = abs(ft1ttab[i] - ub35ttab[i])

  vb4 = abs(ft1ttab[i] - ub41ttab[i])
  wb4 = abs(ft1ttab[i] - ub42ttab[i])
  xb4 = abs(ft1ttab[i] - ub43ttab[i])
  yb4 = abs(ft1ttab[i] - ub44ttab[i])
  zb4 = abs(ft1ttab[i] - ub45ttab[i])

  vb5 = abs(ft1ttab[i] - ub51ttab[i])
  wb5 = abs(ft1ttab[i] - ub52ttab[i])
  xb5 = abs(ft1ttab[i] - ub53ttab[i])
  yb5 = abs(ft1ttab[i] - ub54ttab[i])
  zb5 = abs(ft1ttab[i] - ub55ttab[i])

  vb6 = abs(ft1ttab[i] - ub61ttab[i])
  wb6 = abs(ft1ttab[i] - ub62ttab[i])
  xb6 = abs(ft1ttab[i] - ub63ttab[i])
  yb6 = abs(ft1ttab[i] - ub64ttab[i])
  zb6 = abs(ft1ttab[i] - ub65ttab[i])

  qb1tab.append(vb1)
  rb1tab.append(wb1)
  sb1tab.append(xb1)
  tb1tab.append(yb1)
  ub1tab.append(zb1)

  qb2tab.append(vb2)
  rb2tab.append(wb2)
  sb2tab.append(xb2)
  tb2tab.append(yb2)
  ub2tab.append(zb2)
  
  qb3tab.append(vb3)
  rb3tab.append(wb3)
  sb3tab.append(xb3)
  tb3tab.append(yb3)
  ub3tab.append(zb3)

  qb4tab.append(vb4)
  rb4tab.append(wb4)
  sb4tab.append(xb4)
  tb4tab.append(yb4)
  ub4tab.append(zb4)

  qb5tab.append(vb5)
  rb5tab.append(wb5)
  sb5tab.append(xb5)
  tb5tab.append(yb5)
  ub5tab.append(zb5)

  qb6tab.append(vb6)
  rb6tab.append(wb6)
  sb6tab.append(xb6)
  tb6tab.append(yb6)
  ub6tab.append(zb6)

aab1 = sum(qb1tab)/len(qb1tab)/100
bbb1 = sum(rb1tab)/len(qb1tab)/100
ccb1 = sum(sb1tab)/len(qb1tab)/100
ddb1 = sum(tb1tab)/len(qb1tab)/100
eeb1 = sum(ub1tab)/len(qb1tab)/100

aab2 = sum(qb2tab)/len(qb1tab)/100
bbb2 = sum(rb2tab)/len(qb1tab)/100
ccb2 = sum(sb2tab)/len(qb1tab)/100
ddb2 = sum(tb2tab)/len(qb1tab)/100
eeb2 = sum(ub2tab)/len(qb1tab)/100

aab3 = sum(qb3tab)/len(qb1tab)/100
bbb3 = sum(rb3tab)/len(qb1tab)/100
ccb3 = sum(sb3tab)/len(qb1tab)/100
ddb3 = sum(tb3tab)/len(qb1tab)/100
eeb3 = sum(ub3tab)/len(qb1tab)/100

aab4 = sum(qb4tab)/len(qb1tab)/100
bbb4 = sum(rb4tab)/len(qb1tab)/100
ccb4 = sum(sb4tab)/len(qb1tab)/100
ddb4 = sum(tb4tab)/len(qb1tab)/100
eeb4 = sum(ub4tab)/len(qb1tab)/100

aab5 = sum(qb5tab)/len(qb1tab)/100
bbb5 = sum(rb5tab)/len(qb1tab)/100
ccb5 = sum(sb5tab)/len(qb1tab)/100
ddb5 = sum(tb5tab)/len(qb1tab)/100
eeb5 = sum(ub5tab)/len(qb1tab)/100

aab6 = sum(qb6tab)/len(qb1tab)/100
bbb6 = sum(rb6tab)/len(qb1tab)/100
ccb6 = sum(sb6tab)/len(qb1tab)/100
ddb6 = sum(tb6tab)/len(qb1tab)/100
eeb6 = sum(ub6tab)/len(qb1tab)/100

print(aab1,bbb1,ccb1,ddb1,eeb1)
print((aab1+bbb1+ccb1+ddb1+eeb1)/5)
scattertab2.append((aab1+bbb1+ccb1+ddb1+eeb1)/5)

print(aab2,bbb2,ccb2,ddb2,eeb2)
print((aab2+bbb2+ccb2+ddb2+eeb2)/5)
scattertab2.append((aab2+bbb2+ccb2+ddb2+eeb2)/5)

print(aab3,bbb3,ccb3,ddb3,eeb3)
print((aab3+bbb3+ccb3+ddb3+eeb3)/5)
scattertab2.append((aab3+bbb3+ccb3+ddb3+eeb3)/5)

print(aab4,bbb4,ccb4,ddb4,eeb4)
print((aab4+bbb4+ccb4+ddb4+eeb4)/5)
scattertab2.append((aab4+bbb4+ccb4+ddb4+eeb4)/5)

print(aab5,bbb5,ccb5,ddb5,eeb5)
print((aab5+bbb5+ccb5+ddb5+eeb5)/5)
scattertab2.append((aab5+bbb5+ccb5+ddb5+eeb5)/5)

print(aab6,bbb6,ccb6,ddb6,eeb6)
print((aab6+bbb6+ccb6+ddb6+eeb6)/5)
scattertab2.append((aab6+bbb6+ccb6+ddb6+eeb6)/5)

#-----------------------Pilot 3----------------------#
print("pilot3")
aa1= u3_C1[:,0]
ba1= u3_C1[:,1]
ca1= u3_C1[:,2]
da1= u3_C1[:,3]
ea1= u3_C1[:,4]

aa2= u3_C2[:,0]
ba2= u3_C2[:,1]
ca2= u3_C2[:,2]
da2= u3_C2[:,3]
ea2= u3_C2[:,4]

aa3= u3_C3[:,0]
ba3= u3_C3[:,1]
ca3= u3_C3[:,2]
da3= u3_C3[:,3]
ea3= u3_C3[:,4]

aa4= u3_C4[:,0]
ba4= u3_C4[:,1]
ca4= u3_C4[:,2]
da4= u3_C4[:,3]
ea4= u3_C4[:,4]

aa5= u3_C5[:,0]
ba5= u3_C5[:,1]
ca5= u3_C5[:,2]
da5= u3_C5[:,3]
ea5= u3_C5[:,4]

aa6= u3_C6[:,0]
ba6= u3_C6[:,1]
ca6= u3_C6[:,2]
da6= u3_C6[:,3]
ea6= u3_C6[:,4]


ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ua11ttab = []
ua12ttab = []
ua13ttab = []
ua14ttab = []
ua15ttab = []

ua21ttab = []
ua22ttab = []
ua23ttab = []
ua24ttab = []
ua25ttab = []

ua31ttab = []
ua32ttab = []
ua33ttab = []
ua34ttab = []
ua35ttab = []

ua41ttab = []
ua42ttab = []
ua43ttab = []
ua44ttab = []
ua45ttab = []

ua51ttab = []
ua52ttab = []
ua53ttab = []
ua54ttab = []
ua55ttab = []

ua61ttab = []
ua62ttab = []
ua63ttab = []
ua64ttab = []
ua65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

#ua11ttab.remove(1523)


qa1tab = []
ra1tab = []
sa1tab = []
ta1tab = []
ua1tab = []

qa2tab = []
ra2tab = []
sa2tab = []
ta2tab = []
ua2tab = []

qa3tab = []
ra3tab = []
sa3tab = []
ta3tab = []
ua3tab = []

qa4tab = []
ra4tab = []
sa4tab = []
ta4tab = []
ua4tab = []

qa5tab = []
ra5tab = []
sa5tab = []
ta5tab = []
ua5tab = []

qa6tab = []
ra6tab = []
sa6tab = []
ta6tab = []
ua6tab = []

for i in range(len(ft1ttab)):
  va1 = abs(ft1ttab[i] - ua11ttab[i])
  wa1 = abs(ft1ttab[i] - ua12ttab[i])
  xa1 = abs(ft1ttab[i] - ua13ttab[i])
  ya1 = abs(ft1ttab[i] - ua14ttab[i])
  za1 = abs(ft1ttab[i] - ua15ttab[i])

  va2 = abs(ft1ttab[i] - ua21ttab[i])
  wa2 = abs(ft1ttab[i] - ua22ttab[i])
  xa2 = abs(ft1ttab[i] - ua23ttab[i])
  ya2 = abs(ft1ttab[i] - ua24ttab[i])
  za2 = abs(ft1ttab[i] - ua25ttab[i])

  va3 = abs(ft1ttab[i] - ua31ttab[i])
  wa3 = abs(ft1ttab[i] - ua32ttab[i])
  xa3 = abs(ft1ttab[i] - ua33ttab[i])
  ya3 = abs(ft1ttab[i] - ua34ttab[i])
  za3 = abs(ft1ttab[i] - ua35ttab[i])

  va4 = abs(ft1ttab[i] - ua41ttab[i])
  wa4 = abs(ft1ttab[i] - ua42ttab[i])
  xa4 = abs(ft1ttab[i] - ua43ttab[i])
  ya4 = abs(ft1ttab[i] - ua44ttab[i])
  za4 = abs(ft1ttab[i] - ua45ttab[i])

  va5 = abs(ft1ttab[i] - ua51ttab[i])
  wa5 = abs(ft1ttab[i] - ua52ttab[i])
  xa5 = abs(ft1ttab[i] - ua53ttab[i])
  ya5 = abs(ft1ttab[i] - ua54ttab[i])
  za5 = abs(ft1ttab[i] - ua55ttab[i])

  va6 = abs(ft1ttab[i] - ua61ttab[i])
  wa6 = abs(ft1ttab[i] - ua62ttab[i])
  xa6 = abs(ft1ttab[i] - ua63ttab[i])
  ya6 = abs(ft1ttab[i] - ua64ttab[i])
  za6 = abs(ft1ttab[i] - ua65ttab[i])

  qa1tab.append(va1)
  ra1tab.append(wa1)
  sa1tab.append(xa1)
  ta1tab.append(ya1)
  ua1tab.append(za1)

  qa2tab.append(va2)
  ra2tab.append(wa2)
  sa2tab.append(xa2)
  ta2tab.append(ya2)
  ua2tab.append(za2)
  
  qa3tab.append(va3)
  ra3tab.append(wa3)
  sa3tab.append(xa3)
  ta3tab.append(ya3)
  ua3tab.append(za3)

  qa4tab.append(va4)
  ra4tab.append(wa4)
  sa4tab.append(xa4)
  ta4tab.append(ya4)
  ua4tab.append(za4)

  qa5tab.append(va5)
  ra5tab.append(wa5)
  sa5tab.append(xa5)
  ta5tab.append(ya5)
  ua5tab.append(za5)

  qa6tab.append(va6)
  ra6tab.append(wa6)
  sa6tab.append(xa6)
  ta6tab.append(ya6)
  ua6tab.append(za6)

aaa1 = sum(qa1tab)/len(qa1tab)/100
bba1 = sum(ra1tab)/len(qa1tab)/100
cca1 = sum(sa1tab)/len(qa1tab)/100
dda1 = sum(ta1tab)/len(qa1tab)/100
eea1 = sum(ua1tab)/len(qa1tab)/100

aaa2 = sum(qa2tab)/len(qa1tab)/100
bba2 = sum(ra2tab)/len(qa1tab)/100
cca2 = sum(sa2tab)/len(qa1tab)/100
dda2 = sum(ta2tab)/len(qa1tab)/100
eea2 = sum(ua2tab)/len(qa1tab)/100

aaa3 = sum(qa3tab)/len(qa1tab)/100
bba3 = sum(ra3tab)/len(qa1tab)/100
cca3 = sum(sa3tab)/len(qa1tab)/100
dda3 = sum(ta3tab)/len(qa1tab)/100
eea3 = sum(ua3tab)/len(qa1tab)/100

aaa4 = sum(qa4tab)/len(qa1tab)/100
bba4 = sum(ra4tab)/len(qa1tab)/100
cca4 = sum(sa4tab)/len(qa1tab)/100
dda4 = sum(ta4tab)/len(qa1tab)/100
eea4 = sum(ua4tab)/len(qa1tab)/100

aaa5 = sum(qa5tab)/len(qa1tab)/100
bba5 = sum(ra5tab)/len(qa1tab)/100
cca5 = sum(sa5tab)/len(qa1tab)/100
dda5 = sum(ta5tab)/len(qa1tab)/100
eea5 = sum(ua5tab)/len(qa1tab)/100

aaa6 = sum(qa6tab)/len(qa1tab)/100
bba6 = sum(ra6tab)/len(qa1tab)/100
cca6 = sum(sa6tab)/len(qa1tab)/100
dda6 = sum(ta6tab)/len(qa1tab)/100
eea6 = sum(ua6tab)/len(qa1tab)/100

print(aaa1,bba1,cca1,dda1,eea1)
print((aaa1+bba1+cca1+dda1+eea1)/5)
scattertab3.append((aaa1+bba1+cca1+dda1+eea1)/5)

print(aaa2,bba2,cca2,dda2,eea2)
print((aaa2+bba2+cca2+dda2+eea2)/5)
scattertab3.append((aaa2+bba2+cca2+dda2+eea2)/5)

print(aaa3,bba3,cca3,dda3,eea3)
print((aaa3+bba3+cca3+dda3+eea3)/5)
scattertab3.append((aaa3+bba3+cca3+dda3+eea3)/5)

print(aaa4,bba4,cca4,dda4,eea4)
print((aaa4+bba4+cca4+dda4+eea4)/5)
scattertab3.append((aaa4+bba4+cca4+dda4+eea4)/5)

print(aaa5,bba5,cca5,dda5,eea5)
print((aaa5+bba5+cca5+dda5+eea5)/5)
scattertab3.append((aaa5+bba5+cca5+dda5+eea5)/5)

print(aaa6,bba6,cca6,dda6,eea6)
print((aaa6+bba6+cca6+dda6+eea6)/5)
scattertab3.append((aaa6+bba6+cca6+dda6+eea6)/5)

#-----------------------Pilot 4----------------------#
print("Pilot 4")
aa1= u4_C1[:,0]
ba1= u4_C1[:,1]
ca1= u4_C1[:,2]
da1= u4_C1[:,3]
ea1= u4_C1[:,4]

aa2= u4_C2[:,0]
ba2= u4_C2[:,1]
ca2= u4_C2[:,2]
da2= u4_C2[:,3]
ea2= u4_C2[:,4]

aa3= u4_C3[:,0]
ba3= u4_C3[:,1]
ca3= u4_C3[:,2]
da3= u4_C3[:,3]
ea3= u4_C3[:,4]

aa4= u4_C4[:,0]
ba4= u4_C4[:,1]
ca4= u4_C4[:,2]
da4= u4_C4[:,3]
ea4= u4_C4[:,4]

aa5= u4_C5[:,0]
ba5= u4_C5[:,1]
ca5= u4_C5[:,2]
da5= u4_C5[:,3]
ea5= u4_C5[:,4]

aa6= u4_C6[:,0]
ba6= u4_C6[:,1]
ca6= u4_C6[:,2]
da6= u4_C6[:,3]
ea6= u4_C6[:,4]


ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ua11ttab = []
ua12ttab = []
ua13ttab = []
ua14ttab = []
ua15ttab = []

ua21ttab = []
ua22ttab = []
ua23ttab = []
ua24ttab = []
ua25ttab = []

ua31ttab = []
ua32ttab = []
ua33ttab = []
ua34ttab = []
ua35ttab = []

ua41ttab = []
ua42ttab = []
ua43ttab = []
ua44ttab = []
ua45ttab = []

ua51ttab = []
ua52ttab = []
ua53ttab = []
ua54ttab = []
ua55ttab = []

ua61ttab = []
ua62ttab = []
ua63ttab = []
ua64ttab = []
ua65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

#ua11ttab.remove(1523)



qa1tab = []
ra1tab = []
sa1tab = []
ta1tab = []
ua1tab = []

qa2tab = []
ra2tab = []
sa2tab = []
ta2tab = []
ua2tab = []

qa3tab = []
ra3tab = []
sa3tab = []
ta3tab = []
ua3tab = []

qa4tab = []
ra4tab = []
sa4tab = []
ta4tab = []
ua4tab = []

qa5tab = []
ra5tab = []
sa5tab = []
ta5tab = []
ua5tab = []

qa6tab = []
ra6tab = []
sa6tab = []
ta6tab = []
ua6tab = []

for i in range(len(ft1ttab)):
  va1 = abs(ft1ttab[i] - ua11ttab[i])
  wa1 = abs(ft1ttab[i] - ua12ttab[i])
  xa1 = abs(ft1ttab[i] - ua13ttab[i])
  ya1 = abs(ft1ttab[i] - ua14ttab[i])
  za1 = abs(ft1ttab[i] - ua15ttab[i])

  va2 = abs(ft1ttab[i] - ua21ttab[i])
  wa2 = abs(ft1ttab[i] - ua22ttab[i])
  xa2 = abs(ft1ttab[i] - ua23ttab[i])
  ya2 = abs(ft1ttab[i] - ua24ttab[i])
  za2 = abs(ft1ttab[i] - ua25ttab[i])

  va3 = abs(ft1ttab[i] - ua31ttab[i])
  wa3 = abs(ft1ttab[i] - ua32ttab[i])
  xa3 = abs(ft1ttab[i] - ua33ttab[i])
  ya3 = abs(ft1ttab[i] - ua34ttab[i])
  za3 = abs(ft1ttab[i] - ua35ttab[i])

  va4 = abs(ft1ttab[i] - ua41ttab[i])
  wa4 = abs(ft1ttab[i] - ua42ttab[i])
  xa4 = abs(ft1ttab[i] - ua43ttab[i])
  ya4 = abs(ft1ttab[i] - ua44ttab[i])
  za4 = abs(ft1ttab[i] - ua45ttab[i])

  va5 = abs(ft1ttab[i] - ua51ttab[i])
  wa5 = abs(ft1ttab[i] - ua52ttab[i])
  xa5 = abs(ft1ttab[i] - ua53ttab[i])
  ya5 = abs(ft1ttab[i] - ua54ttab[i])
  za5 = abs(ft1ttab[i] - ua55ttab[i])

  va6 = abs(ft1ttab[i] - ua61ttab[i])
  wa6 = abs(ft1ttab[i] - ua62ttab[i])
  xa6 = abs(ft1ttab[i] - ua63ttab[i])
  ya6 = abs(ft1ttab[i] - ua64ttab[i])
  za6 = abs(ft1ttab[i] - ua65ttab[i])

  qa1tab.append(va1)
  ra1tab.append(wa1)
  sa1tab.append(xa1)
  ta1tab.append(ya1)
  ua1tab.append(za1)

  qa2tab.append(va2)
  ra2tab.append(wa2)
  sa2tab.append(xa2)
  ta2tab.append(ya2)
  ua2tab.append(za2)
  
  qa3tab.append(va3)
  ra3tab.append(wa3)
  sa3tab.append(xa3)
  ta3tab.append(ya3)
  ua3tab.append(za3)

  qa4tab.append(va4)
  ra4tab.append(wa4)
  sa4tab.append(xa4)
  ta4tab.append(ya4)
  ua4tab.append(za4)

  qa5tab.append(va5)
  ra5tab.append(wa5)
  sa5tab.append(xa5)
  ta5tab.append(ya5)
  ua5tab.append(za5)

  qa6tab.append(va6)
  ra6tab.append(wa6)
  sa6tab.append(xa6)
  ta6tab.append(ya6)
  ua6tab.append(za6)

aaa1 = sum(qa1tab)/len(qa1tab)/100
bba1 = sum(ra1tab)/len(qa1tab)/100
cca1 = sum(sa1tab)/len(qa1tab)/100
dda1 = sum(ta1tab)/len(qa1tab)/100
eea1 = sum(ua1tab)/len(qa1tab)/100

aaa2 = sum(qa2tab)/len(qa1tab)/100
bba2 = sum(ra2tab)/len(qa1tab)/100
cca2 = sum(sa2tab)/len(qa1tab)/100
dda2 = sum(ta2tab)/len(qa1tab)/100
eea2 = sum(ua2tab)/len(qa1tab)/100

aaa3 = sum(qa3tab)/len(qa1tab)/100
bba3 = sum(ra3tab)/len(qa1tab)/100
cca3 = sum(sa3tab)/len(qa1tab)/100
dda3 = sum(ta3tab)/len(qa1tab)/100
eea3 = sum(ua3tab)/len(qa1tab)/100

aaa4 = sum(qa4tab)/len(qa1tab)/100
bba4 = sum(ra4tab)/len(qa1tab)/100
cca4 = sum(sa4tab)/len(qa1tab)/100
dda4 = sum(ta4tab)/len(qa1tab)/100
eea4 = sum(ua4tab)/len(qa1tab)/100

aaa5 = sum(qa5tab)/len(qa1tab)/100
bba5 = sum(ra5tab)/len(qa1tab)/100
cca5 = sum(sa5tab)/len(qa1tab)/100
dda5 = sum(ta5tab)/len(qa1tab)/100
eea5 = sum(ua5tab)/len(qa1tab)/100

aaa6 = sum(qa6tab)/len(qa1tab)/100
bba6 = sum(ra6tab)/len(qa1tab)/100
cca6 = sum(sa6tab)/len(qa1tab)/100
dda6 = sum(ta6tab)/len(qa1tab)/100
eea6 = sum(ua6tab)/len(qa1tab)/100

print(aaa1,bba1,cca1,dda1,eea1)
print((aaa1+bba1+cca1+dda1+eea1)/5)
scattertab4.append((aaa1+bba1+cca1+dda1+eea1)/5)

print(aaa2,bba2,cca2,dda2,eea2)
print((aaa2+bba2+cca2+dda2+eea2)/5)
scattertab4.append((aaa2+bba2+cca2+dda2+eea2)/5)

print(aaa3,bba3,cca3,dda3,eea3)
print((aaa3+bba3+cca3+dda3+eea3)/5)
scattertab4.append((aaa3+bba3+cca3+dda3+eea3)/5)

print(aaa4,bba4,cca4,dda4,eea4)
print((aaa4+bba4+cca4+dda4+eea4)/5)
scattertab4.append((aaa4+bba4+cca4+dda4+eea4)/5)

print(aaa5,bba5,cca5,dda5,eea5)
print((aaa5+bba5+cca5+dda5+eea5)/5)
scattertab4.append((aaa5+bba5+cca5+dda5+eea5)/5)

print(aaa6,bba6,cca6,dda6,eea6)
print((aaa6+bba6+cca6+dda6+eea6)/5)
scattertab4.append((aaa6+bba6+cca6+dda6+eea6)/5)

#-----------------------Pilot 5----------------------#
print("Pilot 5")
aa1= u5_C1[:,0]
ba1= u5_C1[:,1]
ca1= u5_C1[:,2]
da1= u5_C1[:,3]
ea1= u5_C1[:,4]

aa2= u5_C2[:,0]
ba2= u5_C2[:,1]
ca2= u5_C2[:,2]
da2= u5_C2[:,3]
ea2= u5_C2[:,4]

aa3= u5_C3[:,0]
ba3= u5_C3[:,1]
ca3= u5_C3[:,2]
da3= u5_C3[:,3]
ea3= u5_C3[:,4]

aa4= u5_C4[:,0]
ba4= u5_C4[:,1]
ca4= u5_C4[:,2]
da4= u5_C4[:,3]
ea4= u5_C4[:,4]

aa5= u5_C5[:,0]
ba5= u5_C5[:,1]
ca5= u5_C5[:,2]
da5= u5_C5[:,3]
ea5= u5_C5[:,4]

aa6= u5_C6[:,0]
ba6= u5_C6[:,1]
ca6= u5_C6[:,2]
da6= u5_C6[:,3]
ea6= u5_C6[:,4]


ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ua11ttab = []
ua12ttab = []
ua13ttab = []
ua14ttab = []
ua15ttab = []

ua21ttab = []
ua22ttab = []
ua23ttab = []
ua24ttab = []
ua25ttab = []

ua31ttab = []
ua32ttab = []
ua33ttab = []
ua34ttab = []
ua35ttab = []

ua41ttab = []
ua42ttab = []
ua43ttab = []
ua44ttab = []
ua45ttab = []

ua51ttab = []
ua52ttab = []
ua53ttab = []
ua54ttab = []
ua55ttab = []

ua61ttab = []
ua62ttab = []
ua63ttab = []
ua64ttab = []
ua65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

ua53ttab.remove(2630)
ua14ttab.remove(383)



qa1tab = []
ra1tab = []
sa1tab = []
ta1tab = []
ua1tab = []

qa2tab = []
ra2tab = []
sa2tab = []
ta2tab = []
ua2tab = []

qa3tab = []
ra3tab = []
sa3tab = []
ta3tab = []
ua3tab = []

qa4tab = []
ra4tab = []
sa4tab = []
ta4tab = []
ua4tab = []

qa5tab = []
ra5tab = []
sa5tab = []
ta5tab = []
ua5tab = []

qa6tab = []
ra6tab = []
sa6tab = []
ta6tab = []
ua6tab = []

for i in range(len(ft1ttab)):
  va1 = abs(ft1ttab[i] - ua11ttab[i])
  wa1 = abs(ft1ttab[i] - ua12ttab[i])
  xa1 = abs(ft1ttab[i] - ua13ttab[i])
  ya1 = abs(ft1ttab[i] - ua14ttab[i])
  za1 = abs(ft1ttab[i] - ua15ttab[i])

  va2 = abs(ft1ttab[i] - ua21ttab[i])
  wa2 = abs(ft1ttab[i] - ua22ttab[i])
  xa2 = abs(ft1ttab[i] - ua23ttab[i])
  ya2 = abs(ft1ttab[i] - ua24ttab[i])
  za2 = abs(ft1ttab[i] - ua25ttab[i])

  va3 = abs(ft1ttab[i] - ua31ttab[i])
  wa3 = abs(ft1ttab[i] - ua32ttab[i])
  xa3 = abs(ft1ttab[i] - ua33ttab[i])
  ya3 = abs(ft1ttab[i] - ua34ttab[i])
  za3 = abs(ft1ttab[i] - ua35ttab[i])

  va4 = abs(ft1ttab[i] - ua41ttab[i])
  wa4 = abs(ft1ttab[i] - ua42ttab[i])
  xa4 = abs(ft1ttab[i] - ua43ttab[i])
  ya4 = abs(ft1ttab[i] - ua44ttab[i])
  za4 = abs(ft1ttab[i] - ua45ttab[i])

  va5 = abs(ft1ttab[i] - ua51ttab[i])
  wa5 = abs(ft1ttab[i] - ua52ttab[i])
  xa5 = abs(ft1ttab[i] - ua53ttab[i])
  ya5 = abs(ft1ttab[i] - ua54ttab[i])
  za5 = abs(ft1ttab[i] - ua55ttab[i])

  va6 = abs(ft1ttab[i] - ua61ttab[i])
  wa6 = abs(ft1ttab[i] - ua62ttab[i])
  xa6 = abs(ft1ttab[i] - ua63ttab[i])
  ya6 = abs(ft1ttab[i] - ua64ttab[i])
  za6 = abs(ft1ttab[i] - ua65ttab[i])

  qa1tab.append(va1)
  ra1tab.append(wa1)
  sa1tab.append(xa1)
  ta1tab.append(ya1)
  ua1tab.append(za1)

  qa2tab.append(va2)
  ra2tab.append(wa2)
  sa2tab.append(xa2)
  ta2tab.append(ya2)
  ua2tab.append(za2)
  
  qa3tab.append(va3)
  ra3tab.append(wa3)
  sa3tab.append(xa3)
  ta3tab.append(ya3)
  ua3tab.append(za3)

  qa4tab.append(va4)
  ra4tab.append(wa4)
  sa4tab.append(xa4)
  ta4tab.append(ya4)
  ua4tab.append(za4)

  qa5tab.append(va5)
  ra5tab.append(wa5)
  sa5tab.append(xa5)
  ta5tab.append(ya5)
  ua5tab.append(za5)

  qa6tab.append(va6)
  ra6tab.append(wa6)
  sa6tab.append(xa6)
  ta6tab.append(ya6)
  ua6tab.append(za6)

aaa1 = sum(qa1tab)/len(qa1tab)/100
bba1 = sum(ra1tab)/len(qa1tab)/100
cca1 = sum(sa1tab)/len(qa1tab)/100
dda1 = sum(ta1tab)/len(qa1tab)/100
eea1 = sum(ua1tab)/len(qa1tab)/100

aaa2 = sum(qa2tab)/len(qa1tab)/100
bba2 = sum(ra2tab)/len(qa1tab)/100
cca2 = sum(sa2tab)/len(qa1tab)/100
dda2 = sum(ta2tab)/len(qa1tab)/100
eea2 = sum(ua2tab)/len(qa1tab)/100

aaa3 = sum(qa3tab)/len(qa1tab)/100
bba3 = sum(ra3tab)/len(qa1tab)/100
cca3 = sum(sa3tab)/len(qa1tab)/100
dda3 = sum(ta3tab)/len(qa1tab)/100
eea3 = sum(ua3tab)/len(qa1tab)/100

aaa4 = sum(qa4tab)/len(qa1tab)/100
bba4 = sum(ra4tab)/len(qa1tab)/100
cca4 = sum(sa4tab)/len(qa1tab)/100
dda4 = sum(ta4tab)/len(qa1tab)/100
eea4 = sum(ua4tab)/len(qa1tab)/100

aaa5 = sum(qa5tab)/len(qa1tab)/100
bba5 = sum(ra5tab)/len(qa1tab)/100
cca5 = sum(sa5tab)/len(qa1tab)/100
dda5 = sum(ta5tab)/len(qa1tab)/100
eea5 = sum(ua5tab)/len(qa1tab)/100

aaa6 = sum(qa6tab)/len(qa1tab)/100
bba6 = sum(ra6tab)/len(qa1tab)/100
cca6 = sum(sa6tab)/len(qa1tab)/100
dda6 = sum(ta6tab)/len(qa1tab)/100
eea6 = sum(ua6tab)/len(qa1tab)/100

print(aaa1,bba1,cca1,dda1,eea1)
print((aaa1+bba1+cca1+dda1+eea1)/5)
scattertab5.append((aaa1+bba1+cca1+dda1+eea1)/5)

print(aaa2,bba2,cca2,dda2,eea2)
print((aaa2+bba2+cca2+dda2+eea2)/5)
scattertab5.append((aaa2+bba2+cca2+dda2+eea2)/5)

print(aaa3,bba3,cca3,dda3,eea3)
print((aaa3+bba3+cca3+dda3+eea3)/5)
scattertab5.append((aaa3+bba3+cca3+dda3+eea3)/5)

print(aaa4,bba4,cca4,dda4,eea4)
print((aaa4+bba4+cca4+dda4+eea4)/5)
scattertab5.append((aaa4+bba4+cca4+dda4+eea4)/5)

print(aaa5,bba5,cca5,dda5,eea5)
print((aaa5+bba5+cca5+dda5+eea5)/5)
scattertab5.append((aaa5+bba5+cca5+dda5+eea5)/5)

print(aaa6,bba6,cca6,dda6,eea6)
print((aaa6+bba6+cca6+dda6+eea6)/5)
scattertab5.append((aaa6+bba6+cca6+dda6+eea6)/5)

#-----------------------Pilot 6----------------------#
print("Pilot 6")
aa1= u6_C1[:,0]
ba1= u6_C1[:,1]
ca1= u6_C1[:,2]
da1= u6_C1[:,3]
ea1= u6_C1[:,4]

aa2= u6_C2[:,0]
ba2= u6_C2[:,1]
ca2= u6_C2[:,2]
da2= u6_C2[:,3]
ea2= u6_C2[:,4]

aa3= u6_C3[:,0]
ba3= u6_C3[:,1]
ca3= u6_C3[:,2]
da3= u6_C3[:,3]
ea3= u6_C3[:,4]

aa4= u6_C4[:,0]
ba4= u6_C4[:,1]
ca4= u6_C4[:,2]
da4= u6_C4[:,3]
ea4= u6_C4[:,4]

aa5= u6_C5[:,0]
ba5= u6_C5[:,1]
ca5= u6_C5[:,2]
da5= u6_C5[:,3]
ea5= u6_C5[:,4]

aa6= u6_C6[:,0]
ba6= u6_C6[:,1]
ca6= u6_C6[:,2]
da6= u6_C6[:,3]
ea6= u6_C6[:,4]


ft1ttab = [59,309,577,755,1182,2000,2207,2844,3041,3201,3357,3444,3799,4036,4472,5022,5458,5981,6294,6944,7188,7921]

ftab =    [135,385,643,805,1240,2063,2280,2900,3114,3268,3407,3546,3908,4090,4570,5112,5554,6050,6391,7063,7270,8008]
#gatab =    [117,380,629,823,1226,2045,2246,2887,3074,3271,3416,3472,3884,4110,4523,5104,5499,6066,6357,7016,7246,7985]                                       
#hatab =    [111,375,627,844,1234,2127,2247,2944,3092,3343,3428,3498,3984,4126,4541,5132,5500,6081,6449,7002,7248,7995]
#iatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#jatab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]
#katab =    [115,381,633,843,1220,2084,2251,2917,3091,3267,3434,3499,3887,4149,4550,5136,5552,6081,6427,7041,7269,8001]

ua11ttab = []
ua12ttab = []
ua13ttab = []
ua14ttab = []
ua15ttab = []

ua21ttab = []
ua22ttab = []
ua23ttab = []
ua24ttab = []
ua25ttab = []

ua31ttab = []
ua32ttab = []
ua33ttab = []
ua34ttab = []
ua35ttab = []

ua41ttab = []
ua42ttab = []
ua43ttab = []
ua44ttab = []
ua45ttab = []

ua51ttab = []
ua52ttab = []
ua53ttab = []
ua54ttab = []
ua55ttab = []

ua61ttab = []
ua62ttab = []
ua63ttab = []
ua64ttab = []
ua65ttab = []

for n in range(len(ft1ttab)):

  if ft1ttab[n] == 59 or ft1ttab[n] == 309 or ft1ttab[n] == 2207 or ft1ttab[n] == 2844 or ft1ttab[n] == 3444 or ft1ttab[n] == 4036 or ft1ttab[n] == 5458 or ft1ttab[n] == 7921:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

  if ft1ttab[n] == 577 or ft1ttab[n] == 755 or ft1ttab[n] == 1182 or ft1ttab[n] == 2000 or ft1ttab[n] == 3041 or ft1ttab[n] == 3201 or ft1ttab[n] == 3357 or ft1ttab[n] == 3799 or ft1ttab[n] == 4472 or ft1ttab[n] == 5022 or ft1ttab[n] == 5981 or ft1ttab[n] == 6294 or ft1ttab[n] == 6944 or ft1ttab[n] == 7188:
    k1a = np.min(aa1[ft1ttab[n]:ftab[n]])
    l1a = np.min(ba1[ft1ttab[n]:ftab[n]])
    m1a = np.min(ca1[ft1ttab[n]:ftab[n]])
    o1a = np.min(da1[ft1ttab[n]:ftab[n]])
    p1a = np.min(ea1[ft1ttab[n]:ftab[n]])

    k2a = np.min(aa2[ft1ttab[n]:ftab[n]])
    l2a = np.min(ba2[ft1ttab[n]:ftab[n]])
    m2a = np.min(ca2[ft1ttab[n]:ftab[n]])
    o2a = np.min(da2[ft1ttab[n]:ftab[n]])
    p2a = np.min(ea2[ft1ttab[n]:ftab[n]])

    k3a = np.min(aa3[ft1ttab[n]:ftab[n]])
    l3a = np.min(ba3[ft1ttab[n]:ftab[n]])
    m3a = np.min(ca3[ft1ttab[n]:ftab[n]])
    o3a = np.min(da3[ft1ttab[n]:ftab[n]])
    p3a = np.min(ea3[ft1ttab[n]:ftab[n]])

    k4a = np.min(aa4[ft1ttab[n]:ftab[n]])
    l4a = np.min(ba4[ft1ttab[n]:ftab[n]])
    m4a = np.min(ca4[ft1ttab[n]:ftab[n]])
    o4a = np.min(da4[ft1ttab[n]:ftab[n]])
    p4a = np.min(ea4[ft1ttab[n]:ftab[n]])

    k5a = np.min(aa5[ft1ttab[n]:ftab[n]])
    l5a = np.min(ba5[ft1ttab[n]:ftab[n]])
    m5a = np.min(ca5[ft1ttab[n]:ftab[n]])
    o5a = np.min(da5[ft1ttab[n]:ftab[n]])
    p5a = np.min(ea5[ft1ttab[n]:ftab[n]])

    k6a = np.min(aa6[ft1ttab[n]:ftab[n]])
    l6a = np.min(ba6[ft1ttab[n]:ftab[n]])
    m6a = np.min(ca6[ft1ttab[n]:ftab[n]])
    o6a = np.min(da6[ft1ttab[n]:ftab[n]])
    p6a = np.min(ea6[ft1ttab[n]:ftab[n]])

    kaa = (np.where(aa1 == k1a)[0]).tolist()
    laa = (np.where(ba1 == l1a)[0]).tolist()
    maa = (np.where(ca1 == m1a)[0]).tolist()
    oaa = (np.where(da1 == o1a)[0]).tolist()
    paa = (np.where(ea1 == p1a)[0]).tolist()

    kba = (np.where(aa2 == k2a)[0]).tolist()
    lba = (np.where(ba2 == l2a)[0]).tolist()
    mba = (np.where(ca2 == m2a)[0]).tolist()
    oba = (np.where(da2 == o2a)[0]).tolist()
    pba = (np.where(ea2 == p2a)[0]).tolist()

    kca = (np.where(aa3 == k3a)[0]).tolist()
    lca = (np.where(ba3 == l3a)[0]).tolist()
    mca = (np.where(ca3 == m3a)[0]).tolist()
    oca = (np.where(da3 == o3a)[0]).tolist()
    pca = (np.where(ea3 == p3a)[0]).tolist()

    kda = (np.where(aa4 == k4a)[0]).tolist()
    lda = (np.where(ba4 == l4a)[0]).tolist()
    mda = (np.where(ca4 == m4a)[0]).tolist()
    oda = (np.where(da4 == o4a)[0]).tolist()
    pda = (np.where(ea4 == p4a)[0]).tolist()

    kea = (np.where(aa5 == k5a)[0]).tolist()
    lea = (np.where(ba5 == l5a)[0]).tolist()
    mea = (np.where(ca5 == m5a)[0]).tolist()
    oea = (np.where(da5 == o5a)[0]).tolist()
    pea = (np.where(ea5 == p5a)[0]).tolist()

    kfa = (np.where(aa6 == k6a)[0]).tolist()
    lfa = (np.where(ba6 == l6a)[0]).tolist()
    mfa = (np.where(ca6 == m6a)[0]).tolist()
    ofa = (np.where(da6 == o6a)[0]).tolist()
    pfa = (np.where(ea6 == p6a)[0]).tolist()

    ua11ttab.extend(kaa)
    ua12ttab.extend(laa)
    ua13ttab.extend(maa)
    ua14ttab.extend(oaa)
    ua15ttab.extend(paa)

    ua21ttab.extend(kba)
    ua22ttab.extend(lba)
    ua23ttab.extend(mba)
    ua24ttab.extend(oba)
    ua25ttab.extend(pba)

    ua31ttab.extend(kca)
    ua32ttab.extend(lca)
    ua33ttab.extend(mca)
    ua34ttab.extend(oca)
    ua35ttab.extend(pca)

    ua41ttab.extend(kda)
    ua42ttab.extend(lda)
    ua43ttab.extend(mda)
    ua44ttab.extend(oda)
    ua45ttab.extend(pda)

    ua51ttab.extend(kea)
    ua52ttab.extend(lea)
    ua53ttab.extend(mea)
    ua54ttab.extend(oea)
    ua55ttab.extend(pea)

    ua61ttab.extend(kfa)
    ua62ttab.extend(lfa)
    ua63ttab.extend(mfa)
    ua64ttab.extend(ofa)
    ua65ttab.extend(pfa)

#ua11ttab.remove(1523)


qa1tab = []
ra1tab = []
sa1tab = []
ta1tab = []
ua1tab = []

qa2tab = []
ra2tab = []
sa2tab = []
ta2tab = []
ua2tab = []

qa3tab = []
ra3tab = []
sa3tab = []
ta3tab = []
ua3tab = []

qa4tab = []
ra4tab = []
sa4tab = []
ta4tab = []
ua4tab = []

qa5tab = []
ra5tab = []
sa5tab = []
ta5tab = []
ua5tab = []

qa6tab = []
ra6tab = []
sa6tab = []
ta6tab = []
ua6tab = []

for i in range(len(ft1ttab)):
  va1 = abs(ft1ttab[i] - ua11ttab[i])
  wa1 = abs(ft1ttab[i] - ua12ttab[i])
  xa1 = abs(ft1ttab[i] - ua13ttab[i])
  ya1 = abs(ft1ttab[i] - ua14ttab[i])
  za1 = abs(ft1ttab[i] - ua15ttab[i])

  va2 = abs(ft1ttab[i] - ua21ttab[i])
  wa2 = abs(ft1ttab[i] - ua22ttab[i])
  xa2 = abs(ft1ttab[i] - ua23ttab[i])
  ya2 = abs(ft1ttab[i] - ua24ttab[i])
  za2 = abs(ft1ttab[i] - ua25ttab[i])

  va3 = abs(ft1ttab[i] - ua31ttab[i])
  wa3 = abs(ft1ttab[i] - ua32ttab[i])
  xa3 = abs(ft1ttab[i] - ua33ttab[i])
  ya3 = abs(ft1ttab[i] - ua34ttab[i])
  za3 = abs(ft1ttab[i] - ua35ttab[i])

  va4 = abs(ft1ttab[i] - ua41ttab[i])
  wa4 = abs(ft1ttab[i] - ua42ttab[i])
  xa4 = abs(ft1ttab[i] - ua43ttab[i])
  ya4 = abs(ft1ttab[i] - ua44ttab[i])
  za4 = abs(ft1ttab[i] - ua45ttab[i])

  va5 = abs(ft1ttab[i] - ua51ttab[i])
  wa5 = abs(ft1ttab[i] - ua52ttab[i])
  xa5 = abs(ft1ttab[i] - ua53ttab[i])
  ya5 = abs(ft1ttab[i] - ua54ttab[i])
  za5 = abs(ft1ttab[i] - ua55ttab[i])

  va6 = abs(ft1ttab[i] - ua61ttab[i])
  wa6 = abs(ft1ttab[i] - ua62ttab[i])
  xa6 = abs(ft1ttab[i] - ua63ttab[i])
  ya6 = abs(ft1ttab[i] - ua64ttab[i])
  za6 = abs(ft1ttab[i] - ua65ttab[i])

  qa1tab.append(va1)
  ra1tab.append(wa1)
  sa1tab.append(xa1)
  ta1tab.append(ya1)
  ua1tab.append(za1)

  qa2tab.append(va2)
  ra2tab.append(wa2)
  sa2tab.append(xa2)
  ta2tab.append(ya2)
  ua2tab.append(za2)
  
  qa3tab.append(va3)
  ra3tab.append(wa3)
  sa3tab.append(xa3)
  ta3tab.append(ya3)
  ua3tab.append(za3)

  qa4tab.append(va4)
  ra4tab.append(wa4)
  sa4tab.append(xa4)
  ta4tab.append(ya4)
  ua4tab.append(za4)

  qa5tab.append(va5)
  ra5tab.append(wa5)
  sa5tab.append(xa5)
  ta5tab.append(ya5)
  ua5tab.append(za5)

  qa6tab.append(va6)
  ra6tab.append(wa6)
  sa6tab.append(xa6)
  ta6tab.append(ya6)
  ua6tab.append(za6)

aaa1 = sum(qa1tab)/len(qa1tab)/100
bba1 = sum(ra1tab)/len(qa1tab)/100
cca1 = sum(sa1tab)/len(qa1tab)/100
dda1 = sum(ta1tab)/len(qa1tab)/100
eea1 = sum(ua1tab)/len(qa1tab)/100

aaa2 = sum(qa2tab)/len(qa1tab)/100
bba2 = sum(ra2tab)/len(qa1tab)/100
cca2 = sum(sa2tab)/len(qa1tab)/100
dda2 = sum(ta2tab)/len(qa1tab)/100
eea2 = sum(ua2tab)/len(qa1tab)/100

aaa3 = sum(qa3tab)/len(qa1tab)/100
bba3 = sum(ra3tab)/len(qa1tab)/100
cca3 = sum(sa3tab)/len(qa1tab)/100
dda3 = sum(ta3tab)/len(qa1tab)/100
eea3 = sum(ua3tab)/len(qa1tab)/100

aaa4 = sum(qa4tab)/len(qa1tab)/100
bba4 = sum(ra4tab)/len(qa1tab)/100
cca4 = sum(sa4tab)/len(qa1tab)/100
dda4 = sum(ta4tab)/len(qa1tab)/100
eea4 = sum(ua4tab)/len(qa1tab)/100

aaa5 = sum(qa5tab)/len(qa1tab)/100
bba5 = sum(ra5tab)/len(qa1tab)/100
cca5 = sum(sa5tab)/len(qa1tab)/100
dda5 = sum(ta5tab)/len(qa1tab)/100
eea5 = sum(ua5tab)/len(qa1tab)/100

aaa6 = sum(qa6tab)/len(qa1tab)/100
bba6 = sum(ra6tab)/len(qa1tab)/100
cca6 = sum(sa6tab)/len(qa1tab)/100
dda6 = sum(ta6tab)/len(qa1tab)/100
eea6 = sum(ua6tab)/len(qa1tab)/100

print(aaa1,bba1,cca1,dda1,eea1)
print((aaa1+bba1+cca1+dda1+eea1)/5)
scattertab6.append((aaa1+bba1+cca1+dda1+eea1)/5)

print(aaa2,bba2,cca2,dda2,eea2)
print((aaa2+bba2+cca2+dda2+eea2)/5)
scattertab6.append((aaa2+bba2+cca2+dda2+eea2)/5)

print(aaa3,bba3,cca3,dda3,eea3)
print((aaa3+bba3+cca3+dda3+eea3)/5)
scattertab6.append((aaa3+bba3+cca3+dda3+eea3)/5)

print(aaa4,bba4,cca4,dda4,eea4)
print((aaa4+bba4+cca4+dda4+eea4)/5)
scattertab6.append((aaa4+bba4+cca4+dda4+eea4)/5)

print(aaa5,bba5,cca5,dda5,eea5)
print((aaa5+bba5+cca5+dda5+eea5)/5)
scattertab6.append((aaa5+bba5+cca5+dda5+eea5)/5)

print(aaa6,bba6,cca6,dda6,eea6)
print((aaa6+bba6+cca6+dda6+eea6)/5)
scattertab6.append((aaa6+bba6+cca6+dda6+eea6)/5)

print(scattertab1)
print(scattertab2)
print(scattertab3)
print(scattertab4)
print(scattertab5)
print(scattertab6)
scatterrange = [1,2,3,4,5,6]

fig1 = plt.figure()
bx = fig1.add_subplot(111)
bx.scatter(scatterrange, scattertab1, label = ('pilot 1'))#color='red')
bx.scatter(scatterrange, scattertab2, label = ('pilot 2'))#color='green')
bx.scatter(scatterrange, scattertab3, label = ('pilot 3'))#color='blue')
bx.scatter(scatterrange, scattertab4, label = ('pilot 4'))#color='black')
bx.scatter(scatterrange, scattertab5, label = ('pilot 5'))#color='purple')
bx.scatter(scatterrange, scattertab6, label = ('pilot 6'))#color='orange')
bx.set_xticklabels(['p nm', 'p nm', 'v nm', 'a nm', 'p m', 'v m', 'a m'])
bx.set_title('Avergae Time delay of pilots accros different combinations')
bx.set_xlabel('Combination')
bx.set_ylabel('Time delay [s]')
bx.legend()


boxplttab1 = [scattertab1[0],scattertab2[0],scattertab3[0],scattertab4[0],scattertab5[0],scattertab6[0]]
boxplttab2 = [scattertab1[1],scattertab2[1],scattertab3[1],scattertab4[1],scattertab5[1],scattertab6[1]]
boxplttab3 = [scattertab1[2],scattertab2[2],scattertab3[2],scattertab4[2],scattertab5[2],scattertab6[2]]
boxplttab4 = [scattertab1[3],scattertab2[3],scattertab3[3],scattertab4[3],scattertab5[3],scattertab6[3]]
boxplttab5 = [scattertab1[4],scattertab2[4],scattertab3[4],scattertab4[4],scattertab5[4],scattertab6[4]]
boxplttab6 = [scattertab1[5],scattertab2[5],scattertab3[5],scattertab4[5],scattertab5[5],scattertab6[5]]
finalnmtab = [boxplttab1,boxplttab2,boxplttab3]
finalmtab = [boxplttab4,boxplttab5,boxplttab6]
fig = plt.figure()
ax = fig.add_subplot(111)

boxplot1 = ax.boxplot(finalnmtab, positions = [1,4,7], widths = 0.6, patch_artist=True)
boxplot2 = ax.boxplot(finalmtab, positions = [1.6,4.6,7.6], widths = 0.6, patch_artist=True)

for box in boxplot1['boxes']:
    # change outline color
    box.set(color='black', linewidth=1)
    # change fill color
    box.set(facecolor = 'red' )
    

for box in boxplot2['boxes']:
    box.set(color='black', linewidth=1)
    box.set(facecolor = 'blue' )

ax.legend([boxplot1["boxes"][0], boxplot2["boxes"][0]], ['No motion', 'Motion'], loc='upper right')
ax.set_xlim(0,9)
ax.set_xticklabels(['pos','vel', 'acc'])
ax.set_xticks([1.3,4.3,7.3])
ax.set_title('Average Time delay of pilots accros different combinations')
ax.set_xlabel('Vehicle dynamic')
ax.set_ylabel('Time delay [s]')
print(np.average(boxplttab1))
print(np.average(boxplttab2))
print(np.average(boxplttab3))
print(np.average(boxplttab4))
print(np.average(boxplttab5))
print(np.average(boxplttab6))
plt.show()


<<<<<<< HEAD
"""
=======

<<<<<<< HEAD
#<<<<<<< Updated upstream
=======
>>>>>>> ac5b7a6feddf200a261bf29207f5e30750184b21
<<<<<<< Updated upstream
>>>>>>> 21fad8dcdac6808b8dc7fd00bd96b875042a23b6

#=======
#>>>>>>> Stashed changes
# =============================================================================
# Statistics
# =============================================================================

TD_pos_nm = np.array(boxplttab1)
TD_pos_m  = np.array(boxplttab2)
TD_vel_nm = np.array(boxplttab3)
TD_vel_m  = np.array(boxplttab4)
TD_acc_nm = np.array(boxplttab5)
TD_acc_m  = np.array(boxplttab6)

ttest_TD_pos=ttest_ind(TD_pos_nm, TD_pos_m)
ttest_TD_vel=ttest_ind(TD_vel_nm, TD_vel_m)
ttest_TD_acc=ttest_ind(TD_acc_nm, TD_acc_m)

t_value_TD_pos    =ttest_TD_pos[0]
p_value_TD_pos    =ttest_TD_pos[1]
deg_freedom_TD_pos=ttest_TD_pos[2]

t_value_TD_vel    =ttest_TD_vel[0]
p_value_TD_vel    =ttest_TD_vel[1]
deg_freedom_TD_vel=ttest_TD_vel[2]

t_value_TD_acc    =ttest_TD_acc[0]
p_value_TD_acc    =ttest_TD_acc[1]
deg_freedom_TD_acc=ttest_TD_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, time delay***')
print('t_value=',round(t_value_TD_pos,3), ',',  round(t_value_TD_vel,3), ',',  round(t_value_TD_acc,3))
print('p_value=',round(p_value_TD_pos,3), ',',  round(p_value_TD_vel,3), ',',  round(p_value_TD_acc,3))
print('degrees of freedom:',deg_freedom_TD_pos)
#<<<<<<< Updated upstream
print('')
#=======
print('')
<<<<<<< HEAD
#>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
<<<<<<< HEAD

=======
>>>>>>> ac5b7a6feddf200a261bf29207f5e30750184b21
"""
>>>>>>> 21fad8dcdac6808b8dc7fd00bd96b875042a23b6
