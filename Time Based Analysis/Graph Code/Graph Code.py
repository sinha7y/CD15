import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
from scipy.signal import correlate


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
"""
# Target forcing function as a function of time
#plt.subplot(121)
plt.plot(t,ft1_C1,5)
plt.title('Target forcing function; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

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
"""
# Human operator control input as a function of time
plt.subplot(121)
plt.plot(t, u1_C2)
plt.plot(t, ft1_C2)
plt.title('Human input; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')

"""
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

"""

samples = 4096
length = int(len(ft1_C2))

n = length/samples
ttab = []
slopetab = []
averagetab = []
ytab = []

for i in range(0, length, int(n)):
    x = ft1_C2[int(i):int(i) + int(n)]
    y = t[int(i):int(i) + int(n)]
    z = e1_C2[int(i):int(i) + int(n)]

    slope = (x[-1]-x[0])/(y[-1]-y[0])
    slopetab.append(slope)

    average_error = sum(z)/int(n)

    averagetab.append(average_error)

    time_delay = abs(average_error)/abs(slope)

    ttab.append(time_delay)
    p = time_delay/1000
    ytab.extend(p for r in range(2))

average_time_delay = (sum(ytab)/81.92)
print(average_time_delay)
plt.subplot(122)    
plt.plot(t, ytab)
plt.show()


#>>>>>>> 0d82b29d03f8d470977ac863dbfac941c2cecbd9

