import scipy.io
import numpy as np
import matplotlib.pyplot as plt


# Read Matlab file
datasubj1 = scipy.io.loadmat("ae2223I_measurement_data_subj1.mat")
#print(sorted(datasubj1.keys()))

# Note:
#     | P   V   A
# _________________
#  NM | C1  C2  C3
#  M  | C4  C5  C6

# ---------------------------------- Variables ---------------------------------
w_FC    = datasubj1['w_FC']         # Frequency
t       = datasubj1['t'][0]         # Time
data_C1 = datasubj1['data_C1']      # Data Condition 1
data_C2 = datasubj1['data_C2']
data_C3 = datasubj1['data_C3']
data_C4 = datasubj1['data_C4']
data_C5 = datasubj1['data_C5']
data_C6 = datasubj1['data_C6']

# Subvariables for each Condition
e_C1       = data_C1['e'][0][0].reshape(8192, 5)
u_C1       = data_C1['u'][0][0].reshape(8192, 5)
x_C1       = data_C1['x'][0][0].reshape(8192, 5)
ft_C1      = data_C1['ft']
fd_C1      = data_C1['fd']
Hpe_FC_C1  = data_C1['Hpe_FC'][0][0]
Hpxd_FC_C1 = data_C1['Hpxd_FC'][0][0]


e_C2 = data_C2['e'][0][0].reshape(8192, 5)
u_C2 = data_C2['u'][0][0].reshape(8192, 5)
x_C2 = data_C2['x'][0][0].reshape(8192, 5)
ft_C2 = data_C2['ft']
fd_C2 = data_C2['fd']
Hpe_FC_C2  = data_C2['Hpe_FC'][0][0]
Hpxd_FC_C2 = data_C2['Hpxd_FC'][0][0]


e_C3 = data_C3['e'][0][0].reshape(8192, 5)
u_C3 = data_C3['u'][0][0].reshape(8192, 5)
x_C3 = data_C3['x'][0][0].reshape(8192, 5)
ft_C3 = data_C3['ft']
fd_C3 = data_C3['fd']
Hpe_FC_C3  = data_C3['Hpe_FC'][0][0]
Hpxd_FC_C3 = data_C3['Hpxd_FC'][0][0]


e_C4 = data_C4['e'][0][0].reshape(8192, 5)
u_C4 = data_C4['u'][0][0].reshape(8192, 5)
x_C4 = data_C4['x'][0][0].reshape(8192, 5)
ft_C4 = data_C4['ft']
fd_C4 = data_C4['fd']
Hpe_FC_C4  = data_C4['Hpe_FC'][0][0]
Hpxd_FC_C4 = data_C4['Hpxd_FC'][0][0]


e_C5 = data_C5['e'][0][0].reshape(8192, 5)
u_C5 = data_C5['u'][0][0].reshape(8192, 5)
x_C5 = data_C5['x'][0][0].reshape(8192, 5)
ft_C5 = data_C5['ft']
fd_C5 = data_C5['fd']
Hpe_FC_C5  = data_C5['Hpe_FC'][0][0]
Hpxd_FC_C5 = data_C5['Hpxd_FC'][0][0]


e_C6 = data_C6['e'][0][0].reshape(8192, 5)
u_C6 = data_C6['u'][0][0].reshape(8192, 5)
x_C6 = data_C6['x'][0][0].reshape(8192, 5)
ft_C6 = data_C6['ft']
fd_C6 = data_C6['fd']
Hpe_FC_C6  = data_C6['Hpe_FC'][0][0]
Hpxd_FC_C6 = data_C6['Hpxd_FC'][0][0]


# ---------------------------- Plots --------------------------------

# --------------- Magnitude plots ------------------
plt.suptitle("Magnitude plots")

plt.subplot(321)
plt.loglog(w_FC, Hpe_FC_C1, color='r', linestyle='-', marker='o', markersize='4')
#plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")

plt.subplot(322)
plt.loglog(w_FC, Hpe_FC_C2, color='b', linestyle='-', marker='o', markersize='4')
#plt.xlabel("ω [rad/s]")
#plt.ylabel("$|H_{pe}(jω)|$")

plt.subplot(323)
plt.loglog(w_FC, Hpe_FC_C3, color='g', linestyle='-', marker='o', markersize='4')
#plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")

plt.subplot(324)
plt.loglog(w_FC, Hpe_FC_C4, color='#967BB6', linestyle='-', marker='o', markersize='4')
#plt.xlabel("ω [rad/s]")
#plt.ylabel("$|H_{pe}(jω)|$")

plt.subplot(325)
plt.loglog(w_FC, Hpe_FC_C5, color='#86D7FF', linestyle='-', marker='o', markersize='4')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")

plt.subplot(326)
plt.loglog(w_FC, Hpe_FC_C6, color='#0FF64D', linestyle='-', marker='o', markersize='4')
plt.xlabel("ω [rad/s]")
#plt.ylabel("$|H_{pe}(jω)|$")

plt.show()

# ------------------------------- Angle plots --------------------------------
plt.suptitle("Phase plots")

plt.subplot(311)
plt.semilogx(w_FC, np.angle(Hpxd_FC_C4, deg=True), color='r', linestyle='-', marker='o', markersize='4')
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")

plt.subplot(312)
plt.semilogx(w_FC, np.angle(Hpxd_FC_C5, deg=True), color='b', linestyle='-', marker='o', markersize='4')
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")

plt.subplot(313)
plt.semilogx(w_FC, np.angle(Hpxd_FC_C6, deg=True), color='g', linestyle='-', marker='o', markersize='4')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")

plt.show()