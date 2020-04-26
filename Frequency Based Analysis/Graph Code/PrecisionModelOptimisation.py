import scipy.io
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

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
Hpe_FC_C1  = data_C1['Hpe_FC'][0][0]
Hpxd_FC_C1 = data_C1['Hpxd_FC'][0][0]


Hpe_FC_C2  = data_C2['Hpe_FC'][0][0]
Hpxd_FC_C2 = data_C2['Hpxd_FC'][0][0]


Hpe_FC_C3  = data_C3['Hpe_FC'][0][0]
Hpxd_FC_C3 = data_C3['Hpxd_FC'][0][0]


Hpe_FC_C4  = data_C4['Hpe_FC'][0][0]
Hpxd_FC_C4 = data_C4['Hpxd_FC'][0][0]


Hpe_FC_C5  = data_C5['Hpe_FC'][0][0]
Hpxd_FC_C5 = data_C5['Hpxd_FC'][0][0]


Hpe_FC_C6  = data_C6['Hpe_FC'][0][0]
Hpxd_FC_C6 = data_C6['Hpxd_FC'][0][0]


# ---------------------------- Precision Model function --------------------------------
j = complex(0, 1)       # Define j

# Precision model function
def Y_p(K_p, T_L, T_I, t_e, w_nm, damping_ratio):
    return K_p * (T_L*w_FC*j + 1)/(T_I*w_FC*j + 1) * np.exp(-w_FC*j*t_e) * (1 / ((w_FC*j/w_nm)*(w_FC*j/w_nm) + (2*damping_ratio*w_FC*j / w_nm) + 1))



# ----------------------------------------- VELOCITY H_pe ------------------------------------------

# --------------------------- Cost function and optimisation H_pe ----------------------

# Loop to manually unwrap the phase array
angle_C2_Hpe = np.angle(Hpe_FC_C2)

for i in range(len(angle_C2_Hpe)-1):
    if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i+1]) >= np.pi:
        angle_C2_Hpe[i+1] = angle_C2_Hpe[i+1] - 2*np.pi

def costfunction(variables):
    J = 0  # Define cost function J
    W = 1  # Weight
    Y_precison = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4], variables[5]) # Precision model function

    # Unwrap angle of precision model (has to be done inside function, since Y_precision changes each iteration and affects cost function)
    angle_y_p = np.angle(Y_precison)
    for i in range(len(angle_y_p) - 1):
        if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
            angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # Sum each element (response and model at each frequency) to get the cost
    for i in range(len(w_FC)):
        # Function only takes an array of variables instead of individual variables
        J += W * (abs(Hpe_FC_C2[i]) - abs(Y_precison[i]))**2 + W * (angle_C2_Hpe[i] - angle_y_p[i])**2

    return J

# Initial guess
K_p = 0.07              # Pilot gain
T_L = 2.1               # Lead time constant
T_I = 0.08              # Lag time constant
t_e = 0.3               # Effective time delay
w_nm = 15.0             # Neuromuscular frequency
damping_ratio = 0.30    # Neuromuscular damping ratio
guess_velocity_Hpe = [K_p, T_L, T_I, t_e, w_nm, damping_ratio]

# Optimise the function, Y_p_velocity_Hpe is initial guess
minimumcost = scipy.optimize.fmin(costfunction, guess_velocity_Hpe, full_output=True, retall=True)
# print(minimumcost[0])
# print("0:", minimumcost[0])
# print("1:", minimumcost[1])
# print("2:", minimumcost[2])
# print("3:", minimumcost[3])
# print("4:", minimumcost[4])
# print("5:", minimumcost[5])
#
# print("Len:", len(minimumcost))

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



# Loop through the cost function iterations to plot the progress of the fitting (plot once every 30 iterations)
for iteration in minimumcost[5][::20]:
    Y_p_velocity_Hpe = Y_p(iteration[0], iteration[1], iteration[2], iteration[3], iteration[4], iteration[5])

    # Delete previous plot at each iteration
    plt.clf()

    # Unwrap angle
    angle_y_p = np.angle(Y_p_velocity_Hpe)
    for i in range(len(angle_y_p) - 1):
        if abs(angle_y_p[i] - angle_y_p[i + 1]) >= np.pi:
            angle_y_p[i + 1] = angle_y_p[i + 1] - 2 * np.pi

    # ------------ Magnitude plot H_pe -------------
    plt.subplot(121)
    plt.title("Magnitude plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
    plt.loglog(w_FC, abs(Hpe_FC_C2), color='#86D7FF', linestyle='-', marker='o', markersize='4', label='No motion')
    # plt.loglog(w_FC, abs(Hpe_FC_C5), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.loglog(w_FC, abs(Y_p_velocity_Hpe), color='black', linestyle='-', marker='o', markersize='4',
               label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel("$|H_{pe}(jω)|$")
    plt.legend(loc='upper left')
    plt.grid(True, which="both")

    # ---------- Angle plot H_pe ------------------
    plt.subplot(122)
    plt.title("Phase plot - $H_{pe}(jω)$ - Velocity (C2+C5)")
    plt.semilogx(w_FC, np.rad2deg(angle_C2_Hpe), color='#86D7FF', linestyle='-', marker='o', markersize='4',
                 label='No motion')
    # plt.semilogx(w_FC, np.rad2deg(angle_C5_Hpe), color='b', linestyle='-', marker='o', markersize='4', label='Motion')
    plt.semilogx(w_FC, np.rad2deg(angle_y_p), color='black', linestyle='-', marker='o', markersize='4',
                 label='Precision Model')
    plt.xlabel("ω [rad/s]")
    plt.ylabel(u"\u2220" + "$H_{pe}(jω)$ [deg]")
    plt.grid(True, which="both")
    plt.legend(loc='lower left')

    plt.pause(0.001)

#plt.subplot(121)
#plt.text(0.1, 10, "Finished")
plt.show()
