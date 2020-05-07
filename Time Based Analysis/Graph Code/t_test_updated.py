#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:27:25 2020

@author: Lasse
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath
import statistics as st
import scipy.stats as stats
from statsmodels.stats.weightstats import ttest_ind

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

#-----------------------------------Subject 3----------------------------------------

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


# ---------------------------- Mean --------------------------------
# -------------------------- Subject 1 -----------------------------
# ------------------- Error as function of time --------------------

e1_C1_mean = np.mean(e1_C1, axis=1)
e1_C4_mean = np.mean(e1_C4, axis=1)
#std_e1_C1 = st.variance(e1_C1[:,0])
#var_e1_C1 = np.var(e1_C1, axis=1)
#var_e1_C4 = np.var(e1_C4, axis=1)

#t = list(range(8192))
#T_value = (e1_C1_mean-e1_C4_mean)/(((5-1)*var_e1_C1**2+(5-1)*var_e1_C4**2)/8*np.sqrt(1/5+1/5))
#plt.plot(t, abs(T_value), 'o')
#plt.axhline(y=2.145,color='k')
#plt.show()

#print(T_value)




t = list(range(8192))

#plt.plot(t, e1_C1_mean, e1_C4_mean)
#plt.title('Error signal; position control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e1_C2_mean = np.mean(e1_C2, axis=1)
e1_C5_mean = np.mean(e1_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e1_C2_mean, e1_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e1_C3_mean = np.mean(e1_C3, axis=1)
e1_C6_mean = np.mean(e1_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e1_C3_mean, e1_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u1_C1_mean = np.mean(u1_C1, axis=1)
u1_C4_mean = np.mean(u1_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u1_C1_mean, u1_C4_mean)
#plt.title('Human input; position control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u1_C2_mean = np.mean(u1_C2, axis=1)
u1_C5_mean = np.mean(u1_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u1_C2_mean, u1_C5_mean)
#plt.title('Human input; velocity control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u1_C3_mean = np.mean(u1_C3, axis=1)
u1_C6_mean = np.mean(u1_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u1_C3_mean, u1_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 1')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x1_C1_mean = np.mean(x1_C1, axis=1)
x1_C4_mean = np.mean(x1_C4, axis=1)
t = list(range(8192))

plt.plot(t, x1_C1_mean, x1_C4_mean)
plt.plot(t, ft1_C1)
plt.title('Pitch input; position control; mean; subject 1')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

x1_C2_mean = np.mean(x1_C2, axis=1)
x1_C5_mean = np.mean(x1_C5, axis=1)
t = list(range(8192))

plt.plot(t, x1_C2_mean, x1_C5_mean)
plt.plot(t, ft1_C2)
plt.title('Pitch input; velocity control; mean; subject 1')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()


x1_C3_mean = np.mean(x1_C3, axis=1)
x1_C6_mean = np.mean(x1_C6, axis=1)
t = list(range(8192))

plt.plot(t, x1_C3_mean, x1_C6_mean)
plt.plot(t, ft1_C3)
plt.title('Pitch input; acceleration control; mean; subject 1')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^2]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

var_x1_C3 = np.var(x1_C3, axis=1)
var_x1_C6 = np.var(x1_C6, axis=1)
t = list(range(8192))
T_value = (x1_C3_mean-x1_C6_mean)/(((5-1)*var_x1_C3**2+(5-1)*var_x1_C6**2)/8*np.sqrt(1/5+1/5))
#plt.plot(t, (T_value), 'o')
#plt.axhline(y=2.145,color='k')
#plt.axhline(y=-2.145,color='k')
#plt.show()

T_mean = np.mean(abs(T_value))
#print(T_mean)

ttest1=ttest_ind(x1_C3_mean, x1_C6_mean)

t_value1=ttest1[0]
p_value1=ttest1[1]
deg_freedom1=ttest1[2]

print('***subject 1, situation 3***')
print('')
print('t_value=',t_value1)
print('p_value=',p_value1)
print('degrees of freedom:',deg_freedom1)
print('')



# -------------------------- Subject 2 -----------------------------
# ------------------- Error as function of time --------------------

e2_C1_mean = np.mean(e2_C1, axis=1)
e2_C4_mean = np.mean(e2_C4, axis=1)
#std_e2_C1 = st.variance(e2_C1[:,0])
t = list(range(8192))

#plt.plot(t, e2_C1_mean, e2_C4_mean)
#plt.title('Error signal; position control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e2_C2_mean = np.mean(e2_C2, axis=1)
e2_C5_mean = np.mean(e2_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e2_C2_mean, e2_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e2_C3_mean = np.mean(e2_C3, axis=1)
e2_C6_mean = np.mean(e2_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e2_C3_mean, e2_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u2_C1_mean = np.mean(u2_C1, axis=1)
u2_C4_mean = np.mean(u2_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u2_C1_mean, u2_C4_mean)
#plt.title('Human input; position control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u2_C2_mean = np.mean(u2_C2, axis=1)
u2_C5_mean = np.mean(u2_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u2_C2_mean, u2_C5_mean)
#plt.title('Human input; velocity control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u2_C3_mean = np.mean(u2_C3, axis=1)
u2_C6_mean = np.mean(u2_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u2_C3_mean, u2_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 2')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x2_C1_mean = np.mean(x2_C1, axis=1)
x2_C4_mean = np.mean(x2_C4, axis=1)
t = list(range(8192))

plt.plot(t, x2_C1_mean, x2_C4_mean)
plt.plot(t, ft2_C1)
plt.title('Pitch input; position control; mean; subject 2')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

x2_C2_mean = np.mean(x2_C2, axis=1)
x2_C5_mean = np.mean(x2_C5, axis=1)
t = list(range(8192))

plt.plot(t, x2_C2_mean, x2_C5_mean)
plt.plot(t, ft2_C2)
plt.title('Pitch input; velocity control; mean; subject 2')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

ttest2=ttest_ind(x2_C2_mean, x2_C5_mean)

t_value2=ttest2[0]
p_value2=ttest2[1]
deg_freedom2=ttest2[2]

print('***subject 2, situation 2***')
print('')
print('t_value=',t_value2)
print('p_value=',p_value2)
print('degrees of freedom:',deg_freedom2)
print('')


x2_C3_mean = np.mean(x2_C3, axis=1)
x2_C6_mean = np.mean(x2_C6, axis=1)
t = list(range(8192))

plt.plot(t, x2_C3_mean, x2_C6_mean)
plt.plot(t, ft2_C3)
plt.title('Pitch input; acceleration control; mean; subject 2')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^3]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

ttest3=ttest_ind(x2_C3_mean, x2_C6_mean)

t_value3=ttest3[0]
p_value3=ttest3[1]
deg_freedom3=ttest3[2]

print('***subject 2, situation 3***')
print('')
print('t_value=',t_value3)
print('p_value=',p_value3)
print('degrees of freedom:',deg_freedom3)
print('')

# -------------------------- Subject 3 -----------------------------
# ------------------- Error as function of time --------------------

e3_C1_mean = np.mean(e3_C1, axis=1)
e3_C4_mean = np.mean(e3_C4, axis=1)
#std_e2_C1 = st.variance(e2_C1[:,0])
t = list(range(8192))

#plt.plot(t, e3_C1_mean, e3_C4_mean)
#plt.title('Error signal; position control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e3_C2_mean = np.mean(e3_C2, axis=1)
e3_C5_mean = np.mean(e3_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e3_C2_mean, e3_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e3_C3_mean = np.mean(e3_C3, axis=1)
e3_C6_mean = np.mean(e3_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e3_C3_mean, e3_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u3_C1_mean = np.mean(u3_C1, axis=1)
u3_C4_mean = np.mean(u3_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u3_C1_mean, u3_C4_mean)
#plt.title('Human input; position control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u3_C2_mean = np.mean(u3_C2, axis=1)
u3_C5_mean = np.mean(u3_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u3_C2_mean, u3_C5_mean)
#plt.title('Human input; velocity control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u3_C3_mean = np.mean(u3_C3, axis=1)
u3_C6_mean = np.mean(u3_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u3_C3_mean, u3_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 3')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x3_C1_mean = np.mean(x3_C1, axis=1)
x3_C4_mean = np.mean(x3_C4, axis=1)
t = list(range(8192))

plt.plot(t, x3_C1_mean, x3_C4_mean)
plt.plot(t, ft3_C1)
plt.title('Pitch input; position control; mean; subject 3')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

x3_C2_mean = np.mean(x3_C2, axis=1)
x3_C5_mean = np.mean(x3_C5, axis=1)
t = list(range(8192))

plt.plot(t, x3_C2_mean, x3_C5_mean)
plt.plot(t, ft3_C2)
plt.title('Pitch input; velocity control; mean; subject 3')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()


x3_C3_mean = np.mean(x3_C3, axis=1)
x3_C6_mean = np.mean(x3_C6, axis=1)
t = list(range(8192))

plt.plot(t, x3_C3_mean, x3_C6_mean)
plt.plot(t, ft3_C3)
plt.title('Pitch input; acceleration control; mean; subject 3')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^2]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()



# -------------------------- Subject 4 -----------------------------
# ------------------- Error as function of time --------------------

e4_C1_mean = np.mean(e4_C1, axis=1)
e4_C4_mean = np.mean(e4_C4, axis=1)
#std_e2_C1 = st.variance(e2_C1[:,0])
t = list(range(8192))

#plt.plot(t, e4_C1_mean, e4_C4_mean)
#plt.title('Error signal; position control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e4_C2_mean = np.mean(e4_C2, axis=1)
e4_C5_mean = np.mean(e4_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e4_C2_mean, e4_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e4_C3_mean = np.mean(e4_C3, axis=1)
e4_C6_mean = np.mean(e4_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e4_C3_mean, e4_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u4_C1_mean = np.mean(u4_C1, axis=1)
u4_C4_mean = np.mean(u4_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u4_C1_mean, u4_C4_mean)
#plt.title('Human input; position control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u4_C2_mean = np.mean(u4_C2, axis=1)
u4_C5_mean = np.mean(u4_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u4_C2_mean, u4_C5_mean)
#plt.title('Human input; velocity control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u4_C3_mean = np.mean(u4_C3, axis=1)
u4_C6_mean = np.mean(u4_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u4_C3_mean, u4_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 4')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x4_C1_mean = np.mean(x4_C1, axis=1)
x4_C4_mean = np.mean(x4_C4, axis=1)
t = list(range(8192))

plt.plot(t, x4_C1_mean, x4_C4_mean)
plt.plot(t, ft4_C1)
plt.title('Pitch input; position control; mean; subject 4')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

x4_C2_mean = np.mean(x4_C2, axis=1)
x4_C5_mean = np.mean(x4_C5, axis=1)
t = list(range(8192))

plt.plot(t, x4_C2_mean, x4_C5_mean)
plt.plot(t, ft4_C2)
plt.title('Pitch input; velocity control; mean; subject 4')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()


x4_C3_mean = np.mean(x4_C3, axis=1)
x4_C6_mean = np.mean(x4_C6, axis=1)
t = list(range(8192))

plt.plot(t, x4_C3_mean, x4_C6_mean)
plt.plot(t, ft4_C3)
plt.title('Pitch input; acceleration control; mean; subject 4')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^2]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()



# -------------------------- Subject 5 -----------------------------
# ------------------- Error as function of time --------------------

e5_C1_mean = np.mean(e5_C1, axis=1)
e5_C4_mean = np.mean(e5_C4, axis=1)
#std_e2_C1 = st.variance(e2_C1[:,0])
t = list(range(8192))

#plt.plot(t, e5_C1_mean, e5_C4_mean)
#plt.title('Error signal; position control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e5_C2_mean = np.mean(e5_C2, axis=1)
e5_C5_mean = np.mean(e5_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e5_C2_mean, e5_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e5_C3_mean = np.mean(e5_C3, axis=1)
e5_C6_mean = np.mean(e5_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e5_C3_mean, e5_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u5_C1_mean = np.mean(u5_C1, axis=1)
u5_C4_mean = np.mean(u5_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u5_C1_mean, u5_C4_mean)
#plt.title('Human input; position control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u5_C2_mean = np.mean(u5_C2, axis=1)
u5_C5_mean = np.mean(u5_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u5_C2_mean, u5_C5_mean)
#plt.title('Human input; velocity control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u5_C3_mean = np.mean(u5_C3, axis=1)
u5_C6_mean = np.mean(u5_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u5_C3_mean, u5_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 5')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x5_C1_mean = np.mean(x5_C1, axis=1)
x5_C4_mean = np.mean(x5_C4, axis=1)
t = list(range(8192))

plt.plot(t, x5_C1_mean, x5_C4_mean)
plt.plot(t, ft5_C1)
plt.title('Pitch input; position control; mean; subject 5')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

x5_C2_mean = np.mean(x5_C2, axis=1)
x5_C5_mean = np.mean(x5_C5, axis=1)
t = list(range(8192))

plt.plot(t, x5_C2_mean, x5_C5_mean)
plt.plot(t, ft5_C2)
plt.title('Pitch input; velocity control; mean; subject 5')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()


x5_C3_mean = np.mean(x5_C3, axis=1)
x5_C6_mean = np.mean(x5_C6, axis=1)
t = list(range(8192))

plt.plot(t, x5_C3_mean, x5_C6_mean)
plt.plot(t, ft5_C3)
plt.title('Pitch input; acceleration control; mean; subject 5')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^2]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()


# -------------------------- Subject 6 -----------------------------
# ------------------- Error as function of time --------------------

e6_C1_mean = np.mean(e6_C1, axis=1)
e6_C4_mean = np.mean(e6_C4, axis=1)
#std_e2_C1 = st.variance(e2_C1[:,0])
t = list(range(8192))

#plt.plot(t, e6_C1_mean, e6_C4_mean)
#plt.title('Error signal; position control; mean; subject 6')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()

e6_C2_mean = np.mean(e6_C2, axis=1)
e6_C5_mean = np.mean(e6_C5, axis=1)
t = list(range(8192))

#plt.plot(t, e6_C2_mean, e6_C5_mean)
#plt.title('Error signal; velocity control; mean; subject 6')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


e6_C3_mean = np.mean(e6_C3, axis=1)
e6_C6_mean = np.mean(e6_C6, axis=1)
t = list(range(8192))

#plt.plot(t, e6_C3_mean, e6_C6_mean)
#plt.title('Error signal; acceleration control; mean; subject 6')
#plt.xlabel("t[s]")
#plt.ylabel("e[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Human input ---------------------------
u6_C1_mean = np.mean(u6_C1, axis=1)
u6_C4_mean = np.mean(u6_C4, axis=1)
t = list(range(8192))

#plt.plot(t, u6_C1_mean, u6_C4_mean)
#plt.title('Human input; position control; mean; subject 6')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u6_C2_mean = np.mean(u6_C2, axis=1)
u6_C5_mean = np.mean(u6_C5, axis=1)
t = list(range(8192))

#plt.plot(t, u6_C2_mean, u6_C5_mean)
#plt.title('Human input; velocity control; mean; subject 6')
#plt.xlabel("t[s]"
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


u6_C3_mean = np.mean(u6_C3, axis=1)
u6_C6_mean = np.mean(u6_C6, axis=1)
t = list(range(8192))

#plt.plot(t, u6_C3_mean, u6_C6_mean)
#plt.title('Human input; acceleration control; mean; subject 6')
#plt.xlabel("t[s]")
#plt.ylabel("u[-]")
#plt.legend(('NM', 'M'), loc='upper right')
#plt.show()


# ------------------------- Pitch input ---------------------------
x6_C1_mean = np.mean(x6_C1, axis=1)
x6_C4_mean = np.mean(x6_C4, axis=1)
t = list(range(8192))

plt.plot(t, x6_C1_mean, x6_C4_mean)
plt.plot(t, ft6_C1)
plt.title('Pitch input; position control; mean; subject 6')
plt.xlabel("t[s]")
plt.ylabel("x[deg]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

ttest_x6_pos=ttest_ind(x6_C1_mean, x6_C4_mean)

t_value_x6_1=ttest_x6_pos[0]
p_value_x6_1=ttest_x6_pos[1]
deg_freedom_x6_1=ttest_x6_pos[2]

print('***subject 6, situation 1***')
print('')
print('t_value=',t_value_x6_1)
print('p_value=',p_value_x6_1)
print('degrees of freedom:',deg_freedom_x6_1)
print('')


x6_C2_mean = np.mean(x6_C2, axis=1)
x6_C5_mean = np.mean(x6_C5, axis=1)
t = list(range(8192))

plt.plot(t, x6_C2_mean, x6_C5_mean)
plt.plot(t, ft6_C2)
plt.title('Pitch input; velocity control; mean; subject 6')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

ttest_x6_vel=ttest_ind(x6_C2_mean, x6_C5_mean)

t_value_x6_2=ttest_x6_vel[0]
p_value_x6_2=ttest_x6_vel[1]
deg_freedom_x6_2=ttest_x6_vel[2]

print('***subject 6, situation 2***')
print('')
print('t_value=',t_value_x6_2)
print('p_value=',p_value_x6_2)
print('degrees of freedom:',deg_freedom_x6_2)
print('')


x6_C3_mean = np.mean(x6_C3, axis=1)
x6_C6_mean = np.mean(x6_C6, axis=1)
t = list(range(8192))

plt.plot(t, x6_C3_mean, x6_C6_mean)
plt.plot(t, ft6_C3)
plt.title('Pitch input; acceleration control; mean; subject 6')
plt.xlabel("t[s]")
plt.ylabel("x[deg/s^2]")
plt.legend(('NM', 'M', 'Target'), loc='upper right')
plt.show()

ttest_x6_acc=ttest_ind(x6_C3_mean, x6_C6_mean)

t_value_x6_3=ttest_x6_acc[0]
p_value_x6_3=ttest_x6_acc[1]
deg_freedom_x6_3=ttest_x6_acc[2]

print('***subject 6, situation 3***')
print('')
print('t_value=',t_value_x6_3)
print('p_value=',p_value_x6_3)
print('degrees of freedom:',deg_freedom_x6_3)
print('')

# ---------------------------- ANOVA --------------------------------


# Keeping only those where (p-value < 95%)
print('-----------------------  x   -------------------------')
#print('***subject 1, statistical difference between runs x1_C1***')
#print(stats.f_oneway(x1_C1[0,:], x1_C1[1,:], x1_C1[2,:], x1_C1[3,:], x1_C1[4,:]))
#print('***subject 2, statistical difference between runs x2_C1***')
#print(stats.f_oneway(x2_C1[0,:], x2_C1[1,:], x2_C1[2,:], x2_C1[3,:], x2_C1[4,:]))
#print('***subject 3, statistical difference between runs x3_C1***')
#print(stats.f_oneway(x3_C1[0,:], x3_C1[1,:], x3_C1[2,:], x3_C1[3,:], x3_C1[4,:]))
#print('***subject 4, statistical difference between runs x4_C1***')
#print(stats.f_oneway(x4_C1[0,:], x4_C1[1,:], x4_C1[2,:], x4_C1[3,:], x4_C1[4,:]))
#print('***subject 5, statistical difference between runs x5_C1***')
#print(stats.f_oneway(x5_C1[0,:], x5_C1[1,:], x5_C1[2,:], x5_C1[3,:], x5_C1[4,:]))
#print('***subject 6, statistical difference between runs x6_C1***')
#print(stats.f_oneway(x6_C1[0,:], x6_C1[1,:], x6_C1[2,:], x6_C1[3,:], x6_C1[4,:]))

#print('***subject 1, statistical difference between runs x1_C2***')
#print(stats.f_oneway(x1_C2[0,:], x1_C2[1,:], x1_C2[2,:], x1_C2[3,:], x1_C2[4,:]))
#print('***subject 2, statistical difference between runs x2_C2***')
#print(stats.f_oneway(x2_C2[0,:], x2_C2[1,:], x2_C2[2,:], x2_C2[3,:], x2_C2[4,:]))
#print('***subject 3, statistical difference between runs x3_C2***')
#print(stats.f_oneway(x3_C2[0,:], x3_C2[1,:], x3_C2[2,:], x3_C2[3,:], x3_C2[4,:]))
#print('***subject 4, statistical difference between runs x4_C2***')
#print(stats.f_oneway(x4_C2[0,:], x4_C2[1,:], x4_C2[2,:], x4_C2[3,:], x4_C2[4,:]))
#print('***subject 5, statistical difference between runs x5_C2***')
#print(stats.f_oneway(x5_C2[0,:], x5_C2[1,:], x5_C2[2,:], x5_C2[3,:], x5_C2[4,:]))
#print('***subject 6, statistical difference between runs x6_C2***')
#print(stats.f_oneway(x6_C2[0,:], x6_C2[1,:], x6_C2[2,:], x6_C2[3,:], x6_C2[4,:]))

#print('***subject 1, statistical difference between runs x1_C3***')
#print(stats.f_oneway(x1_C3[0,:], x1_C3[1,:], x1_C3[2,:], x1_C3[3,:], x1_C3[4,:]))
#print('***subject 2, statistical difference between runs x2_C3***')
#print(stats.f_oneway(x2_C3[0,:], x2_C3[1,:], x2_C3[2,:], x2_C3[3,:], x2_C3[4,:]))
#print('***subject 3, statistical difference between runs x3_C3***')
#print(stats.f_oneway(x3_C3[0,:], x3_C3[1,:], x3_C3[2,:], x3_C3[3,:], x3_C3[4,:]))
#print('***subject 4, statistical difference between runs x4_C3***')
#print(stats.f_oneway(x4_C3[0,:], x4_C3[1,:], x4_C3[2,:], x4_C3[3,:], x4_C3[4,:]))
#print('***subject 5, statistical difference between runs x5_C3***')
#print(stats.f_oneway(x5_C3[0,:], x5_C3[1,:], x5_C3[2,:], x5_C3[3,:], x5_C3[4,:]))
#print('***subject 6, statistical difference between runs x6_C3***')
#print(stats.f_oneway(x6_C3[0,:], x6_C3[1,:], x6_C3[2,:], x6_C3[3,:], x6_C3[4,:]))
#
#print('***subject 1, statistical difference between runs x1_C4***')
#print(stats.f_oneway(x1_C4[0,:], x1_C4[1,:], x1_C4[2,:], x1_C4[3,:], x1_C4[4,:]))
#print('***subject 2, statistical difference between runs x2_C4***')
#print(stats.f_oneway(x2_C4[0,:], x2_C4[1,:], x2_C4[2,:], x2_C4[3,:], x2_C4[4,:]))
#print('***subject 3, statistical difference between runs x3_C4***')
#print(stats.f_oneway(x3_C4[0,:], x3_C4[1,:], x3_C4[2,:], x3_C4[3,:], x3_C4[4,:]))
#print('***subject 4, statistical difference between runs x4_C4***')
#print(stats.f_oneway(x4_C4[0,:], x4_C4[1,:], x4_C4[2,:], x4_C4[3,:], x4_C4[4,:]))
#print('***subject 5, statistical difference between runs x5_C4***')
#print(stats.f_oneway(x5_C4[0,:], x5_C4[1,:], x5_C4[2,:], x5_C4[3,:], x5_C4[4,:]))
#print('***subject 6, statistical difference between runs x6_C4***')
#print(stats.f_oneway(x6_C4[0,:], x6_C4[1,:], x6_C4[2,:], x6_C4[3,:], x6_C4[4,:]))
#
#print('***subject 1, statistical difference between runs x1_C5***')
#print(stats.f_oneway(x1_C5[0,:], x1_C5[1,:], x1_C5[2,:], x1_C5[3,:], x1_C5[4,:]))
#print('***subject 2, statistical difference between runs x2_C5***')
#print(stats.f_oneway(x2_C5[0,:], x2_C5[1,:], x2_C5[2,:], x2_C5[3,:], x2_C5[4,:]))
#print('***subject 3, statistical difference between runs x3_C5***')
#print(stats.f_oneway(x3_C5[0,:], x3_C5[1,:], x3_C5[2,:], x3_C5[3,:], x3_C5[4,:]))
#print('***subject 4, statistical difference between runs x4_C5***')
#print(stats.f_oneway(x4_C5[0,:], x4_C5[1,:], x4_C5[2,:], x4_C5[3,:], x4_C5[4,:]))
#print('***subject 5, statistical difference between runs x5_C5***')
#print(stats.f_oneway(x5_C5[0,:], x5_C5[1,:], x5_C5[2,:], x5_C5[3,:], x5_C5[4,:]))
#print('***subject 6, statistical difference between runs x6_C5***')
#print(stats.f_oneway(x6_C5[0,:], x6_C5[1,:], x6_C5[2,:], x6_C5[3,:], x6_C5[4,:]))

print('-----------------------  u   -------------------------')
#print('***subject 1, statistical difference between runs u1_C1***')
#print(stats.f_oneway(u1_C1[0,:], u1_C1[1,:], u1_C1[2,:], u1_C1[3,:], u1_C1[4,:]))
#print('***subject 2, statistical difference between runs u2_C1***')
#print(stats.f_oneway(u2_C1[0,:], u2_C1[1,:], u2_C1[2,:], u2_C1[3,:], u2_C1[4,:]))
#print('***subject 3, statistical difference between runs u3_C1***')
#print(stats.f_oneway(u3_C1[0,:], u3_C1[1,:], u3_C1[2,:], u3_C1[3,:], u3_C1[4,:]))
print('***subject 4, statistical difference between runs u4_C1***')
print(stats.f_oneway(u4_C1[0,:], u4_C1[1,:], u4_C1[2,:], u4_C1[3,:], u4_C1[4,:]))
print('***subject 5, statistical difference between runs u5_C1***')
print(stats.f_oneway(u5_C1[0,:], u5_C1[1,:], u5_C1[2,:], u5_C1[3,:], u5_C1[4,:]))
#print('***subject 6, statistical difference between runs u6_C1***')
#print(stats.f_oneway(u6_C1[0,:], u6_C1[1,:], u6_C1[2,:], u6_C1[3,:], u6_C1[4,:]))

#print('***subject 1, statistical difference between runs u1_C2***')
#print(stats.f_oneway(u1_C2[0,:], u1_C2[1,:], u1_C2[2,:], u1_C2[3,:], u1_C2[4,:]))
print('***subject 2, statistical difference between runs u2_C2***')
print(stats.f_oneway(u2_C2[0,:], u2_C2[1,:], u2_C2[2,:], u2_C2[3,:], u2_C2[4,:]))
#print('***subject 3, statistical difference between runs u3_C2***')
#print(stats.f_oneway(u3_C2[0,:], u3_C2[1,:], u3_C2[2,:], u3_C2[3,:], u3_C2[4,:]))
print('***subject 4, statistical difference between runs u4_C2***')
print(stats.f_oneway(u4_C2[0,:], u4_C2[1,:], u4_C2[2,:], u4_C2[3,:], u4_C2[4,:]))
print('***subject 5, statistical difference between runs u5_C2***')
print(stats.f_oneway(u5_C2[0,:], u5_C2[1,:], u5_C2[2,:], u5_C2[3,:], u5_C2[4,:]))
#print('***subject 6, statistical difference between runs u6_C2***')
#print(stats.f_oneway(u6_C2[0,:], u6_C2[1,:], u6_C2[2,:], u6_C2[3,:], u6_C2[4,:]))

#print('***subject 1, statistical difference between runs u1_C3***')
#print(stats.f_oneway(u1_C3[0,:], u1_C3[1,:], u1_C3[2,:], u1_C3[3,:], u1_C3[4,:]))
#print('***subject 2, statistical difference between runs u2_C3***')
#print(stats.f_oneway(u2_C3[0,:], u2_C3[1,:], u2_C3[2,:], u2_C3[3,:], u2_C3[4,:]))
#print('***subject 3, statistical difference between runs u3_C3***')
#print(stats.f_oneway(u3_C3[0,:], u3_C3[1,:], u3_C3[2,:], u3_C3[3,:], u3_C3[4,:]))
print('***subject 4, statistical difference between runs u4_C3***')
print(stats.f_oneway(u4_C3[0,:], u4_C3[1,:], u4_C3[2,:], u4_C3[3,:], u4_C3[4,:]))
#print('***subject 5, statistical difference between runs u5_C3***')
#print(stats.f_oneway(u5_C3[0,:], u5_C3[1,:], u5_C3[2,:], u5_C3[3,:], u5_C3[4,:]))
print('***subject 6, statistical difference between runs u6_C3***')
print(stats.f_oneway(u6_C3[0,:], u6_C3[1,:], u6_C3[2,:], u6_C3[3,:], u6_C3[4,:]))

print('***subject 1, statistical difference between runs u1_C4***')
print(stats.f_oneway(u1_C4[0,:], u1_C4[1,:], u1_C4[2,:], u1_C4[3,:], u1_C4[4,:]))
#print('***subject 2, statistical difference between runs u2_C4***')
#print(stats.f_oneway(u2_C4[0,:], u2_C4[1,:], u2_C4[2,:], u2_C4[3,:], u2_C4[4,:]))
#print('***subject 3, statistical difference between runs u3_C4***')
#print(stats.f_oneway(u3_C4[0,:], u3_C4[1,:], u3_C4[2,:], u3_C4[3,:], u3_C4[4,:]))
print('***subject 4, statistical difference between runs u4_C4***')
print(stats.f_oneway(u4_C4[0,:], u4_C4[1,:], u4_C4[2,:], u4_C4[3,:], u4_C4[4,:]))
#print('***subject 5, statistical difference between runs u5_C4***')
#print(stats.f_oneway(u5_C4[0,:], u5_C4[1,:], u5_C4[2,:], u5_C4[3,:], u5_C4[4,:]))
#print('***subject 6, statistical difference between runs u6_C4***')
#print(stats.f_oneway(u6_C4[0,:], u6_C4[1,:], u6_C4[2,:], u6_C4[3,:], u6_C4[4,:]))

print('***subject 1, statistical difference between runs u1_C5***')
print(stats.f_oneway(u1_C5[0,:], u1_C5[1,:], u1_C5[2,:], u1_C5[3,:], u1_C5[4,:]))
#print('***subject 2, statistical difference between runs u2_C5***')
#print(stats.f_oneway(u2_C5[0,:], u2_C5[1,:], u2_C5[2,:], u2_C5[3,:], u2_C5[4,:]))
print('***subject 3, statistical difference between runs u3_C5***')
print(stats.f_oneway(u3_C5[0,:], u3_C5[1,:], u3_C5[2,:], u3_C5[3,:], u3_C5[4,:]))
#print('***subject 4, statistical difference between runs u4_C5***')
#print(stats.f_oneway(u4_C5[0,:], u4_C5[1,:], u4_C5[2,:], u4_C5[3,:], u4_C5[4,:]))
#print('***subject 5, statistical difference between runs u5_C5***')
#print(stats.f_oneway(u5_C5[0,:], u5_C5[1,:], u5_C5[2,:], u5_C5[3,:], u5_C5[4,:]))
#print('***subject 6, statistical difference between runs u6_C5***')
#print(stats.f_oneway(u6_C5[0,:], u6_C5[1,:], u6_C5[2,:], u6_C5[3,:], u6_C5[4,:]))

print('-----------------------  e   -------------------------')
#print('***subject 1, statistical difference between runs e1_C1***')
#print(stats.f_oneway(e1_C1[0,:], e1_C1[1,:], e1_C1[2,:], e1_C1[3,:], e1_C1[4,:]))
#print('***subject 2, statistical difference between runs e2_C1***')
#print(stats.f_oneway(e2_C1[0,:], e2_C1[1,:], e2_C1[2,:], e2_C1[3,:], e2_C1[4,:]))
#print('***subject 3, statistical difference between runs e3_C1***')
#print(stats.f_oneway(e3_C1[0,:], e3_C1[1,:], e3_C1[2,:], e3_C1[3,:], e3_C1[4,:]))
print('***subject 4, statistical difference between runs e4_C1***')
print(stats.f_oneway(e4_C1[0,:], e4_C1[1,:], e4_C1[2,:], e4_C1[3,:], e4_C1[4,:]))
#print('***subject 5, statistical difference between runs e5_C1***')
#print(stats.f_oneway(e5_C1[0,:], e5_C1[1,:], e5_C1[2,:], e5_C1[3,:], e5_C1[4,:]))
##print('***subject 6, statistical difference between runs e6_C1***')
##print(stats.f_oneway(e6_C1[0,:], e6_C1[1,:], e6_C1[2,:], e6_C1[3,:], e6_C1[4,:]))

#print('***subject 1, statistical difference between runs e1_C2***')
#print(stats.f_oneway(e1_C2[0,:], e1_C2[1,:], e1_C2[2,:], e1_C2[3,:], e1_C2[4,:]))
print('***subject 2, statistical difference between runs e2_C2***')
print(stats.f_oneway(e2_C2[0,:], e2_C2[1,:], e2_C2[2,:], e2_C2[3,:], e2_C2[4,:]))
#print('***subject 3, statistical difference between runs e3_C2***')
#print(stats.f_oneway(e3_C2[0,:], e3_C2[1,:], e3_C2[2,:], e3_C2[3,:], e3_C2[4,:]))
#print('***subject 4, statistical difference between runs e4_C2***')
#print(stats.f_oneway(e4_C2[0,:], e4_C2[1,:], e4_C2[2,:], e4_C2[3,:], e4_C2[4,:]))
#print('***subject 5, statistical difference between runs e5_C2***')
#print(stats.f_oneway(e5_C2[0,:], e5_C2[1,:], e5_C2[2,:], e5_C2[3,:], e5_C2[4,:]))
#print('***subject 6, statistical difference between runs e6_C2***')
#print(stats.f_oneway(e6_C2[0,:], e6_C2[1,:], e6_C2[2,:], e6_C2[3,:], e6_C2[4,:]))
#
#print('***subject 1, statistical difference between runs e1_C3***')
#print(stats.f_oneway(e1_C3[0,:], e1_C3[1,:], e1_C3[2,:], e1_C3[3,:], e1_C3[4,:]))
#print('***subject 2, statistical difference between runs e2_C3***')
#print(stats.f_oneway(e2_C3[0,:], e2_C3[1,:], e2_C3[2,:], e2_C3[3,:], e2_C3[4,:]))
#print('***subject 3, statistical difference between runs e3_C3***')
#print(stats.f_oneway(e3_C3[0,:], e3_C3[1,:], e3_C3[2,:], e3_C3[3,:], e3_C3[4,:]))
#print('***subject 4, statistical difference between runs e4_C3***')
#print(stats.f_oneway(e4_C3[0,:], e4_C3[1,:], e4_C3[2,:], e4_C3[3,:], e4_C3[4,:]))
#print('***subject 5, statistical difference between runs e5_C3***')
#print(stats.f_oneway(e5_C3[0,:], e5_C3[1,:], e5_C3[2,:], e5_C3[3,:], e5_C3[4,:]))
#print('***subject 6, statistical difference between runs e6_C3***')
#print(stats.f_oneway(e6_C3[0,:], e6_C3[1,:], e6_C3[2,:], e6_C3[3,:], e6_C3[4,:]))

#print('***subject 1, statistical difference between runs e1_C4***')
#print(stats.f_oneway(e1_C4[0,:], e1_C4[1,:], e1_C4[2,:], e1_C4[3,:], e1_C4[4,:]))
print('***subject 2, statistical difference between runs e2_C4***')
print(stats.f_oneway(e2_C4[0,:], e2_C4[1,:], e2_C4[2,:], e2_C4[3,:], e2_C4[4,:]))
#print('***subject 3, statistical difference between runs e3_C4***')
#print(stats.f_oneway(e3_C4[0,:], e3_C4[1,:], e3_C4[2,:], e3_C4[3,:], e3_C4[4,:]))
print('***subject 4, statistical difference between runs e4_C4***')
print(stats.f_oneway(e4_C4[0,:], e4_C4[1,:], e4_C4[2,:], e4_C4[3,:], e4_C4[4,:]))
#print('***subject 5, statistical difference between runs e5_C4***')
#print(stats.f_oneway(e5_C4[0,:], e5_C4[1,:], e5_C4[2,:], e5_C4[3,:], e5_C4[4,:]))
#print('***subject 6, statistical difference between runs e6_C4***')
#print(stats.f_oneway(e6_C4[0,:], e6_C4[1,:], e6_C4[2,:], e6_C4[3,:], e6_C4[4,:]))

print('***subject 1, statistical difference between runs e1_C5***')
print(stats.f_oneway(e1_C5[0,:], e1_C5[1,:], e1_C5[2,:], e1_C5[3,:], e1_C5[4,:]))
#print('***subject 2, statistical difference between runs e2_C5***')
#print(stats.f_oneway(e2_C5[0,:], e2_C5[1,:], e2_C5[2,:], e2_C5[3,:], e2_C5[4,:]))
#print('***subject 3, statistical difference between runs e3_C5***')
#print(stats.f_oneway(e3_C5[0,:], e3_C5[1,:], e3_C5[2,:], e3_C5[3,:], e3_C5[4,:]))
print('***subject 4, statistical difference between runs e4_C5***')
print(stats.f_oneway(e4_C5[0,:], e4_C5[1,:], e4_C5[2,:], e4_C5[3,:], e4_C5[4,:]))
#print('***subject 5, statistical difference between runs e5_C5***')
#print(stats.f_oneway(e5_C5[0,:], e5_C5[1,:], e5_C5[2,:], e5_C5[3,:], e5_C5[4,:]))
#print('***subject 6, statistical difference between runs e6_C5***')
#print(stats.f_oneway(e6_C5[0,:], e6_C5[1,:], e6_C5[2,:], e6_C5[3,:], e6_C5[4,:]))


# ---------------------------- Boxplot -------------------------------

# ---------------------------- Position Control -------------------------------
eAll_C1_mean = [e1_C1_mean, e2_C1_mean, e3_C1_mean, e4_C1_mean, e5_C1_mean, e6_C1_mean]
eAll_C4_mean = [e1_C4_mean, e2_C4_mean, e3_C4_mean, e4_C4_mean, e5_C4_mean, e6_C4_mean]
ticks = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)
    
plt.figure()

bpl = plt.boxplot(eAll_C1_mean, positions=np.array(range(len(eAll_C1_mean)))*2.0-0.3, sym='', widths=0.5)
bpr = plt.boxplot(eAll_C4_mean, positions=np.array(range(len(eAll_C4_mean)))*2.0+0.3, sym='', widths=0.5)
set_box_color(bpl, '#D7191C')
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='No Motion')
plt.plot([], c='#2C7BB6', label='Motion')
plt.legend(loc='upper right')

plt.title('Mean error; position control')
plt.ylabel("e[-]")
plt.axhline(y=0, xmin=-2, xmax= len(ticks)*2, linestyle = '--', color ='k', linewidth=0.4)


plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
#plt.ylim(0, 8)
plt.tight_layout()


# ---------------------------- Velocity Control -------------------------------
eAll_C2_mean = [e1_C2_mean, e2_C2_mean, e3_C2_mean, e4_C2_mean, e5_C2_mean, e6_C2_mean]
eAll_C5_mean = [e1_C5_mean, e2_C5_mean, e3_C5_mean, e4_C5_mean, e5_C5_mean, e6_C5_mean]
ticks = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)
    
plt.figure()

bpl = plt.boxplot(eAll_C2_mean, positions=np.array(range(len(eAll_C2_mean)))*2.0-0.3, sym='', widths=0.5)
bpr = plt.boxplot(eAll_C5_mean, positions=np.array(range(len(eAll_C5_mean)))*2.0+0.3, sym='', widths=0.5)
set_box_color(bpl, '#D7191C')
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='No Motion')
plt.plot([], c='#2C7BB6', label='Motion')
plt.legend(loc='upper right')

plt.title('Mean error; velocity control')
plt.ylabel("e[-]")
plt.axhline(y=0, xmin=-2, xmax= len(ticks)*2, linestyle = '--', color ='k', linewidth=0.4)


plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
#plt.ylim(0, 8)
plt.tight_layout()


# ---------------------------- Acceleration Control -------------------------------
eAll_C3_mean = [e1_C3_mean, e2_C3_mean, e3_C3_mean, e4_C3_mean, e5_C3_mean, e6_C3_mean]
eAll_C6_mean = [e1_C6_mean, e2_C6_mean, e3_C6_mean, e4_C6_mean, e5_C6_mean, e6_C6_mean]
ticks = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)
    
plt.figure()

bpl = plt.boxplot(eAll_C3_mean, positions=np.array(range(len(eAll_C3_mean)))*2.0-0.3, sym='', widths=0.5)
bpr = plt.boxplot(eAll_C6_mean, positions=np.array(range(len(eAll_C6_mean)))*2.0+0.3, sym='', widths=0.5)
set_box_color(bpl, '#D7191C')
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='No Motion')
plt.plot([], c='#2C7BB6', label='Motion')
plt.legend()
plt.title('Mean error; acceleration control')
plt.ylabel("e[-]")
plt.axhline(y=0, xmin=-2, xmax= len(ticks)*2, linestyle = '--', color ='k', linewidth=0.4)


plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.tight_layout()
