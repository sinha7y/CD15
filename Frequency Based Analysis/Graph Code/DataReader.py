import scipy.io
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt


# Read Matlab file
datasubj1 = scipy.io.loadmat("ae2223I_measurement_data_subj1.mat")

# Note:
#     | P   V   A
# _________________
#  NM | C1  C2  C3
#  M  | C4  C5  C6

# ---------------------------------- Variables ---------------------------------
w_FC = datasubj1['w_FC']        # Frequency
t = datasubj1['t'][0]           # Time
data_C1 = datasubj1['data_C1']  # Data Condition 1
data_C2 = datasubj1['data_C2']
data_C3 = datasubj1['data_C3']
data_C4 = datasubj1['data_C4']
data_C5 = datasubj1['data_C5']
data_C6 = datasubj1['data_C6']

# Subvariables for each Condition
# e_C1       = data_C1['e'][0][0].reshape(8192, 5)
# u_C1       = data_C1['u'][0][0].reshape(8192, 5)
# x_C1       = data_C1['x'][0][0].reshape(8192, 5)
# ft_C1      = data_C1['ft']
# fd_C1      = data_C1['fd']
Hpe_FC_C1 = data_C1['Hpe_FC'][0][0]
Hpxd_FC_C1 = data_C1['Hpxd_FC'][0][0]

# e_C2 = data_C2['e'][0][0].reshape(8192, 5)
# u_C2 = data_C2['u'][0][0].reshape(8192, 5)
# x_C2 = data_C2['x'][0][0].reshape(8192, 5)
# ft_C2 = data_C2['ft']
# fd_C2 = data_C2['fd']
Hpe_FC_C2 = data_C2['Hpe_FC'][0][0]
Hpxd_FC_C2 = data_C2['Hpxd_FC'][0][0]

# e_C3 = data_C3['e'][0][0].reshape(8192, 5)
# u_C3 = data_C3['u'][0][0].reshape(8192, 5)
# x_C3 = data_C3['x'][0][0].reshape(8192, 5)
# ft_C3 = data_C3['ft']
# fd_C3 = data_C3['fd']
Hpe_FC_C3 = data_C3['Hpe_FC'][0][0]
Hpxd_FC_C3 = data_C3['Hpxd_FC'][0][0]

# e_C4 = data_C4['e'][0][0].reshape(8192, 5)
# u_C4 = data_C4['u'][0][0].reshape(8192, 5)
# x_C4 = data_C4['x'][0][0].reshape(8192, 5)
# ft_C4 = data_C4['ft']
# fd_C4 = data_C4['fd']
Hpe_FC_C4 = data_C4['Hpe_FC'][0][0]
Hpxd_FC_C4 = data_C4['Hpxd_FC'][0][0]

# e_C5 = data_C5['e'][0][0].reshape(8192, 5)
# u_C5 = data_C5['u'][0][0].reshape(8192, 5)
# x_C5 = data_C5['x'][0][0].reshape(8192, 5)
# ft_C5 = data_C5['ft']
# fd_C5 = data_C5['fd']
Hpe_FC_C5 = data_C5['Hpe_FC'][0][0]
Hpxd_FC_C5 = data_C5['Hpxd_FC'][0][0]

# e_C6 = data_C6['e'][0][0].reshape(8192, 5)
# u_C6 = data_C6['u'][0][0].reshape(8192, 5)
# x_C6 = data_C6['x'][0][0].reshape(8192, 5)
# ft_C6 = data_C6['ft']
# fd_C6 = data_C6['fd']
Hpe_FC_C6 = data_C6['Hpe_FC'][0][0]
Hpxd_FC_C6 = data_C6['Hpxd_FC'][0][0]

# ---------------------------- Precision Model function --------------------------------
j = complex(0, 1)  # Define j

# Precision model function
def Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio):
    return K_p * (T_L * w_FC * j + 1) / (T_I * w_FC * j + 1) * np.exp(-w_FC * j * t_e) * (
                1 / ((w_FC * j / w_nm) * (w_FC * j / w_nm) + (2 * damping_ratio * w_FC * j / w_nm) + 1))


# ---------------------------------------- PLOTS --------------------------------------

"""
-----------------------------------------------------------------------------------
----------------------------------- POSITION --------------------------------------
-----------------------------------------------------------------------------------
"""

# # --------------------------------- POSITION H_pe ----------------------------
#
# # Variables NO MOTION:
# K_p_nomotion = 3                 # Pilot gain
# T_L_nomotion = 0.1               # Lead time constant
# T_I_nomotion = 1.58              # Lag time constant
# t_e_nomotion = 0.10              # Effective time delay
# w_nm_nomotion = 8.0              # Neuromuscular frequency
# damping_ratio_nomotion = 0.10    # Neuromuscular damping ratio
#
# # Model NO MOTION:
# Y_p_position_Hpe_no_motion = Y_p(K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion, damping_ratio_nomotion)
#
# # Variables MOTION:
# K_p_motion = 2                 # Pilot gain
# T_L_motion = 0.2               # Lead time constant
# T_I_motion = 1.85              # Lag time constant
# t_e_motion = 0.20              # Effective time delay
# w_nm_motion = 7.0              # Neuromuscular frequency
# damping_ratio_motion = 0.20    # Neuromuscular damping ratio
#
# # Model MOTION:
# Y_p_position_Hpe_motion = Y_p(K_p_motion, T_L_motion, T_I_motion, t_e_motion, w_nm_motion, damping_ratio_motion)
#
# # -------------- Magnitude plot H_pe ------------------
# plt.subplot(121)
# plt.title("Magnitude plot - $H_{pe}(jω)$ - Position (C1+C4)")
# plt.loglog(w_FC, abs(Hpe_FC_C1), color='#7A5195', linestyle='-', marker='x', markersize='6', label='No motion')
# plt.loglog(w_FC, abs(Y_p_position_Hpe_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6', label='Precision Model - No motion')
# plt.loglog(w_FC, abs(Hpe_FC_C4), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_position_Hpe_motion), color='#FFA600', linestyle='-', marker='o', markersize='4', label='Precision Model - Motion')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pe}(jω)|$")
# plt.legend(loc='lower left')
# plt.grid(True, which="both")
#
# # ----------------- Angle plot H_pe -------------------
# # Loop to manually unwrap the phase array
# angle_C2_Hpe = np.angle(Hpe_FC_C2)
# angle_C5_Hpe = np.angle(Hpe_FC_C4)
#
# for i in range(len(angle_C2_Hpe)-1):
#     if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i+1]) >= np.pi:
#         angle_C2_Hpe[i+1] = angle_C2_Hpe[i+1] - 2*np.pi
#
# for i in range(len(angle_C4_Hpe)-1):
#     if abs(angle_C4_Hpe[i] - angle_C4_Hpe[i+1]) >= np.pi:
#         angle_C4_Hpe[i+1] = angle_C4_Hpe[i+1] - 2*np.pi

