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
        d='data_C'+chr(j+49)
        data = datasubj[d]
        e = data['e'][0][0].reshape(8192, 5)
        u = data['u'][0][0].reshape(8192, 5)
        x = data['x'][0][0].reshape(8192, 5)
        fd = data['fd'][0][0].reshape(8192,1)
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

def slope(a,b):
    return abs((b-a)/0.1)

#---------------------------------Looking for major peaks----------------------------
"""
peaks=[]
for i in range (len(ft)-3):
    if peak(ft[i],ft[i+1],ft[i+2])==True:
        peaks.append([ft[i+1],i])
i=0
goodpeaks=[]
while (i<(len(peaks)-2)):
    if (peaks[i+1][1]-peaks[i][1]>30) or (peaks[i+2][1]-peaks[i+1][1]>30):
        peaks=np.delete(peaks,i+1)
        print(i)
        i=i-1
    i+=1
print(peaks)
"""
sm=[]
fspline=[]
for i in range (32):
    sm.append(i*256)
    fspline.append(ft[i*256])

peaks=[]
for i in range (len(fspline)-3):
    if peak(fspline[i],fspline[i+1],fspline[i+2])==True:
        peaks.append([fspline[i+1],(i+1)*128])

goodpeaks=[]
i=0
while (i<(len(peaks)-2)):
    if (abs(peaks[i+1][0]-peaks[i][0]>5)) or (abs(peaks[i+2][0]-peaks[i+1][0])>5):
        goodpeaks.append(peaks[i+1])
    i+=1
print(goodpeaks)

plt.plot(sm,fspline)
plt.plot(ft)
plt.show()



