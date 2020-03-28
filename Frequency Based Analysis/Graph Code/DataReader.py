import scipy.io
import numpy as np
import matplotlib.pyplot as plt


# Read Matlab file
datasubj1 = scipy.io.loadmat("ae2223I_measurement_data_subj6.mat")

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


# ---------------------------- Precision Model function --------------------------------
j = complex(0, 1)       # Define j

# Precision model function
def Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio):
    return K_p * (T_L*w_FC*j + 1)/(T_I*w_FC*j + 1) * np.exp(-w_FC*j*t_e) * (1 / ((w_FC*j/w_nm)*(w_FC*j/w_nm) + (2*damping_ratio*w_FC*j / w_nm) + 1))


# ---------------------------------------- PLOTS --------------------------------------

"""
-----------------------------------------------------------------------------------
----------------------------------- POSITION --------------------------------------
-----------------------------------------------------------------------------------
"""

# --------------------------------- POSITION H_pe ----------------------------

# Variables:
K_p = 3                 # Pilot gain
T_L = 0.1               # Lead time constant
T_I = 1.58              # Lag time constant
t_e = 0.10              # Effective time delay
w_nm = 8.0              # Neuromuscular frequency
damping_ratio = 0.10    # Neuromuscular damping ratio

# Model:
Y_p_position_Hpe = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# -------------- Magnitude plot H_pe ------------------
plt.subplot(121)
plt.title("Magnitude plot - $H_{pe}(jω)$ - Position (C1+C4)")
plt.loglog(w_FC, abs(Hpe_FC_C1), color='#967BB6', linestyle='-', marker='o', markersize='4', label='No motion')
plt.loglog(w_FC, abs(Hpe_FC_C4), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_position_Hpe), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")
plt.legend(loc='lower left')
plt.grid(True, which="both")

# ----------------- Angle plot H_pe -------------------
# Loop to manually unwrap the phase array
angle_C2_Hpe = np.angle(Hpe_FC_C2)
angle_C4_Hpe = np.angle(Hpe_FC_C4)

for i in range(len(angle_C2_Hpe)-1):
    if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i+1]) >= np.pi:
        angle_C2_Hpe[i+1] = angle_C2_Hpe[i+1] - 2*np.pi

for i in range(len(angle_C4_Hpe)-1):
    if abs(angle_C4_Hpe[i] - angle_C4_Hpe[i+1]) >= np.pi:
        angle_C4_Hpe[i+1] = angle_C4_Hpe[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_position_Hpe)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pe}(jω)$ - Position (C1+C4)")
plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#967BB6', linestyle='-', marker='o', markersize='4', label='No motion')
plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpe), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pe}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()

# --------------------------------- POSITION H_pxd ----------------------------

# Variables:
K_p = 0.6               # Pilot gain
T_L = 0.1               # Lead time constant
T_I = 2.00              # Lag time constant
t_e = 0.10              # Effective time delay
w_nm = 8.0              # Neuromuscular frequency
damping_ratio = 0.10    # Neuromuscular damping ratio

# Model:
Y_p_position_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# ---------- Magnitude plot H_pxd -----------
plt.subplot(121)
plt.title("Magnitude plot - $H_{pxd}(jω)$ - Position (C4)")
plt.loglog(w_FC, abs(Hpxd_FC_C4), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_position_Hpxd), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pxd}(jω)|$")
plt.legend(loc='lower left')
plt.grid(True, which="both")

# ------------- Angle plot H_pxd ------------
# Loop to manually unwrap the phase array
angle_C4_Hpxd = np.angle(Hpxd_FC_C4)

for i in range(len(angle_C4_Hpxd)-1):
    if abs(angle_C4_Hpxd[i] - angle_C4_Hpxd[i+1]) >= np.pi:
        angle_C4_Hpxd[i+1] = angle_C4_Hpxd[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_position_Hpxd)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pxd}(jω)$ - Position (C4)")
plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpxd), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()


