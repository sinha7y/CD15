import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

#----------------------------Initialisation---------------------------------------

a = np.empty((6,6,3,8192,5)) # Columns: Subjects, Condition, (e/u/x), measurements, try
b = np.empty((6,6,8192,1)) # Columns: Subjects, Condition, measurements, try

# Time matrix
t=[]
for i in range (8192):
    t.append(i/10)

# Target function
datasubj1 = scipy.io.loadmat("ae2223I_measurement_data_subj1.mat") # Subject 1
data1_C1  = datasubj1['data_C1']                                   # Data Condition 1
ft        = data1_C1['ft'][0][0].reshape(8192,1)                   # Target function

# Matrix for e,u,x and fd
for i in range(6):
    c='ae2223I_measurement_data_subj'+chr(i+49)+'.mat'
    datasubj = scipy.io.loadmat(c)
    for j in range(6):
        d='data_C'+chr(i+49)
        data = datasubj[d]
        e = data['e'][0][0].reshape(8192, 5)
        u = data['u'][0][0].reshape(8192, 5)
        x = data['x'][0][0].reshape(8192, 5)
        fd = data1_C1['fd'][0][0].reshape(8192,1)
        a[i][j][0] = e
        a[i][j][1] = u
        a[i][j][2] = x
        b[i][j] = fd

#-------------------------------Definitions---------------------------------

def maximum(a,t):

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

def minimum(a,t):

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

def steepest_change(a,t):
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

#--------------------------------Maximum-----------------------------------------

        

