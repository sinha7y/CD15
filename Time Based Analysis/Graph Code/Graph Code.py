import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath

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

# ---------------------------- Plot --------------------------------

# Error as a function of time
plt.plot(t, e1_C1)
plt.title('Error signal; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, e1_C2)
plt.title('Error signal; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, e1_C3)
plt.title('Error signal; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, e1_C4)
plt.title('Error signal; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, e1_C5)
plt.title('Error signal; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, e1_C6)
plt.title('Error signal; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("e[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Human operator control input as a function of time

plt.plot(t, u1_C1)
plt.title('Human input; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, u1_C2)
plt.title('Human input; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, u1_C3)
plt.title('Human input; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, u1_C4)
plt.title('Human input; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, u1_C5)
plt.title('Human input; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, u1_C6)
plt.title('Human input; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("u[-]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Pitch input as a function of time

plt.plot(t, x1_C1)
plt.title('Pitch input; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, x1_C2)
plt.title('Pitch input; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, x1_C3)
plt.title('Pitch input; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s2]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, x1_C4)
plt.title('Pitch input; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, x1_C5)
plt.title('Pitch input; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

plt.plot(t, x1_C6)
plt.title('Pitch input; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("x[m/s2]")
plt.legend(('1st try', '2nd try', '3rd try','4rd try','5rd try'),
           loc='upper right')
plt.show()

# Target forcing function as a function of time

plt.plot(t,ft1_C1)
plt.title('Target forcing function; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

plt.plot(t, ft1_C2)
plt.title('Target forcing function; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

plt.plot(t, ft1_C3)
plt.title('Target forcing function; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

plt.plot(t, ft1_C4)
plt.title('Target forcing function; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

plt.plot(t, ft1_C5)
plt.title('Target forcing function; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

plt.plot(t, ft1_C6)
plt.title('Target forcing function; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("ft[N]")
plt.show()

# Disturbance forcing function as a function of time

plt.plot(t,fd1_C1)
plt.title('Disturbance forcing function; position control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()

plt.plot(t, fd1_C2)
plt.title('Disturbance forcing function; velocity control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()

plt.plot(t, fd1_C3)
plt.title('Disturbance forcing function; acceleration control; no motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()

plt.plot(t, fd1_C4)
plt.title('Disturbance forcing function; position control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()

plt.plot(t, fd1_C5)
plt.title('Disturbance forcing function; velocity control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()

plt.plot(t, fd1_C6)
plt.title('Disturbance forcing function; acceleration control; motion')
plt.xlabel("t[s]")
plt.ylabel("fd[N]")
plt.show()