"""
-----------------------------------------------------------------------------------
----------------------------------- VELOCITY --------------------------------------
-----------------------------------------------------------------------------------
"""

# --------------------------------- VELOCITY H_pe ----------------------------

# ------- Precision Model for velocity H_pe ----------
# Variables:
K_p = 0.07              # Pilot gain
T_L = 2.1               # Lead time constant
T_I = 0.08              # Lag time constant
t_e = 0.3               # Effective time delay
w_nm = 15.0             # Neuromuscular frequency
damping_ratio = 0.30    # Neuromuscular damping ratio

# Model:
Y_p_velocity_Hpe = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# ------------ Magnitude plot H_pe -------------
plt.subplot(121)
plt.title("Magnitude plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
plt.loglog(w_FC, abs(Hpe_FC_C2), color='#86D7FF', linestyle='-', marker='o', markersize='4', label='No motion')
plt.loglog(w_FC, abs(Hpe_FC_C5), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_velocity_Hpe), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")
plt.legend(loc='upper left')
plt.grid(True, which="both")

# ---------- Angle plot H_pe ------------------
# Loop to manually unwrap the phase array
angle_C2_Hpe = np.angle(Hpe_FC_C2)
angle_C5_Hpe = np.angle(Hpe_FC_C5)

for i in range(len(angle_C2_Hpe)-1):
    if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i+1]) >= np.pi:
        angle_C2_Hpe[i+1] = angle_C2_Hpe[i+1] - 2*np.pi

for i in range(len(angle_C5_Hpe)-1):
    if abs(angle_C5_Hpe[i] - angle_C5_Hpe[i+1]) >= np.pi:
        angle_C5_Hpe[i+1] = angle_C5_Hpe[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_velocity_Hpe)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#86D7FF', linestyle='-', marker='o', markersize='4', label='No motion')
plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpe), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pe}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()

# --------------------------------- VELOCITY H_pxd ----------------------------

# ------------------ Precision Model for Velocity H_pxd ------------------
# Variables:
K_p = 0.07              # Pilot gain
T_L = 2.1               # Lead time constant
T_I = 0.08              # Lag time constant
t_e = 0.3               # Effective time delay
w_nm = 15.0             # Neuromuscular frequency
damping_ratio = 0.30    # Neuromuscular damping ratio

# Model:
Y_p_velocity_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)


# ------------ Magnitude plot H_pxd ------------------
plt.subplot(121)
plt.title("Magnitude plot - $H_{pxd}(jω)$ - Velocity (C5)")
plt.loglog(w_FC, abs(Hpxd_FC_C5), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_position_Hpxd), color='k', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pxd}(jω)|$")
plt.legend(loc='upper left')
plt.grid(True, which="both")

# --------------- Angle plot H_pxd -------------------
# Loop to manually unwrap the phase array
angle_C5_Hpxd = np.angle(Hpxd_FC_C5)

for i in range(len(angle_C5_Hpxd)-1):
    if abs(angle_C5_Hpxd[i] - angle_C5_Hpxd[i+1]) >= np.pi:
        angle_C5_Hpxd[i+1] = angle_C5_Hpxd[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_velocity_Hpxd)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pxd}(jω)$ - Velocity (C5)")
plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpxd), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()

"""
-----------------------------------------------------------------------------------
--------------------------------- ACCELERATION ------------------------------------
-----------------------------------------------------------------------------------
"""

# --------------------------------- ACCELERATION H_pe ----------------------------

# ------------------ Precision Model for Acceleraion H_pe ------------------
# Variables:
K_p = 0.07              # Pilot gain
T_L = 2.1               # Lead time constant
T_I = 0.08              # Lag time constant
t_e = 0.3               # Effective time delay
w_nm = 13.0             # Neuromuscular frequency
damping_ratio = 0.30    # Neuromuscular damping ratio

