import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.weightstats import ttest_ind

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

def change(matrix):
    a=matrix[1]
    matrix[1]=matrix[3]
    matrix[3]=a

    a=matrix[2]
    matrix[2]=matrix[3]
    matrix[3]=a

    a=matrix[3]
    matrix[3]=matrix[4]
    matrix[4]=a
    return (matrix)
#-----------------------------Peaks of input function-----------------------------------------

matrix1=np.empty((36,5))
o=0
for i in range(6):
    for j in range(6):
        tabel1=[]
        for k in range(5):
            peaks=0
            for l in range(8190):
                if peak(a[j][i][0][l][k],a[j][i][0][l+1][k],a[j][i][0][l+2][k])==True:
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
namesboxplot=['p-nm','p-m','v-nm','v-m','a-nm','a-m']

#Peaks
print("Average number of stick movements for every case")
matrix11=[]
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
    matrix11.append(vectorpeaks)
    plt.subplot(constant)
    plt.plot(tpeak, vectorpeaks,'r+')
    plt.title(vectornames[i])
    plt.ylabel("u[-]")
    print(vectornames[i],np.average(vectorpeaks))
plt.suptitle('Number of peaks for the human input function',fontsize=14)
plt.show()

matrix11=change(matrix11)
plt.suptitle('Boxplot with the number of peaks of the input function')
plt.boxplot(np.transpose(matrix11),labels=namesboxplot)
plt.show()

#Maximum and minimum
print("Average of the maximum absolute error for every case")
matrix12=[]
matrix13=[]
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
    matrix12.append(vectormax[0:len(vectormax)-1:2])
    matrix13.append(vectormax[1:len(vectormax):2])
    plt.subplot(constant)
    plt.plot(tmax, vectormax,'r+')
    plt.title(vectornames[i])
    plt.ylabel("e[-]")
    vectormax=np.absolute(vectormax)
    print(vectornames[i],np.average(vectormax))
plt.suptitle('Maximum and minimum of the error function',fontsize=14)    
plt.show()

matrix12=change(matrix12)
plt.suptitle('Boxplot with the maximum of the error function')
plt.boxplot(np.transpose(matrix12),labels=namesboxplot)
plt.show()

matrix13=change(matrix13)
plt.suptitle('Boxplot with the minimum of the error function')
plt.boxplot(np.transpose(matrix13),labels=namesboxplot)
plt.show()

#Slope input
print("Average of the slope of human input function for every case")
matrix14=[]
for i in range(6):
    vectorslope=[]
    for j in range(6):
        for k in range(5):
            vectorslope.append(matrix4[6*j+i][k])
    constant=231+i
    matrix14.append(vectorslope)
    plt.subplot(constant)
    plt.plot(tpeak, vectorslope,'r+')
    plt.title(vectornames[i])
    plt.ylabel("u[-]")
    print(vectornames[i],np.average(vectorslope))
plt.suptitle('Average slope for the human input function',fontsize=14)     
plt.show()

matrix14=change(matrix14)
plt.suptitle('Boxplot with the average slope of the input function')
plt.boxplot(np.transpose(matrix14),labels=namesboxplot)
plt.show()

#Slope output
print("Average of the slope of output function for every case")
matrix15=[]
for i in range(6):
    vectorslopex=[]
    for j in range(6):
        for k in range(5):
            vectorslopex.append(matrix5[6*j+i][k])
    constant=231+i
    matrix15.append(vectorslopex)
    plt.subplot(constant)
    plt.plot(tpeak, vectorslopex,'r+')
    plt.title(vectornames[i])
    plt.ylabel("x[-]")
    print(vectornames[i],np.average(vectorslopex))
plt.suptitle('Average slope for the output function',fontsize=14)      
plt.show()

matrix15=change(matrix15)
plt.suptitle('Boxplot with the average slope of the output function')
plt.boxplot(np.transpose(matrix15),labels=namesboxplot)
plt.show()


#********** Statistics **********
print('***** Matrix 11 **********')
ttest_matrix11_pos=ttest_ind(matrix11[0,:], matrix11[1,:])
ttest_matrix11_vel=ttest_ind(matrix11[2,:], matrix11[3,:])
ttest_matrix11_acc=ttest_ind(matrix11[4,:], matrix11[5,:])

t_value_matrix11_pos=ttest_matrix11_pos[0]
p_value_matrix11_pos=ttest_matrix11_pos[1]
deg_freedom_matrix11_pos=ttest_matrix11_pos[2]

t_value_matrix11_vel=ttest_matrix11_vel[0]
p_value_matrix11_vel=ttest_matrix11_vel[1]
deg_freedom_matrix11_vel=ttest_matrix11_vel[2]

t_value_matrix11_acc=ttest_matrix11_acc[0]
p_value_matrix11_acc=ttest_matrix11_acc[1]
deg_freedom_matrix11_acc=ttest_matrix11_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, matrix11***')
print('t_value=',round(t_value_matrix11_pos,3), ',',  round(t_value_matrix11_vel,3), ',',  round(t_value_matrix11_acc,3))
print('p_value=',round(p_value_matrix11_pos,3), ',',  round(p_value_matrix11_vel,3), ',',  round(p_value_matrix11_acc,3))
print('degrees of freedom:',deg_freedom_matrix11_pos)
print('')