# angle_y_p_no_motion = np.angle(Y_p_position_Hpe_no_motion)
# for i in range(len(angle_y_p_no_motion)-1):
#     if abs(angle_y_p_no_motion[i] - angle_y_p_no_motion[i+1]) >= np.pi:
#         angle_y_p_no_motion[i+1] = angle_y_p_no_motion[i+1] - 2*np.pi
#
# angle_y_p_motion = np.angle(Y_p_position_Hpe_motion)
# for i in range(len(angle_y_p_motion)-1):
#     if abs(angle_y_p_motion[i] - angle_y_p_motion[i+1]) >= np.pi:
#         angle_y_p_motion[i+1] = angle_y_p_motion[i+1] - 2*np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pe}(jω)$ - Position (C1+C4)")
# plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#7A5195', linestyle='-', marker='x', markersize='6', label='No motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6', label='Precision Model - No motion')
# plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpe), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4', label='Precision Model - Motion')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220"+"$H_{pe}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()
# --------------------------- Cost function and optimisation H_pe ----------------------

# Loop to manually unwrap the phase array
angle_C1_Hpe = np.angle(Hpe_FC_C1)

for i in range(len(angle_C1_Hpe) - 1):
    if abs(angle_C1_Hpe[i] - angle_C1_Hpe[i + 1]) >= np.pi:
        angle_C1_Hpe[i + 1] = angle_C1_Hpe[i + 1] - 2 * np.pi


def costfunction_nomotion(variables):
    J = 0  # Define cost function J
    W = 1  # Weight
    # Precision model function for H_pe
    Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                      variables[5])

    # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    angle_y_p = np.angle(Y_precision)
    for i in range(len(angle_y_p) - 1):
        if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
            angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        #J += W * (abs(Hpe_FC_C1[i]) - abs(Y_precision[i])) ** 2 + W * (angle_C1_Hpe[i] - angle_y_p[i]) ** 2
        J += W * abs((Hpe_FC_C1[i] - Y_precision[i]) ** 2)
    return J


angle_C4_Hpe = np.angle(Hpe_FC_C4)

for i in range(len(angle_C4_Hpe) - 1):
    if abs(angle_C4_Hpe[i] - angle_C4_Hpe[i + 1]) >= np.pi:
        angle_C4_Hpe[i + 1] = angle_C4_Hpe[i + 1] - 2 * np.pi


def costfunction_motion(variables):
    J = 0        # Define cost function J
    W_abs = 1    # Weight
    W_angle = 1  # Weight
    # Precision model function for H_pe
    Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                          variables[5])
    # Precision model function for H_pxd
    Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                           variables[5])

    # # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    # angle_y_p_Hpe = np.angle(Y_precision_Hpe)
    # for i in range(len(angle_y_p_Hpe) - 1):
    #     if abs(angle_y_p_Hpe[i] - angle_y_p_Hpe[i + 1]) >= np.pi:
    #         angle_y_p_Hpe[i + 1] = angle_y_p_Hpe[i + 1] - 2 * np.pi
    #
    # angle_y_p_Hpxd = np.angle(Y_precision_Hpxd)
    # for i in range(len(angle_y_p_Hpxd) - 1):
    #     if abs(angle_y_p_Hpxd[i] - angle_y_p_Hpxd[i + 1]) >= np.pi:
    #         angle_y_p_Hpxd[i + 1] = angle_y_p_Hpxd[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        #J += W_abs * (abs(Hpe_FC_C4[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C4_Hpe[i] - angle_y_p[i]) ** 2
        J += W_abs * abs((Hpe_FC_C4[i] - Y_precision_Hpe[i]) ** 2) + abs((Hpxd_FC_C4[i] - Y_precision_Hpxd[i]) ** 2)
    return J


# Initial guess NO MOTION:
K_p_nomotion = 3     # Pilot gain
T_L_nomotion = 0.1   # Lead time constant
T_I_nomotion = 1.58  # Lag time constant
t_e_nomotion = 0.10  # Effective time delay
w_nm_nomotion = 8.0  # Neuromuscular frequency
damping_ratio_nomotion = 0.10  # Neuromuscular damping ratio
guess_position_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                               damping_ratio_nomotion]

# Initial guess MOTION:
K_p_motion_Hpe = 2     # Pilot gain for H_pe
T_L_motion_Hpe = 0.2   # Lead time constant for H_pe
T_I_motion_Hpe = 1.85  # Lag time constant for H_pe
t_e_motion_Hpe = 0.20  # Effective time delay for H_pe
w_nm_motion = 7.0      # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
damping_ratio_motion = 0.20  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
K_p_motion_Hpxd = 2     # Pilot gain for H_pxd
T_L_motion_Hpxd = 0.2   # Lead time constant for H_pxd
T_I_motion_Hpxd = 1.85  # Lag time constant for H_pxd
t_e_motion_Hpxd = 0.20  # Effective time delay for H_pxd
guess_position_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion, damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd, t_e_motion_Hpxd]

# NOTE: Guess is called H_pe, but contains also H_pxd

# Optimise the function, Y_p_position_Hpe is initial guess
minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_position_Hpe_nomotion, retall=True)
minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_position_Hpe_motion, retall=True)

length = max(len(minimumcost_nomotion[1]), len(minimumcost_motion[1]))

# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
for i in range(0, length, 30):
    # Account for different number of iterations
    # No motion
    if i >= len(minimumcost_nomotion[1]):
        h = len(minimumcost_nomotion[1]) - 1
    else: h = i
    # Motion
    if i >= len(minimumcost_motion[1]):
        k = len(minimumcost_motion[1]) - 1
    else: k = i

    Y_p_position_Hpe_no_motion = Y_p(minimumcost_nomotion[1][h][0], minimumcost_nomotion[1][h][1], minimumcost_nomotion[1][h][2],
                                     minimumcost_nomotion[1][h][3], minimumcost_nomotion[1][h][4], minimumcost_nomotion[1][h][5])
    Y_p_position_Hpe_motion = Y_p(minimumcost_motion[1][k][0], minimumcost_motion[1][k][1], minimumcost_motion[1][k][2],
                                  minimumcost_motion[1][k][3], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])
    # Y_p_position_Hpxd_motion = Y_p(minimumcost_motion[1][k][6], minimumcost_motion[1][k][7], minimumcost_motion[1][k][8],
    #                                minimumcost_motion[1][k][9], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])

    # Delete previous plot at each iteration
    plt.clf()

    # -------------- Magnitude plot H_pe ------------------
    plt.subplot(131)
    plt.title("Magnitude plot - $H_{pe}(jω)$ - Position (C1+C4)")
    plt.loglog(w_FC, abs(Hpe_FC_C1), color='#7A5195', linestyle='-', marker='x', markersize='6', label='No motion')
    plt.loglog(w_FC, abs(Y_p_position_Hpe_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
               label='Precision Model - No motion')
    plt.loglog(w_FC, abs(Hpe_FC_C4), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_position_Hpe_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pe}(jω)|$")
    leg = plt.legend(loc='lower left', fontsize=7)
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_no_motion = np.angle(Y_p_position_Hpe_no_motion)
    for l in range(len(angle_y_p_no_motion) - 1):
        if abs(angle_y_p_no_motion[l] - angle_y_p_no_motion[l + 1]) >= np.pi:
            angle_y_p_no_motion[l + 1] = angle_y_p_no_motion[l + 1] - 2 * np.pi

    angle_y_p_motion = np.angle(Y_p_position_Hpe_motion)
    for m in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[m] - angle_y_p_motion[m + 1]) >= np.pi:
            angle_y_p_motion[m + 1] = angle_y_p_motion[m + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pe}(jω)$ - Position (C1+C4)")
    plt.semilogx(w_FC, np.rad2deg(angle_C1_Hpe), color='#7A5195', linestyle='-', marker='x', markersize='6',
                 label='No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
                 label='Precision Model - No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpe), color='#EF5675', linestyle='-', marker='o', markersize='4',
                 label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left', fontsize=10)

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(max(h, k)), horizontalalignment='center', verticalalignment='center', fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0., 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.7, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.775, "no motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(0.7, 0.7, guess_position_Hpe_nomotion[0], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(0.7, 0.6, guess_position_Hpe_nomotion[1], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(0.7, 0.5, guess_position_Hpe_nomotion[2], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(0.7, 0.4, guess_position_Hpe_nomotion[3], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(0.7, 0.3, guess_position_Hpe_nomotion[4], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(0.7, 0.2, guess_position_Hpe_nomotion[5], horizontalalignment='center', verticalalignment='center', fontsize=10)

    plt.text(1, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(1, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(1, 0.775, "motion", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')

    plt.text(1, 0.7, guess_position_Hpe_motion[0], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(1, 0.6, guess_position_Hpe_motion[1], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(1, 0.5, guess_position_Hpe_motion[2], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(1, 0.4, guess_position_Hpe_motion[3], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(1, 0.3, guess_position_Hpe_motion[4], horizontalalignment='center', verticalalignment='center', fontsize=10)
    plt.text(1, 0.2, guess_position_Hpe_motion[5], horizontalalignment='center', verticalalignment='center', fontsize=10)

    plt.text(0.2, 0.8, "No motion", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(0.2, 0.7, round(minimumcost_nomotion[1][h][0], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.6, round(minimumcost_nomotion[1][h][1], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.5, round(minimumcost_nomotion[1][h][2], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.4, round(minimumcost_nomotion[1][h][3], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.3, round(minimumcost_nomotion[1][h][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.2, round(minimumcost_nomotion[1][h][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.text(0.45, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(0.45, 0.7, round(minimumcost_motion[1][k][0], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.6, round(minimumcost_motion[1][k][1], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.5, round(minimumcost_motion[1][k][2], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.4, round(minimumcost_motion[1][k][3], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
plt.show()

# --------------------------------- POSITION H_pxd ----------------------------

# # Variables:
# K_p = 0.6               # Pilot gain
# T_L = 0.1               # Lead time constant
# T_I = 2.00              # Lag time constant
# t_e = 0.10              # Effective time delay
# w_nm = 8.0              # Neuromuscular frequency
# damping_ratio = 0.10    # Neuromuscular damping ratio
#
# # Model:
# Y_p_position_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)

# # ---------- Magnitude plot H_pxd -----------
# plt.subplot(121)
# plt.title("Magnitude plot - $H_{pxd}(jω)$ - Position (C4)")
# plt.loglog(w_FC, abs(Hpxd_FC_C4), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_position_Hpxd), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pxd}(jω)|$")
# plt.legend(loc='lower left')
# plt.grid(True, which="both")

# # ------------- Angle plot H_pxd ------------
# # Loop to manually unwrap the phase array
# angle_C4_Hpxd = np.angle(Hpxd_FC_C4)
#
# for i in range(len(angle_C4_Hpxd)-1):
#     if abs(angle_C4_Hpxd[i] - angle_C4_Hpxd[i+1]) >= np.pi:
#         angle_C4_Hpxd[i+1] = angle_C4_Hpxd[i+1] - 2*np.pi
#
# angle_y_p = np.angle(Y_p_position_Hpxd)
# for i in range(len(angle_y_p)-1):
#     if abs(angle_y_p[i] - angle_y_p[i+1]) >= np.pi:
#         angle_y_p[i+1] = angle_y_p[i+1] - 2*np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pxd}(jω)$ - Position (C4)")
# plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpxd), color='r', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4', label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220"+"$H_{pxd}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()

# --------------------------- Cost function and optimisation H_pxd ----------------------


# def costfunction_motion(variables):
#     J = 0        # Define cost function J
#     W_abs = 20   # Weight absolute value
#     W_angle = 1  # Weight angle
#     Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
#                       variables[5])
#
#     # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
#     angle_y_p = np.angle(Y_precision)
#     for i in range(len(angle_y_p) - 1):
#         if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#             angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
#     # Sum each element (response and model at each frequency) to get the cost
#     for i in range(len(w_FC)):
#         # Function only takes an array of variables instead of individual variables
#         #J += W_abs * (abs(Hpxd_FC_C4[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C4_Hpxd[i] - angle_y_p[i]) ** 2
#         J += W_abs * abs((Hpxd_FC_C4[i] - Y_precision[i]) ** 2)
#     return J
#
#
# # Initial guess MOTION:
# K_p_motion = 0.6   # Pilot gain
# T_L_motion = 0.1   # Lead time constant
# T_I_motion = 2.00  # Lag time constant
# t_e_motion = 0.10  # Effective time delay
# w_nm_motion = 8.0  # Neuromuscular frequency
# damping_ratio_motion = 0.10  # Neuromuscular damping ratio
# guess_position_Hpxd_motion = [K_p_motion, T_L_motion, T_I_motion, t_e_motion, w_nm_motion, damping_ratio_motion]

# Optimise the function, Y_p_position_Hpe is initial guess
#minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_position_Hpxd_motion, retall=True)

# Loop to manually unwrap the phase array
angle_C4_Hpxd = np.angle(Hpxd_FC_C4)

for i in range(len(angle_C4_Hpxd) - 1):
    if abs(angle_C4_Hpxd[i] - angle_C4_Hpxd[i + 1]) >= np.pi:
        angle_C4_Hpxd[i + 1] = angle_C4_Hpxd[i + 1] - 2 * np.pi

# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
# for iteration in minimumcost_motion[1][::30]:
for k in range(0, len(minimumcost_motion[1]), 30):

    Y_p_position_Hpxd_motion = Y_p(minimumcost_motion[1][k][6], minimumcost_motion[1][k][7], minimumcost_motion[1][k][8],
                                   minimumcost_motion[1][k][9], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])
    # Delete previous plot at each iteration
    plt.clf()

    # ---------- Magnitude plot H_pxd -----------
    plt.subplot(131)
    plt.title("Magnitude plot - $H_{pxd}(jω)$ - Position (C4)")
    plt.loglog(w_FC, abs(Hpxd_FC_C4), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_position_Hpxd_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pxd}(jω)|$")
    plt.legend(loc='lower left')
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_motion = np.angle(Y_p_position_Hpxd_motion)
    for i in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[i] - angle_y_p_motion[i + 1]) >= np.pi:
            angle_y_p_motion[i + 1] = angle_y_p_motion[i + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pxd}(jω)$ - Position (C4)")
    plt.semilogx(w_FC, np.rad2deg(angle_C4_Hpxd), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pxd}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(k), horizontalalignment='center', verticalalignment='center',
             fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0.2, 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.8, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.8, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')

    plt.text(0.8, 0.7, guess_position_Hpe_motion[6], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.6, guess_position_Hpe_motion[7], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.5, guess_position_Hpe_motion[8], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.4, guess_position_Hpe_motion[9], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.3, guess_position_Hpe_motion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.2, guess_position_Hpe_motion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(0.5, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.5, 0.7, round(minimumcost_motion[1][k][6], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.6, round(minimumcost_motion[1][k][7], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.5, round(minimumcost_motion[1][k][8], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.4, round(minimumcost_motion[1][k][9], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
plt.show()

"""
-----------------------------------------------------------------------------------
----------------------------------- VELOCITY --------------------------------------
-----------------------------------------------------------------------------------
"""

# --------------------------------- VELOCITY H_pe ----------------------------

# # ------- Precision Model for velocity H_pe ----------
# # Variables:
# K_p = 0.07  # Pilot gain
# T_L = 2.1  # Lead time constant
# T_I = 0.08  # Lag time constant
# t_e = 0.3  # Effective time delay
# w_nm = 15.0  # Neuromuscular frequency
# damping_ratio = 0.30  # Neuromuscular damping ratio
#
# # Model:
# Y_p_velocity_Hpe = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)
#
# # ------------ Magnitude plot H_pe -------------
# plt.subplot(121)
# plt.title("Magnitude plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
# plt.loglog(w_FC, abs(Hpe_FC_C2), color='#86D7FF', linestyle='-', marker='o', markersize='4', label='No motion')
# plt.loglog(w_FC, abs(Hpe_FC_C5), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_velocity_Hpe), color='black', linestyle='-', marker='o', markersize='4',
#            label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pe}(jω)|$")
# plt.legend(loc='upper left')
# plt.grid(True, which="both")
#
# # ---------- Angle plot H_pe ------------------
# # Loop to manually unwrap the phase array
# angle_C2_Hpe = np.angle(Hpe_FC_C2)
# angle_C5_Hpe = np.angle(Hpe_FC_C5)
#
# for i in range(len(angle_C2_Hpe) - 1):
#     if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i + 1]) >= np.pi:
#         angle_C2_Hpe[i + 1] = angle_C2_Hpe[i + 1] - 2 * np.pi
#
# for i in range(len(angle_C5_Hpe) - 1):
#     if abs(angle_C5_Hpe[i] - angle_C5_Hpe[i + 1]) >= np.pi:
#         angle_C5_Hpe[i + 1] = angle_C5_Hpe[i + 1] - 2 * np.pi
#
# angle_y_p = np.angle(Y_p_velocity_Hpe)
# for i in range(len(angle_y_p) - 1):
#     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
# plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#86D7FF', linestyle='-', marker='o', markersize='4',
#              label='No motion')
# plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpe), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4',
#              label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()

# --------------------------- Cost function and optimisation H_pe ----------------------

# Loop to manually unwrap the phase array
angle_C2_Hpe = np.angle(Hpe_FC_C2)

for i in range(len(angle_C2_Hpe) - 1):
    if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i + 1]) >= np.pi:
        angle_C2_Hpe[i + 1] = angle_C2_Hpe[i + 1] - 2 * np.pi


def costfunction_nomotion(variables):
    J = 0        # Define cost function J
    W_abs = 1    # Weight
    W_angle = 1  # Weight
    Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                      variables[5])  # Precision model function

    # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    angle_y_p = np.angle(Y_precision)
    for i in range(len(angle_y_p) - 1):
        if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
            angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        #J += W_abs * (abs(Hpe_FC_C2[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C2_Hpe[i] - angle_y_p[i]) ** 2
        J += W_abs * abs((Hpe_FC_C2[i] - Y_precision[i]) ** 2)
    return J

angle_C5_Hpe = np.angle(Hpe_FC_C5)

for i in range(len(angle_C5_Hpe) - 1):
    if abs(angle_C5_Hpe[i] - angle_C5_Hpe[i + 1]) >= np.pi:
        angle_C5_Hpe[i + 1] = angle_C5_Hpe[i + 1] - 2 * np.pi


def costfunction_motion(variables):
    J = 0        # Define cost function J
    W_abs = 1    # Weight
    W_angle = 1  # Weight

    # Precision model function for H_pe
    Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                          variables[5])
    # Precision model function for H_pxd
    Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                           variables[5])

    # # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    # angle_y_p = np.angle(Y_precision)
    # for i in range(len(angle_y_p) - 1):
    #     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
    #         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        #J += W_abs * (abs(Hpe_FC_C5[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C5_Hpe[i] - angle_y_p[i]) ** 2
        #J += W_abs * abs((Hpe_FC_C5[i] - Y_precision[i]) ** 2)
        J += W_abs * abs((Hpe_FC_C5[i] - Y_precision_Hpe[i]) ** 2) + abs((Hpxd_FC_C5[i] - Y_precision_Hpxd[i]) ** 2)
    return J


# Initial guess NO MOTION:
K_p_nomotion = 0.07             # Pilot gain
T_L_nomotion = 2.1              # Lead time constant
T_I_nomotion = 0.08             # Lag time constant
t_e_nomotion = 0.3              # Effective time delay
w_nm_nomotion = 15.0            # Neuromuscular frequency
damping_ratio_nomotion = 0.30   # Neuromuscular damping ratio
guess_velocity_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                               damping_ratio_nomotion]

# Initial guess MOTION:
K_p_motion_Hpe = 0.09   # Pilot gain for H_pe
T_L_motion_Hpe = 3.1    # Lead time constant for H_pe
T_I_motion_Hpe = 0.10   # Lag time constant for H_pe
t_e_motion_Hpe = 0.20   # Effective time delay for H_pe
w_nm_motion = 14.0      # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
damping_ratio_motion = 0.40  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
K_p_motion_Hpxd = 0.07  # Pilot gain for H_pxd
T_L_motion_Hpxd = 2.1   # Lead time constant for H_pxd
T_I_motion_Hpxd = 0.08  # Lag time constant for H_pxd
t_e_motion_Hpxd = 0.3   # Effective time delay for H_pxd
guess_velocity_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion, damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd, t_e_motion_Hpxd]

# NOTE: Guess is called H_pe, but contains also H_pxd

# Optimise the function, Y_p_position_Hpe is initial guess
minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_velocity_Hpe_nomotion, retall=True)
minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_velocity_Hpe_motion, retall=True)

length = max(len(minimumcost_nomotion[1]), len(minimumcost_motion[1]))

# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
for i in range(0, length, 30):  # [::30]:
    # Account for different number of iterations
    # No motion
    if i >= len(minimumcost_nomotion[1]):
        h = len(minimumcost_nomotion[1]) - 1
    else: h = i
    # Motion
    if i >= len(minimumcost_motion[1]):
        k = len(minimumcost_motion[1]) - 1
    else: k = i

    Y_p_velocity_Hpe_no_motion = Y_p(minimumcost_nomotion[1][h][0], minimumcost_nomotion[1][h][1], minimumcost_nomotion[1][h][2],
                                     minimumcost_nomotion[1][h][3], minimumcost_nomotion[1][h][4], minimumcost_nomotion[1][h][5])
    Y_p_velocity_Hpe_motion = Y_p(minimumcost_motion[1][k][0], minimumcost_motion[1][k][1], minimumcost_motion[1][k][2],
                                  minimumcost_motion[1][k][3], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])

    # Delete previous plot at each iteration
    plt.clf()

    # -------------- Magnitude plot H_pe ------------------
    plt.subplot(131)
    plt.title("Magnitude plots - $H_{pe}(jω)$ - Velocity (C2+C5)")
    plt.loglog(w_FC, abs(Hpe_FC_C2), color='#7A5195', linestyle='-', marker='x', markersize='6', label='No motion')
    plt.loglog(w_FC, abs(Y_p_velocity_Hpe_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
               label='Precision Model - No motion')
    plt.loglog(w_FC, abs(Hpe_FC_C5), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_velocity_Hpe_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pe}(jω)|$")
    plt.legend(loc='upper left')
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_no_motion = np.angle(Y_p_velocity_Hpe_no_motion)
    for l in range(len(angle_y_p_no_motion) - 1):
        if abs(angle_y_p_no_motion[l] - angle_y_p_no_motion[l + 1]) >= np.pi:
            angle_y_p_no_motion[l + 1] = angle_y_p_no_motion[l + 1] - 2 * np.pi

    angle_y_p_motion = np.angle(Y_p_velocity_Hpe_motion)
    for m in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[m] - angle_y_p_motion[m + 1]) >= np.pi:
            angle_y_p_motion[m + 1] = angle_y_p_motion[m + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
    plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#7A5195', linestyle='-', marker='x', markersize='6',
                 label='No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
                 label='Precision Model - No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpe), color='#EF5675', linestyle='-', marker='o', markersize='4',
                 label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(max(h, k)), horizontalalignment='center', verticalalignment='center',
             fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0., 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.7, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.775, "no motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(0.7, 0.7, guess_velocity_Hpe_nomotion[0], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.6, guess_velocity_Hpe_nomotion[1], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.5, guess_velocity_Hpe_nomotion[2], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.4, guess_velocity_Hpe_nomotion[3], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.3, guess_velocity_Hpe_nomotion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.2, guess_velocity_Hpe_nomotion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(1, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(1, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(1, 0.775, "motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(1, 0.7, guess_velocity_Hpe_motion[0], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.6, guess_velocity_Hpe_motion[1], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.5, guess_velocity_Hpe_motion[2], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.4, guess_velocity_Hpe_motion[3], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.3, guess_velocity_Hpe_motion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.2, guess_velocity_Hpe_motion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(0.2, 0.8, "No motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.2, 0.7, round(minimumcost_nomotion[1][h][0], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.6, round(minimumcost_nomotion[1][h][1], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.5, round(minimumcost_nomotion[1][h][2], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.4, round(minimumcost_nomotion[1][h][3], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.3, round(minimumcost_nomotion[1][h][4], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.2, round(minimumcost_nomotion[1][h][5], 3), horizontalalignment='center',
             verticalalignment='center')

    plt.text(0.45, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.45, 0.7, round(minimumcost_motion[1][k][0], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.6, round(minimumcost_motion[1][k][1], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.5, round(minimumcost_motion[1][k][2], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.4, round(minimumcost_motion[1][k][3], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
plt.show()


# --------------------------------- VELOCITY H_pxd ----------------------------

# # ------------------ Precision Model for Velocity H_pxd ------------------
# # Variables:
# K_p = 0.07  # Pilot gain
# T_L = 2.1  # Lead time constant
# T_I = 0.08  # Lag time constant
# t_e = 0.3  # Effective time delay
# w_nm = 15.0  # Neuromuscular frequency
# damping_ratio = 0.30  # Neuromuscular damping ratio
#
# # Model:
# Y_p_velocity_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)
#
# # ------------ Magnitude plot H_pxd ------------------
# plt.subplot(121)
# plt.title("Magnitude plot - $H_{pxd}(jω)$ - Velocity (C5)")
# plt.loglog(w_FC, abs(Hpxd_FC_C5), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_velocity_Hpxd), color='k', linestyle='-', marker='o', markersize='4', label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pxd}(jω)|$")
# plt.legend(loc='upper left')
# plt.grid(True, which="both")
#
# # --------------- Angle plot H_pxd -------------------
# # Loop to manually unwrap the phase array
# angle_C5_Hpxd = np.angle(Hpxd_FC_C5)
#
# for i in range(len(angle_C5_Hpxd) - 1):
#     if abs(angle_C5_Hpxd[i] - angle_C5_Hpxd[i + 1]) >= np.pi:
#         angle_C5_Hpxd[i + 1] = angle_C5_Hpxd[i + 1] - 2 * np.pi
#
# angle_y_p = np.angle(Y_p_velocity_Hpxd)
# for i in range(len(angle_y_p) - 1):
#     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pxd}(jω)$ - Velocity (C5)")
# plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpxd), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4',
#              label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220" + "$H_{pxd}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()

# --------------------------- Cost function and optimisation H_pxd ----------------------

# def costfunction_motion(variables):
#     J = 0         # Define cost function J
#     W_abs = 1     # Weight absolute value
#     W_angle = 1   # Weight angle
#     Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
#                      variables[5])
#
#     # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
#     angle_y_p = np.angle(Y_precision)
#     for i in range(len(angle_y_p) - 1):
#         if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#             angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
#     # Sum each element (response and model at each frequency) to get the cost
#     for i in range(len(w_FC)):
#         # Function only takes an array of variables instead of individual variables
#         #J += W_abs * (abs(Hpxd_FC_C5[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C5_Hpxd[i] - angle_y_p[i]) ** 2
#         J += W_abs * abs((Hpxd_FC_C5[i] - Y_precision[i]) ** 2)
#     return J
#
# # Initial guess MOTION:
# K_p_motion = 0.07   # Pilot gain
# T_L_motion = 2.1    # Lead time constant
# T_I_motion = 0.08   # Lag time constant
# t_e_motion = 0.3    # Effective time delay
# w_nm_motion = 15.0  # Neuromuscular frequency
# damping_ratio_motion = 0.30  # Neuromuscular damping ratio
# guess_velocity_Hpxd_motion = [K_p_motion, T_L_motion, T_I_motion, t_e_motion, w_nm_motion, damping_ratio_motion]
#
#
# # Optimise the function, Y_p_position_Hpe is initial guess
# minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_velocity_Hpxd_motion, retall=True)

# Loop to manually unwrap the phase array
angle_C5_Hpxd = np.angle(Hpxd_FC_C5)

for i in range(len(angle_C5_Hpxd) - 1):
    if abs(angle_C5_Hpxd[i] - angle_C5_Hpxd[i + 1]) >= np.pi:
        angle_C5_Hpxd[i + 1] = angle_C5_Hpxd[i + 1] - 2 * np.pi


# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
# for iteration in minimumcost_motion[1][::30]:
#     Y_p_velocity_Hpxd_motion = Y_p(iteration[0], iteration[1], iteration[2], iteration[3], iteration[4], iteration[5])
for k in range(0, len(minimumcost_motion[1]), 30):
    Y_p_velocity_Hpxd_motion = Y_p(minimumcost_motion[1][k][6], minimumcost_motion[1][k][7],
                                   minimumcost_motion[1][k][8],
                                   minimumcost_motion[1][k][9], minimumcost_motion[1][k][4],
                                   minimumcost_motion[1][k][5])
    # Delete previous plot at each iteration
    plt.clf()

    # ---------- Magnitude plot H_pxd -----------
    plt.subplot(131)
    plt.title("Magnitude plot - $H_{pxd}(jω)$ - Velocity (C5)")
    plt.loglog(w_FC, abs(Hpxd_FC_C5), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_velocity_Hpxd_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pxd}(jω)|$")
    plt.legend(loc='upper right')
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_motion = np.angle(Y_p_velocity_Hpxd_motion)
    for i in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[i] - angle_y_p_motion[i + 1]) >= np.pi:
            angle_y_p_motion[i + 1] = angle_y_p_motion[i + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pxd}(jω)$ - Velocity (C5)")
    plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpxd), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pxd}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(k), horizontalalignment='center', verticalalignment='center',
             fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0.2, 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.8, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.8, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(0.8, 0.7, guess_velocity_Hpe_motion[6], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.6, guess_velocity_Hpe_motion[7], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.5, guess_velocity_Hpe_motion[8], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.4, guess_velocity_Hpe_motion[9], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.3, guess_velocity_Hpe_motion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.2, guess_velocity_Hpe_motion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(0.5, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.5, 0.7, round(minimumcost_motion[1][k][6], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.6, round(minimumcost_motion[1][k][7], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.5, round(minimumcost_motion[1][k][8], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.4, round(minimumcost_motion[1][k][9], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
plt.show()


"""
-----------------------------------------------------------------------------------
--------------------------------- ACCELERATION ------------------------------------
-----------------------------------------------------------------------------------
"""

# --------------------------------- ACCELERATION H_pe ----------------------------
#
# # ------------------ Precision Model for Acceleraion H_pe ------------------
# # Variables:
# K_p = 0.07   # Pilot gain
# T_L = 2.1    # Lead time constant
# T_I = 0.08   # Lag time constant
# t_e = 0.3    # Effective time delay
# w_nm = 13.0  # Neuromuscular frequency
# damping_ratio = 0.30  # Neuromuscular damping ratio
#
# # Model:
# Y_p_acceleration_Hpe = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)
#
# # --------------- Magnitude plot H_pe ------------------
# plt.subplot(121)
# plt.title("Magnitude plots - $H_{pe}(jω)$ - Acceleration (C3+C6)")
# plt.loglog(w_FC, abs(Hpe_FC_C3), color='#0FF64D', linestyle='-', marker='o', markersize='4', label='No motion')
# plt.loglog(w_FC, abs(Hpe_FC_C6), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_acceleration_Hpe), color='black', linestyle='-', marker='o', markersize='4',
#            label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pe}(jω)|$")
# plt.legend(loc='upper left')
# plt.grid(True, which="both")
#
# # ------------------ Angle plot H_pe ----------------------
# # Loop to manually unwrap the phase array
# angle_C3_Hpe = np.angle(Hpe_FC_C3)
# for i in range(len(angle_C3_Hpe) - 1):
#     if abs(angle_C3_Hpe[i] - angle_C3_Hpe[i + 1]) >= np.pi:
#         angle_C3_Hpe[i + 1] = angle_C3_Hpe[i + 1] - 2 * np.pi
#
# angle_C6_Hpe = np.angle(Hpe_FC_C6)
# for i in range(len(angle_C6_Hpe) - 1):
#     if abs(angle_C6_Hpe[i] - angle_C6_Hpe[i + 1]) >= np.pi:
#         angle_C6_Hpe[i + 1] = angle_C6_Hpe[i + 1] - 2 * np.pi
#
# angle_y_p = np.angle(Y_p_acceleration_Hpe)
# for i in range(len(angle_y_p) - 1):
#     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pe}(jω)$ - Acceleration (C3+C6)")
# plt.semilogx(w_FC, np.rad2deg(angle_C3_Hpe), color='#0FF64D', linestyle='-', marker='o', markersize='4',
#              label='No motion')
# plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpe), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4',
#              label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()

# --------------------------- Cost function and optimisation H_pe ----------------------

# Loop to manually unwrap the phase array
angle_C3_Hpe = np.angle(Hpe_FC_C3)

for i in range(len(angle_C3_Hpe) - 1):
    if abs(angle_C3_Hpe[i] - angle_C3_Hpe[i + 1]) >= np.pi:
        angle_C3_Hpe[i + 1] = angle_C3_Hpe[i + 1] - 2 * np.pi


def costfunction_nomotion(variables):
    J = 0        # Define cost function J
    W_abs = 1    # Weight
    W_angle = 1  # Weight
    Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                      variables[5])  # Precision model function

    # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    angle_y_p = np.angle(Y_precision)
    for i in range(len(angle_y_p) - 1):
        if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
            angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        #J += W_abs * (abs(Hpe_FC_C3[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C3_Hpe[i] - angle_y_p[i]) ** 2
        J += W_abs * abs((Hpe_FC_C3[i] - Y_precision[i]) ** 2)
    return J

angle_C6_Hpe = np.angle(Hpe_FC_C6)

for i in range(len(angle_C6_Hpe) - 1):
    if abs(angle_C6_Hpe[i] - angle_C6_Hpe[i + 1]) >= np.pi:
        angle_C6_Hpe[i + 1] = angle_C6_Hpe[i + 1] - 2 * np.pi


def costfunction_motion(variables):
    J = 0        # Define cost function J
    W_abs = 1    # Weight
    W_angle = 1  # Weight

    # Precision model function for H_pe
    Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                          variables[5])
    # Precision model function for H_pxd
    Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                           variables[5])

    # # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    # angle_y_p = np.angle(Y_precision)
    # for i in range(len(angle_y_p) - 1):
    #     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
    #         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        # J += W_abs * (abs(Hpe_FC_C6[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C6_Hpe[i] - angle_y_p[i]) ** 2
        # J += W_abs * abs((Hpe_FC_C6[i] - Y_precision[i]) ** 2)
        J += W_abs * abs((Hpe_FC_C6[i] - Y_precision_Hpe[i]) ** 2) + abs((Hpxd_FC_C6[i] - Y_precision_Hpxd[i]) ** 2)

    return J


# Initial guess NO MOTION:
K_p_nomotion = 0.07             # Pilot gain
T_L_nomotion = 2.1              # Lead time constant
T_I_nomotion = 0.08             # Lag time constant
t_e_nomotion = 0.3              # Effective time delay
w_nm_nomotion = 13.0            # Neuromuscular frequency
damping_ratio_nomotion = 0.30   # Neuromuscular damping ratio
guess_acceleration_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                                   damping_ratio_nomotion]

# Initial guess MOTION:
K_p_motion_Hpe = 0.08   # Pilot gain for H_pe
T_L_motion_Hpe = 2.3    # Lead time constant for H_pe
T_I_motion_Hpe = 0.09   # Lag time constant for H_pe
t_e_motion_Hpe = 0.20   # Effective time delay for H_pe
w_nm_motion = 14.0      # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
damping_ratio_motion = 0.35  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
K_p_motion_Hpxd = 0.02  # Pilot gain for H_pxd
T_L_motion_Hpxd = 3.1   # Lead time constant for H_pxd
T_I_motion_Hpxd = 0.50  # Lag time constant for H_pxd
t_e_motion_Hpxd = 0.1   # Effective time delay for H_pxd
guess_acceleration_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion, damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd, t_e_motion_Hpxd]

# NOTE: Guess is called H_pe, but contains also H_pxd

# Optimisation function
minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_acceleration_Hpe_nomotion, retall=True)
minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_acceleration_Hpe_motion, retall=True)

length = max(len(minimumcost_nomotion[1]), len(minimumcost_motion[1]))

# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
for i in range(0, length, 30):  # [::30]:
    # Account for different number of iterations
    # No motion
    if i >= len(minimumcost_nomotion[1]):
        h = len(minimumcost_nomotion[1]) - 1
    else: h = i
    # Motion
    if i >= len(minimumcost_motion[1]):
        k = len(minimumcost_motion[1]) - 1
    else: k = i

    Y_p_acceleration_Hpe_no_motion = Y_p(minimumcost_nomotion[1][h][0], minimumcost_nomotion[1][h][1], minimumcost_nomotion[1][h][2],
                                         minimumcost_nomotion[1][h][3], minimumcost_nomotion[1][h][4], minimumcost_nomotion[1][h][5])
    Y_p_acceleration_Hpe_motion = Y_p(minimumcost_motion[1][k][0], minimumcost_motion[1][k][1], minimumcost_motion[1][k][2],
                                      minimumcost_motion[1][k][3], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])

    # Delete previous plot at each iteration
    plt.clf()

    # -------------- Magnitude plot H_pe ------------------
    plt.subplot(131)
    plt.title("Magnitude plots - $H_{pe}(jω)$ - Acceleration (C3+C6)")
    plt.loglog(w_FC, abs(Hpe_FC_C3), color='#7A5195', linestyle='-', marker='x', markersize='6', label='No motion')
    plt.loglog(w_FC, abs(Y_p_acceleration_Hpe_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
               label='Precision Model - No motion')
    plt.loglog(w_FC, abs(Hpe_FC_C6), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_acceleration_Hpe_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pe}(jω)|$")
    plt.legend(loc='lower right')
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_no_motion = np.angle(Y_p_acceleration_Hpe_no_motion)
    for l in range(len(angle_y_p_no_motion) - 1):
        if abs(angle_y_p_no_motion[l] - angle_y_p_no_motion[l + 1]) >= np.pi:
            angle_y_p_no_motion[l + 1] = angle_y_p_no_motion[l + 1] - 2 * np.pi

    angle_y_p_motion = np.angle(Y_p_acceleration_Hpe_motion)
    for m in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[m] - angle_y_p_motion[m + 1]) >= np.pi:
            angle_y_p_motion[m + 1] = angle_y_p_motion[m + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pe}(jω)$ - Acceleration (C3+C6)")
    plt.semilogx(w_FC, np.rad2deg(angle_C3_Hpe), color='#7A5195', linestyle='-', marker='x', markersize='6',
                 label='No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_no_motion), color='#003f5c', linestyle='-', marker='x', markersize='6',
                 label='Precision Model - No motion')
    plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpe), color='#EF5675', linestyle='-', marker='o', markersize='4',
                 label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model - Motion')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(max(h, k)), horizontalalignment='center', verticalalignment='center',
             fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0., 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0., 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.7, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.7, 0.775, "no motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(0.7, 0.7, guess_acceleration_Hpe_nomotion[0], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.6, guess_acceleration_Hpe_nomotion[1], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.5, guess_acceleration_Hpe_nomotion[2], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.4, guess_acceleration_Hpe_nomotion[3], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.3, guess_acceleration_Hpe_nomotion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.7, 0.2, guess_acceleration_Hpe_nomotion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(1, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(1, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10, fontweight='bold')
    plt.text(1, 0.775, "motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(1, 0.7, guess_velocity_Hpe_motion[0], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.6, guess_velocity_Hpe_motion[1], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.5, guess_velocity_Hpe_motion[2], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.4, guess_velocity_Hpe_motion[3], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.3, guess_velocity_Hpe_motion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(1, 0.2, guess_velocity_Hpe_motion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(0.2, 0.8, "No motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.2, 0.7, round(minimumcost_nomotion[1][h][0], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.6, round(minimumcost_nomotion[1][h][1], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.5, round(minimumcost_nomotion[1][h][2], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.4, round(minimumcost_nomotion[1][h][3], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.3, round(minimumcost_nomotion[1][h][4], 3), horizontalalignment='center',
             verticalalignment='center')
    plt.text(0.2, 0.2, round(minimumcost_nomotion[1][h][5], 3), horizontalalignment='center',
             verticalalignment='center')

    plt.text(0.45, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.45, 0.7, round(minimumcost_motion[1][k][0], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.6, round(minimumcost_motion[1][k][1], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.5, round(minimumcost_motion[1][k][2], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.4, round(minimumcost_motion[1][k][3], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.45, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
plt.show()


# --------------------------------- ACCELERATION H_pxd ----------------------------

# # ------------------ Precision Model for Acceleration H_pxd ------------------
# # Variables:
# K_p = 0.02  # Pilot gain
# T_L = 3.1  # Lead time constant
# T_I = 0.5  # Lag time constant
# t_e = 0.1  # Effective time delay
# w_nm = 15.0  # Neuromuscular frequency
# damping_ratio = 0.30  # Neuromuscular damping ratio
#
# # Model:
# Y_p_acceleration_Hpxd = Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio)
#
# # --------------- Magnitude plot H_pxd ------------------
# plt.subplot(121)
# plt.title("Magnitude plot - $H_{pxd}(jω)$ - Acceleration (C6)")
# plt.loglog(w_FC, abs(Hpxd_FC_C6), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.loglog(w_FC, abs(Y_p_acceleration_Hpxd), color='black', linestyle='-', marker='o', markersize='4',
#            label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel("$|H_{pxd}(jω)|$")
# plt.legend(loc='upper left')
# plt.grid(True, which="both")
#
# # ------------------ Angle plot H_pxd ----------------------
# # Loop to manually unwrap the phase array
# angle_C6_Hpxd = np.angle(Hpxd_FC_C6)
# for i in range(len(angle_C6_Hpxd) - 1):
#     if abs(angle_C6_Hpxd[i] - angle_C6_Hpxd[i + 1]) >= np.pi:
#         angle_C6_Hpxd[i + 1] = angle_C6_Hpxd[i + 1] - 2 * np.pi
#
# angle_y_p = np.angle(Y_p_acceleration_Hpxd)
# for i in range(len(angle_y_p) - 1):
#     if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#         angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
# plt.subplot(122)
# plt.title("Phase plot - $H_{pxd}(jω)$ - Acceleration (C6)")
# plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpxd), color='g', linestyle='-', marker='o', markersize='4', label='Motion')
# plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4',
#              label='Precision Model')
# plt.xlabel("ω [rad/s]")
# plt.ylabel(u"\u2220" + "$H_{pxd}(jω)$ [deg]")
# plt.grid(True, which="both")
# plt.legend(loc='lower left')
# plt.show()


# --------------------------- Cost function and optimisation H_pxd ----------------------


# def costfunction_motion(variables):
#     J = 0         # Define cost function J
#     W_abs = 1     # Weight absolute value
#     W_angle = 1   # Weight angle
#     Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
#                       variables[5])
#
#     # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
#     angle_y_p = np.angle(Y_precision)
#     for i in range(len(angle_y_p) - 1):
#         if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
#             angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi
#
#     # Sum each element (response and model at each frequency) to get the cost
#     for i in range(len(w_FC)):
#         # Function only takes an array of variables instead of individual variables
#         #J += W_abs * (abs(Hpxd_FC_C6[i]) - abs(Y_precision[i])) ** 2 + W_angle * (angle_C6_Hpxd[i] - angle_y_p[i]) ** 2
#         J += W_abs * abs((Hpxd_FC_C6[i] - Y_precision[i])**2)
#     return J
#
# # Initial guess MOTION:
# K_p_motion = 0.02            # Pilot gain
# T_L_motion = 3.1             # Lead time constant
# T_I_motion = 0.5             # Lag time constant
# t_e_motion = 0.1             # Effective time delay
# w_nm_motion = 15.0           # Neuromuscular frequency
# damping_ratio_motion = 0.30  # Neuromuscular damping ratio
# guess_acceleration_Hpxd_motion = [K_p_motion, T_L_motion, T_I_motion, t_e_motion, w_nm_motion, damping_ratio_motion]
#
#
# # Optimise the function, Y_p_position_Hpe is initial guess
# minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_acceleration_Hpxd_motion, retall=True)


# Loop to manually unwrap the phase array
angle_C6_Hpxd = np.angle(Hpxd_FC_C6)

for i in range(len(angle_C6_Hpxd) - 1):
    if abs(angle_C6_Hpxd[i] - angle_C6_Hpxd[i + 1]) >= np.pi:
        angle_C6_Hpxd[i + 1] = angle_C6_Hpxd[i + 1] - 2 * np.pi


# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
# for iteration in minimumcost_motion[1][::30]:
#     Y_p_acceleration_Hpxd_motion = Y_p(iteration[0], iteration[1], iteration[2], iteration[3], iteration[4], iteration[5])
for k in range(0, len(minimumcost_motion[1]), 30):
    Y_p_acceleration_Hpxd_motion = Y_p(minimumcost_motion[1][k][6], minimumcost_motion[1][k][7], minimumcost_motion[1][k][8],
                                       minimumcost_motion[1][k][9], minimumcost_motion[1][k][4], minimumcost_motion[1][k][5])

    # Delete previous plot at each iteration
    plt.clf()

    # ---------- Magnitude plot H_pxd -----------
    plt.subplot(131)
    plt.title("Magnitude plot - $H_{pxd}(jω)$ - Acceleration (C6)")
    plt.loglog(w_FC, abs(Hpxd_FC_C6), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_acceleration_Hpxd_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
               label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pxd}(jω)|$")
    plt.legend(loc='upper left')
    plt.grid(True, which="both")

    # ------- Angle plots ------
    # Unwrap angle
    angle_y_p_motion = np.angle(Y_p_acceleration_Hpxd_motion)
    for i in range(len(angle_y_p_motion) - 1):
        if abs(angle_y_p_motion[i] - angle_y_p_motion[i + 1]) >= np.pi:
            angle_y_p_motion[i + 1] = angle_y_p_motion[i + 1] - 2 * np.pi

    plt.subplot(132)
    plt.title("Phase plot - $H_{pxd}(jω)$ - Acceleration (C6)")
    plt.semilogx(w_FC, np.rad2deg(angle_C6_Hpxd), color='#EF5675', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p_motion), color='#FFA600', linestyle='-', marker='o', markersize='4',
                 label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pxd}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.subplot(133)
    plt.axis('off')

    plt.title("Precision model parameters")
    plt.text(0.5, 0.9, "Iteration #" + str(k), horizontalalignment='center', verticalalignment='center',
             fontsize=9, fontweight='bold', fontstyle='italic')

    plt.text(0.2, 0.7, r'$\mathbf{K_p}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.6, r'$\mathbf{T_L}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.5, r'$\mathbf{T_I}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.4, r'$\mathbf{\tau_e}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.3, r'$\mathbf{\omega_{nm}}$', horizontalalignment='center', verticalalignment='center')
    plt.text(0.2, 0.2, r'$\mathbf{\zeta_{nm}}$', horizontalalignment='center', verticalalignment='center')

    plt.text(0.8, 0.825, "Initial", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.8, 0.8, "guess", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')

    plt.text(0.8, 0.7, guess_acceleration_Hpe_motion[6], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.6, guess_acceleration_Hpe_motion[7], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.5, guess_acceleration_Hpe_motion[8], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.4, guess_acceleration_Hpe_motion[9], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.3, guess_acceleration_Hpe_motion[4], horizontalalignment='center', verticalalignment='center',
             fontsize=10)
    plt.text(0.8, 0.2, guess_acceleration_Hpe_motion[5], horizontalalignment='center', verticalalignment='center',
             fontsize=10)

    plt.text(0.5, 0.8, "Motion", horizontalalignment='center', verticalalignment='center', fontsize=10,
             fontweight='bold')
    plt.text(0.5, 0.7, round(minimumcost_motion[1][k][6], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.6, round(minimumcost_motion[1][k][7], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.5, round(minimumcost_motion[1][k][8], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.4, round(minimumcost_motion[1][k][9], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.3, round(minimumcost_motion[1][k][4], 3), horizontalalignment='center', verticalalignment='center')
    plt.text(0.5, 0.2, round(minimumcost_motion[1][k][5], 3), horizontalalignment='center', verticalalignment='center')

    plt.pause(0.001)

plt.text(0.5, 0.1, "Iteration finished", horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
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

