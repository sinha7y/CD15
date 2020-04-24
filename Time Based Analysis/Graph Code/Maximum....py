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

def peak(a,b,c):
    const = (b-a)/0.1
    cst = (c-b)/0.1
    if (np.sign(const)!=np.sign(cst)):
        return True
    else:
        return False

#-----------------------------Peaks of input function-----------------------------------------

for i in range(6):
    for j in range(6):
        tabel1=[]
        for k in range(5):
            peaks=0
            for l in range(8190):
                if peak(a[j][i][2][l][k],a[j][i][2][l+1][k],a[j][i][2][l+2][k])==True:
                    peaks+=1
            tabel1.append(peaks)
        print(tabel1)

#-----------------------------Maximum and minimum of error function----------------------------------------

for i in range(6):
    for j in range(6):
        tabelmax=[]
        tabelmin=[]
        for k in range(5):
            maximum=0
            minimum=0
            for l in range(8190):
                if maximum<a[j][i][0][l][k]:
                    maximum=a[j][i][0][l][k]
                if minimum>a[j][i][0][l][k]:
                    minimum=a[j][i][0][l][k]
            tabelmax.append(maximum)
            tabelmin.append(minimum)
        print(tabelmax)
        print(tabelmin)
    