print('***** Matrix 12 **********')
ttest_matrix12_pos=ttest_ind(matrix12[0,:], matrix12[1,:])
ttest_matrix12_vel=ttest_ind(matrix12[2,:], matrix12[3,:])
ttest_matrix12_acc=ttest_ind(matrix12[4,:], matrix12[5,:])

t_value_matrix12_pos=ttest_matrix12_pos[0]
p_value_matrix12_pos=ttest_matrix12_pos[1]
deg_freedom_matrix12_pos=ttest_matrix12_pos[2]

t_value_matrix12_vel=ttest_matrix12_vel[0]
p_value_matrix12_vel=ttest_matrix12_vel[1]
deg_freedom_matrix12_vel=ttest_matrix12_vel[2]

t_value_matrix12_acc=ttest_matrix12_acc[0]
p_value_matrix12_acc=ttest_matrix12_acc[1]
deg_freedom_matrix12_acc=ttest_matrix12_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, matrix12***')
print('t_value=',round(t_value_matrix12_pos,3), ',',  round(t_value_matrix12_vel,3), ',',  round(t_value_matrix12_acc,3))
print('p_value=',round(p_value_matrix12_pos,3), ',',  round(p_value_matrix12_vel,3), ',',  round(p_value_matrix12_acc,3))
print('degrees of freedom:',deg_freedom_matrix12_pos)
print('')


print('***** Matrix 13 **********')
ttest_matrix13_pos=ttest_ind(matrix13[0,:], matrix13[1,:])
ttest_matrix13_vel=ttest_ind(matrix13[2,:], matrix13[3,:])
ttest_matrix13_acc=ttest_ind(matrix13[4,:], matrix13[5,:])

t_value_matrix13_pos=ttest_matrix13_pos[0]
p_value_matrix13_pos=ttest_matrix13_pos[1]
deg_freedom_matrix13_pos=ttest_matrix13_pos[2]

t_value_matrix13_vel=ttest_matrix13_vel[0]
p_value_matrix13_vel=ttest_matrix13_vel[1]
deg_freedom_matrix13_vel=ttest_matrix13_vel[2]

t_value_matrix13_acc=ttest_matrix13_acc[0]
p_value_matrix13_acc=ttest_matrix13_acc[1]
deg_freedom_matrix13_acc=ttest_matrix13_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, matrix13***')
print('t_value=',round(t_value_matrix13_pos,3), ',',  round(t_value_matrix13_vel,3), ',',  round(t_value_matrix13_acc,3))
print('p_value=',round(p_value_matrix13_pos,3), ',',  round(p_value_matrix13_vel,3), ',',  round(p_value_matrix13_acc,3))
print('degrees of freedom:',deg_freedom_matrix13_pos)
print('')


print('***** Matrix 14 **********')
ttest_matrix14_pos=ttest_ind(matrix14[0,:], matrix14[1,:])
ttest_matrix14_vel=ttest_ind(matrix14[2,:], matrix14[3,:])
ttest_matrix14_acc=ttest_ind(matrix14[4,:], matrix14[5,:])

t_value_matrix14_pos=ttest_matrix14_pos[0]
p_value_matrix14_pos=ttest_matrix14_pos[1]
deg_freedom_matrix14_pos=ttest_matrix14_pos[2]

t_value_matrix14_vel=ttest_matrix14_vel[0]
p_value_matrix14_vel=ttest_matrix14_vel[1]
deg_freedom_matrix14_vel=ttest_matrix14_vel[2]

t_value_matrix14_acc=ttest_matrix14_acc[0]
p_value_matrix14_acc=ttest_matrix14_acc[1]
deg_freedom_matrix14_acc=ttest_matrix14_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, matrix14***')
print('t_value=',round(t_value_matrix14_pos,3), ',',  round(t_value_matrix14_vel,3), ',',  round(t_value_matrix14_acc,3))
print('p_value=',round(p_value_matrix14_pos,3), ',',  round(p_value_matrix14_vel,3), ',',  round(p_value_matrix14_acc,3))
print('degrees of freedom:',deg_freedom_matrix14_pos)
print('')


print('***** Matrix 15 **********')
ttest_matrix15_pos=ttest_ind(matrix15[0,:], matrix15[1,:])
ttest_matrix15_vel=ttest_ind(matrix15[2,:], matrix15[3,:])
ttest_matrix15_acc=ttest_ind(matrix15[4,:], matrix15[5,:])

t_value_matrix15_pos=ttest_matrix15_pos[0]
p_value_matrix15_pos=ttest_matrix15_pos[1]
deg_freedom_matrix15_pos=ttest_matrix15_pos[2]

t_value_matrix15_vel=ttest_matrix15_vel[0]
p_value_matrix15_vel=ttest_matrix15_vel[1]
deg_freedom_matrix15_vel=ttest_matrix15_vel[2]

t_value_matrix15_acc=ttest_matrix15_acc[0]
p_value_matrix15_acc=ttest_matrix15_acc[1]
deg_freedom_matrix15_acc=ttest_matrix15_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, matrix15***')
print('t_value=',round(t_value_matrix15_pos,3), ',',  round(t_value_matrix15_vel,3), ',',  round(t_value_matrix15_acc,3))
print('p_value=',round(p_value_matrix15_pos,3), ',',  round(p_value_matrix15_vel,3), ',',  round(p_value_matrix15_acc,3))
print('degrees of freedom:',deg_freedom_matrix15_pos)
print('')