# Model:
Y_p_acceleration_Hpe = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# --------------- Magnitude plot H_pe ------------------
plt.subplot(121)
plt.title("Magnitude plots - $H_{pe}(jω)$ - Acceleration (C3+C6)")
plt.loglog(w_FC, abs(Hpe_FC_C3), color='#0FF64D', linestyle='-', marker='o', markersize='4', label='No motion')
plt.loglog(w_FC, abs(Hpe_FC_C6), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_acceleration_Hpe), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pe}(jω)|$")
plt.legend(loc='upper left')
plt.grid(True, which="both")

# ------------------ Angle plot H_pe ----------------------
# Loop to manually unwrap the phase array
angle_C3_Hpe = np.angle(Hpe_FC_C3)
for i in range(len(angle_C3_Hpe)-1):
    if abs(angle_C3_Hpe[i] - angle_C3_Hpe[i+1]) >= np.pi:
        angle_C3_Hpe[i+1] = angle_C3_Hpe[i+1] - 2*np.pi

angle_C6_Hpe = np.angle(Hpe_FC_C6)
for i in range(len(angle_C6_Hpe)-1):
    if abs(angle_C6_Hpe[i] - angle_C6_Hpe[i+1]) >= np.pi:
        angle_C6_Hpe[i+1] = angle_C6_Hpe[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_acceleration_Hpe)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pe}(jω)$ - Acceleration (C3+C6)")
plt.semilogx(w_FC, np.rad2deg(angle_C3_Hpe), color='#0FF64D', linestyle='-', marker='o', markersize='4', label='No motion')
plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpe), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pe}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()

# --------------------------------- ACCELERATION H_pxd ----------------------------

# ------------------ Precision Model for Acceleration H_pxd ------------------
# Variables:
K_p = 0.02              # Pilot gain
T_L = 3.1               # Lead time constant
T_I = 0.5               # Lag time constant
t_e = 0.1               # Effective time delay
w_nm = 15.0             # Neuromuscular frequency
damping_ratio = 0.30    # Neuromuscular damping ratio

# Model:
Y_p_acceleration_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# --------------- Magnitude plot H_pxd ------------------
plt.subplot(121)
plt.title("Magnitude plot - $H_{pxd}(jω)$ - Acceleration (C6)")
plt.loglog(w_FC, abs(Hpxd_FC_C6), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
plt.loglog(w_FC, abs(Y_p_acceleration_Hpxd), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel("$|H_{pxd}(jω)|$")
plt.legend(loc='upper left')
plt.grid(True, which="both")

# ------------------ Angle plot H_pxd ----------------------
# Loop to manually unwrap the phase array
angle_C6_Hpxd = np.angle(Hpxd_FC_C6)
for i in range(len(angle_C6_Hpxd)-1):
    if abs(angle_C6_Hpxd[i] - angle_C6_Hpxd[i+1]) >= np.pi:
        angle_C6_Hpxd[i+1] = angle_C6_Hpxd[i+1] - 2*np.pi

angle_y_p = np.angle(Y_p_acceleration_Hpxd)
for i in range(len(angle_y_p)-1):
    if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
        angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi

plt.subplot(122)
plt.title("Phase plot - $H_{pxd}(jω)$ - Acceleration (C6)")
plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpxd), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
plt.xlabel("ω [rad/s]")
plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")
plt.grid(True, which="both")
plt.legend(loc='lower left')
plt.show()





"""
This portion of the code does not affect the actual program, it is used to store previous/deleted
code just in case it might be useful later
"""

# plt.subplot(122)
# plt.title("Phase plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
# #plt.semilogx(w_FC, np.rad2deg(np.unwrap(np.angle(Hpxd_FC_C5))), color='r', linestyle='-', marker='o', markersize='4', label='Not unwrapped')
# plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#86D7FF', linestyle='-', marker='o', markersize='4', label='No motion')
# plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpe), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220"+"$H_{pe}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# #plt.tight_layout()
# plt.show()


""" Function to optimise non-linear cost function: """
# scipy.optimize.fmin

""" Read and print Matlab file """
# print(sorted(datasubj1.keys()))
