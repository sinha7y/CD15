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

#-----------------------------Peaks of input function-----------------------------------------

matrix1=np.empty((36,5))
o=0
for i in range(6):
    for j in range(6):
        tabel1=[]
        for k in range(5):
            peaks=0
            for l in range(8190):
                if peak(a[j][i][1][l][k],a[j][i][1][l+1][k],a[j][i][1][l+2][k])==True:
                    peaks+=1
            tabel1.append(peaks)
        matrix1[o]=tabel1
        o+=1

#-----------------------------Maximum and minimum of error function----------------------------------------

matrix2=np.empty((36,5))
matrix3=np.empty((36,5))
o=0
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
        matrix2[o]=tabelmax
        matrix3[o]=tabelmin
        o+=1
    
#-----------------------------Average steep of input function-----------------------

matrix4=np.empty((36,5))
o=0
for i in range(6):
    for j in range(6):
        tabelslope=[]
        for k in range(5):
            panda=0
            for l in range(8191):
                panda=panda+slope(a[i][j][1][l][k],a[i][j][1][l+1][k])
            panda=panda/8191
            tabelslope.append(panda)
        matrix4[o]=tabelslope
        o+=1

#-----------------------------Average steep of output function-----------------------

matrix5=np.empty((36,5))
o=0
for i in range(6):
    for j in range(6):
        tabelslope=[]
        for k in range(5):
            panda=0
            for l in range(8191):
                panda=panda+slope(a[i][j][2][l][k],a[i][j][2][l+1][k])
            panda=panda/8191
            tabelslope.append(panda)
        matrix5[o]=tabelslope
        o+=1

#--------------------------------Looking for errors------------------------------------
"""
for i in range(6):
    for j in range(6):
        tabelslope=[]
        for k in range(5):
            l=0
            while(l<8188):
                if ((a[j][i][0][l][k]>0.8 and a[j][i][0][l][k]<1) and (slope(a[j][i][0][l][k],a[j][i][0][l+1][k])>0)) or ((a[j][i][0][l][k]<-0.8 and a[j][i][0][l][k]>-1) and (slope(a[j][i][0][l][k],a[j][i][0][l+1][k])<0)):
                    for m in range(l+3,8189):
                        if peak(a[j][i][0][m][k],a[j][i][0][m+1][k],a[j][i][0][m+2][k])==True:
                            constant=abs((a[j][i][0][l][k]-a[j][i][0][m+1][k])/2)
                            slope1=abs(slope(constant,a[j][i][0][m+1][k]))
                            slope2=abs(slope(a[j][i][0][l][k],constant))
                            if (slope2>slope1):
                                print(a[j][i][0][l][k])
                            break
                l+=1
    print(i)
"""
#------------------------------------Graphs-----------------------------------------
vectornames=['pos. control; no motion','vel. control; no motion','acc. control; no motion','pos. control; motion','vel. control; motion','acc. control; motion']

#Peaks
for i in range(6):
    vectorpeaks=[]
    tpeak=[]
    f=0
    for j in range(6):
        for k in range(5):
            vectorpeaks.append(matrix1[6*j+i][k])
            f+=1
            tpeak.append(f)
    constant=231+i               
    plt.subplot(constant)
    plt.plot(tpeak, vectorpeaks,'r+')
    plt.title(vectornames[i])
    plt.ylabel("u[-]")
    print(vectornames[i],np.average(vectorpeaks))
    
plt.show()

#Maximum and minimum
for i in range(6):
    vectormax=[]
    tmax=[]
    f=0
    for j in range(6):
        for k in range(5):
            vectormax.append(matrix2[6*j+i][k])
            f+=1
            tmax.append(f)
            vectormax.append(matrix3[6*j+i][k])
            f+=1
            tmax.append(f)
    constant=231+i               
    plt.subplot(constant)
    plt.plot(tmax, vectormax,'r+')
    plt.title(vectornames[i])
    plt.ylabel("e[-]")
    vectormax=np.absolute(vectormax)
    print(vectornames[i],np.average(vectormax))
    
plt.show()

#Slope input
for i in range(6):
    vectorslope=[]
    for j in range(6):
        for k in range(5):
            vectorslope.append(matrix4[6*j+i][k])
    constant=231+i               
    plt.subplot(constant)
    plt.plot(tpeak, vectorslope,'r+')
    plt.title(vectornames[i])
    plt.ylabel("u[-]")
    print(vectornames[i],np.average(vectorslope))
    
plt.show()

#Slope output
for i in range(6):
    vectorslopex=[]
    for j in range(6):
        for k in range(5):
            vectorslopex.append(matrix5[6*j+i][k])
    constant=231+i               
    plt.subplot(constant)
    plt.plot(tpeak, vectorslopex,'r+')
    plt.title(vectornames[i])
    plt.ylabel("x[-]")
    print(vectornames[i],np.average(vectorslopex))
    
plt.show()


