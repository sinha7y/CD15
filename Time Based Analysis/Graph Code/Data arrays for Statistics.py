import scipy.io
import scipy.optimize
import numpy as np
from statsmodels.stats.weightstats import ttest_ind


# Arrays for statistics
Kp_array_NoMo_Hpe_Pos = []
Kp_array_Mo_Hpe_Pos = []
Kp_array_Mo_Hpxd_Pos = []
Kp_array_NoMo_Hpe_Vel = []
Kp_array_Mo_Hpe_Vel = []
Kp_array_Mo_Hpxd_Vel = []
Kp_array_NoMo_Hpe_Acc = []
Kp_array_Mo_Hpe_Acc = []
Kp_array_Mo_Hpxd_Acc = []

TL_array_NoMo_Hpe_Pos = []
TL_array_Mo_Hpe_Pos = []
TL_array_NoMo_Hpe_Vel = []
TL_array_Mo_Hpe_Vel = []
TL_array_NoMo_Hpe_Acc = []
TL_array_Mo_Hpe_Acc = []

TI_array_NoMo_Hpe_Pos = []
TI_array_Mo_Hpe_Pos = []
TI_array_NoMo_Hpe_Vel = []
TI_array_Mo_Hpe_Vel = []
TI_array_NoMo_Hpe_Acc = []
TI_array_Mo_Hpe_Acc = []

tau_array_NoMo_Hpe_Pos = []
tau_array_Mo_Hpe_Pos = []
tau_array_Mo_Hpxd_Pos = []
tau_array_NoMo_Hpe_Vel = []
tau_array_Mo_Hpe_Vel = []
tau_array_Mo_Hpxd_Vel = []
tau_array_NoMo_Hpe_Acc = []
tau_array_Mo_Hpe_Acc = []
tau_array_Mo_Hpxd_Acc = []

frequency_array_NoMo_Pos = []
frequency_array_Mo_Pos = []
frequency_array_NoMo_Vel = []
frequency_array_Mo_Vel = []
frequency_array_NoMo_Acc = []
frequency_array_Mo_Acc = []

damping_array_NoMo_Pos = []
damping_array_Mo_Pos = []
damping_array_NoMo_Vel = []
damping_array_Mo_Vel = []
damping_array_NoMo_Acc = []
damping_array_Mo_Acc = []


for index in range(1, 7):

    # filename = "ae2223I_measurement_data_subj1.mat"
    filename = "ae2223I_measurement_data_subj" + str(index) + ".mat"

    # Read Matlab file
    datasubj1 = scipy.io.loadmat(filename)

    # Note:
    #     | P   V   A
    # _________________
    #  NM | C1  C2  C3
    #  M  | C4  C5  C6

    # ---------------------------------- Variables ---------------------------------
    w_FC = datasubj1['w_FC']  # Frequency
    t = datasubj1['t'][0]  # Time
    data_C1 = datasubj1['data_C1']  # Data Condition 1
    data_C2 = datasubj1['data_C2']
    data_C3 = datasubj1['data_C3']
    data_C4 = datasubj1['data_C4']
    data_C5 = datasubj1['data_C5']
    data_C6 = datasubj1['data_C6']

    Hpe_FC_C1 = data_C1['Hpe_FC'][0][0]
    Hpxd_FC_C1 = data_C1['Hpxd_FC'][0][0]

    Hpe_FC_C2 = data_C2['Hpe_FC'][0][0]
    Hpxd_FC_C2 = data_C2['Hpxd_FC'][0][0]

    Hpe_FC_C3 = data_C3['Hpe_FC'][0][0]
    Hpxd_FC_C3 = data_C3['Hpxd_FC'][0][0]

    Hpe_FC_C4 = data_C4['Hpe_FC'][0][0]
    Hpxd_FC_C4 = data_C4['Hpxd_FC'][0][0]

    Hpe_FC_C5 = data_C5['Hpe_FC'][0][0]
    Hpxd_FC_C5 = data_C5['Hpxd_FC'][0][0]

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

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W * abs((Hpe_FC_C1[i] - Y_precision[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    angle_C4_Hpe = np.angle(Hpe_FC_C4)

    for i in range(len(angle_C4_Hpe) - 1):
        if abs(angle_C4_Hpe[i] - angle_C4_Hpe[i + 1]) >= np.pi:
            angle_C4_Hpe[i + 1] = angle_C4_Hpe[i + 1] - 2 * np.pi


    def costfunction_motion(variables):
        J = 0  # Define cost function J
        W_abs = 1  # Weight

        # Precision model function for H_pe
        Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                              variables[5])
        # Precision model function for H_pxd
        Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[7], variables[9], variables[4],
                               variables[5])

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W_abs * abs((Hpe_FC_C4[i] - Y_precision_Hpe[i]) ** 2) + abs(
                (Hpxd_FC_C4[i] - Y_precision_Hpxd[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    # Initial guess NO MOTION:
    K_p_nomotion = 3  # Pilot gain
    T_L_nomotion = 0.1  # Lead time constant
    T_I_nomotion = 1.58  # Lag time constant
    t_e_nomotion = 0.10  # Effective time delay
    w_nm_nomotion = 8.0  # Neuromuscular frequency
    damping_ratio_nomotion = 0.10  # Neuromuscular damping ratio
    guess_position_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                                   damping_ratio_nomotion]

    # Initial guess MOTION:
    K_p_motion_Hpe = 2  # Pilot gain for H_pe
    T_L_motion_Hpe = 0.2  # Lead time constant for H_pe
    T_I_motion_Hpe = 1.85  # Lag time constant for H_pe
    t_e_motion_Hpe = 0.20  # Effective time delay for H_pe
    w_nm_motion = 7.0  # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
    damping_ratio_motion = 0.20  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
    K_p_motion_Hpxd = 2  # Pilot gain for H_pxd
    T_L_motion_Hpxd = 0.2  # Lead time constant for H_pxd
    T_I_motion_Hpxd = 1.85  # Lag time constant for H_pxd
    t_e_motion_Hpxd = 0.20  # Effective time delay for H_pxd
    guess_position_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion,
                                 damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd,
                                 t_e_motion_Hpxd]

    # NOTE: Guess is called H_pe, but contains also H_pxd

    # Optimise the function, Y_p_position_Hpe is initial guess
    minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_position_Hpe_nomotion, retall=True)
    minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_position_Hpe_motion, retall=True)

    # ---------------- Save variables to CSV for boxplot --------------
    KpnomotionPos = minimumcost_nomotion[0][0]
    KpmotionHpePos = minimumcost_motion[0][0]
    KpmotionHpxdPos = minimumcost_motion[0][6]

    TLnomotionPos = minimumcost_nomotion[0][1]
    TLmotionHpePos = minimumcost_motion[0][1]
    TLmotionHpxdPos = minimumcost_motion[0][7]

    TInomotionPos = minimumcost_nomotion[0][2]
    TImotionHpePos = minimumcost_motion[0][2]
    TImotionHpxdPos = minimumcost_motion[0][7]

    TaunomotionPos = minimumcost_nomotion[0][3]
    TaumotionHpePos = minimumcost_motion[0][3]
    TaumotionHpxdPos = minimumcost_motion[0][9]

    NMFreqnomotionPos = minimumcost_nomotion[0][4]
    NMFreqmotionHpePos = minimumcost_motion[0][4]
    NMFreqmotionHpxdPos = minimumcost_motion[0][4]

    NMDampingnomotionPos = minimumcost_nomotion[0][5]
    NMDampingmotionHpePos = minimumcost_motion[0][5]
    NMDampingmotionHpxdPos = minimumcost_motion[0][5]

    """
    -----------------------------------------------------------------------------------
    ----------------------------------- VELOCITY --------------------------------------
    -----------------------------------------------------------------------------------
    """

    # --------------------------- Cost function and optimisation H_pe ----------------------

    # Loop to manually unwrap the phase array
    angle_C2_Hpe = np.angle(Hpe_FC_C2)

    for i in range(len(angle_C2_Hpe) - 1):
        if abs(angle_C2_Hpe[i] - angle_C2_Hpe[i + 1]) >= np.pi:
            angle_C2_Hpe[i + 1] = angle_C2_Hpe[i + 1] - 2 * np.pi


    def costfunction_nomotion(variables):
        J = 0  # Define cost function J
        W_abs = 1  # Weight

        Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                          variables[5])  # Precision model function

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W_abs * abs((Hpe_FC_C2[i] - Y_precision[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    angle_C5_Hpe = np.angle(Hpe_FC_C5)

    for i in range(len(angle_C5_Hpe) - 1):
        if abs(angle_C5_Hpe[i] - angle_C5_Hpe[i + 1]) >= np.pi:
            angle_C5_Hpe[i + 1] = angle_C5_Hpe[i + 1] - 2 * np.pi


    def costfunction_motion(variables):
        J = 0  # Define cost function J
        W_abs = 1  # Weight

        # Precision model function for H_pe
        Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                              variables[5])
        # Precision model function for H_pxd
        Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[7], variables[9], variables[4],
                               variables[5])

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W_abs * abs((Hpe_FC_C5[i] - Y_precision_Hpe[i]) ** 2) + abs(
                (Hpxd_FC_C5[i] - Y_precision_Hpxd[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    # Initial guess NO MOTION:
    K_p_nomotion = 0.07  # Pilot gain
    T_L_nomotion = 2.1  # Lead time constant
    T_I_nomotion = 0.08  # Lag time constant
    t_e_nomotion = 0.3  # Effective time delay
    w_nm_nomotion = 15.0  # Neuromuscular frequency
    damping_ratio_nomotion = 0.30  # Neuromuscular damping ratio
    guess_velocity_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                                   damping_ratio_nomotion]

    # Initial guess MOTION:
    K_p_motion_Hpe = 0.09  # Pilot gain for H_pe
    T_L_motion_Hpe = 3.1  # Lead time constant for H_pe
    T_I_motion_Hpe = 0.10  # Lag time constant for H_pe
    t_e_motion_Hpe = 0.20  # Effective time delay for H_pe
    w_nm_motion = 14.0  # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
    damping_ratio_motion = 0.40  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
    K_p_motion_Hpxd = 0.07  # Pilot gain for H_pxd
    T_L_motion_Hpxd = 2.1  # Lead time constant for H_pxd
    T_I_motion_Hpxd = 0.08  # Lag time constant for H_pxd
    t_e_motion_Hpxd = 0.3  # Effective time delay for H_pxd
    guess_velocity_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion,
                                 damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd,
                                 t_e_motion_Hpxd]

    # NOTE: Guess is called H_pe, but contains also H_pxd

    # Optimise the function, Y_p_position_Hpe is initial guess
    minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_velocity_Hpe_nomotion, retall=True)
    minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_velocity_Hpe_motion, retall=True)

    # ---------------- Save variables to CSV for boxplot --------------
    KpnomotionVel = minimumcost_nomotion[0][0]
    KpmotionHpeVel = minimumcost_motion[0][0]
    KpmotionHpxdVel = minimumcost_motion[0][6]

    TLnomotionVel = minimumcost_nomotion[0][1]
    TLmotionHpeVel = minimumcost_motion[0][1]
    TLmotionHpxdVel = minimumcost_motion[0][7]

    TInomotionVel = minimumcost_nomotion[0][2]
    TImotionHpeVel = minimumcost_motion[0][2]
    TImotionHpxdVel = minimumcost_motion[0][7]

    TaunomotionVel = minimumcost_nomotion[0][3]
    TaumotionHpeVel = minimumcost_motion[0][3]
    TaumotionHpxdVel = minimumcost_motion[0][9]

    NMFreqnomotionVel = minimumcost_nomotion[0][4]
    NMFreqmotionHpeVel = minimumcost_motion[0][4]
    NMFreqmotionHpxdVel = minimumcost_motion[0][4]

    NMDampingnomotionVel = minimumcost_nomotion[0][5]
    NMDampingmotionHpeVel = minimumcost_motion[0][5]
    NMDampingmotionHpxdVel = minimumcost_motion[0][5]

    """
    -----------------------------------------------------------------------------------
    --------------------------------- ACCELERATION ------------------------------------
    -----------------------------------------------------------------------------------
    """

    # --------------------------- Cost function and optimisation H_pe ----------------------

    # Loop to manually unwrap the phase array
    angle_C3_Hpe = np.angle(Hpe_FC_C3)

    for i in range(len(angle_C3_Hpe) - 1):
        if abs(angle_C3_Hpe[i] - angle_C3_Hpe[i + 1]) >= np.pi:
            angle_C3_Hpe[i + 1] = angle_C3_Hpe[i + 1] - 2 * np.pi


    def costfunction_nomotion(variables):
        J = 0  # Define cost function J
        W_abs = 1  # Weight
        Y_precision = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                          variables[5])  # Precision model function

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W_abs * abs((Hpe_FC_C3[i] - Y_precision[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    angle_C6_Hpe = np.angle(Hpe_FC_C6)

    for i in range(len(angle_C6_Hpe) - 1):
        if abs(angle_C6_Hpe[i] - angle_C6_Hpe[i + 1]) >= np.pi:
            angle_C6_Hpe[i + 1] = angle_C6_Hpe[i + 1] - 2 * np.pi


    def costfunction_motion(variables):
        J = 0  # Define cost function J
        W_abs = 1  # Weight
        # Precision model function for H_pe
        Y_precision_Hpe = Y_p(variables[0], variables[1], variables[2], variables[3], variables[4],
                              variables[5])
        # Precision model function for H_pxd
        Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[7], variables[9], variables[4],
                               variables[5])

        # Sum each element (response and model at each frequency) to get the cost
        for i in range(len(w_FC)):
            # Function only takes an array of variables instead of individual variables
            J += W_abs * abs((Hpe_FC_C6[i] - Y_precision_Hpe[i]) ** 2) + abs(
                (Hpxd_FC_C6[i] - Y_precision_Hpxd[i]) ** 2)

        for parameter in variables:
            if parameter < 0:
                J += 1000000

        return J


    # Initial guess NO MOTION:
    K_p_nomotion = 0.07  # Pilot gain
    T_L_nomotion = 2.1  # Lead time constant
    T_I_nomotion = 0.08  # Lag time constant
    t_e_nomotion = 0.3  # Effective time delay
    w_nm_nomotion = 13.0  # Neuromuscular frequency
    damping_ratio_nomotion = 0.30  # Neuromuscular damping ratio
    guess_acceleration_Hpe_nomotion = [K_p_nomotion, T_L_nomotion, T_I_nomotion, t_e_nomotion, w_nm_nomotion,
                                       damping_ratio_nomotion]

    # Initial guess MOTION:
    K_p_motion_Hpe = 0.08  # Pilot gain for H_pe
    T_L_motion_Hpe = 2.3  # Lead time constant for H_pe
    T_I_motion_Hpe = 0.09  # Lag time constant for H_pe
    t_e_motion_Hpe = 0.20  # Effective time delay for H_pe
    w_nm_motion = 14.0  # Neuromuscular frequency (SAME FOR H_pe and H_pxd)
    damping_ratio_motion = 0.35  # Neuromuscular damping ratio (SAME FOR H_pe and H_pxd)
    K_p_motion_Hpxd = 0.02  # Pilot gain for H_pxd
    T_L_motion_Hpxd = 3.1  # Lead time constant for H_pxd
    T_I_motion_Hpxd = 0.50  # Lag time constant for H_pxd
    t_e_motion_Hpxd = 0.1  # Effective time delay for H_pxd
    guess_acceleration_Hpe_motion = [K_p_motion_Hpe, T_L_motion_Hpe, T_I_motion_Hpe, t_e_motion_Hpe, w_nm_motion,
                                     damping_ratio_motion, K_p_motion_Hpxd, T_L_motion_Hpxd, T_I_motion_Hpxd,
                                     t_e_motion_Hpxd]

    # NOTE: Guess is called H_pe, but contains also H_pxd

    # Optimisation function
    minimumcost_nomotion = scipy.optimize.fmin(costfunction_nomotion, guess_acceleration_Hpe_nomotion, retall=True)
    minimumcost_motion = scipy.optimize.fmin(costfunction_motion, guess_acceleration_Hpe_motion, retall=True)

    # ---------------- Save variables to CSV for boxplot --------------
    KpnomotionAcc = minimumcost_nomotion[0][0]
    KpmotionHpeAcc = minimumcost_motion[0][0]
    KpmotionHpxdAcc = minimumcost_motion[0][6]

    TLnomotionAcc = minimumcost_nomotion[0][1]
    TLmotionHpeAcc = minimumcost_motion[0][1]
    TLmotionHpxdAcc = minimumcost_motion[0][7]

    TInomotionAcc = minimumcost_nomotion[0][2]
    TImotionHpeAcc = minimumcost_motion[0][2]
    TImotionHpxdAcc = minimumcost_motion[0][7]

    TaunomotionAcc = minimumcost_nomotion[0][3]
    TaumotionHpeAcc = minimumcost_motion[0][3]
    TaumotionHpxdAcc = minimumcost_motion[0][9]

    NMFreqnomotionAcc = minimumcost_nomotion[0][4]
    NMFreqmotionHpeAcc = minimumcost_motion[0][4]
    NMFreqmotionHpxdAcc = minimumcost_motion[0][4]

    NMDampingnomotionAcc = minimumcost_nomotion[0][5]
    NMDampingmotionHpeAcc = minimumcost_motion[0][5]
    NMDampingmotionHpxdAcc = minimumcost_motion[0][5]

    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------- Write parameter values to CSV file -----------------------------------
    # ----------------------------------------------------------------------------------------------------------

    # Pilot gain
    Kp_array_NoMo_Hpe_Pos.append(KpnomotionPos)
    Kp_array_Mo_Hpe_Pos.append(KpmotionHpePos)
    Kp_array_Mo_Hpxd_Pos.append(KpmotionHpxdPos)

    Kp_array_NoMo_Hpe_Vel.append(KpnomotionVel)
    Kp_array_Mo_Hpe_Vel.append(KpmotionHpeVel)
    Kp_array_Mo_Hpxd_Vel.append(KpmotionHpxdVel)

    Kp_array_NoMo_Hpe_Acc.append(KpnomotionAcc)
    Kp_array_Mo_Hpe_Acc.append(KpmotionHpeAcc)
    Kp_array_Mo_Hpxd_Acc.append(KpmotionHpxdAcc)

    # Lead time constant
    TL_array_NoMo_Hpe_Pos.append(TLnomotionPos)
    TL_array_Mo_Hpe_Pos.append(TLmotionHpePos)

    TL_array_NoMo_Hpe_Vel.append(TLnomotionVel)
    TL_array_Mo_Hpe_Vel.append(TLmotionHpeVel)

    TL_array_NoMo_Hpe_Acc.append(TLnomotionAcc)
    TL_array_Mo_Hpe_Acc.append(TLmotionHpeAcc)

    # Lag time constant
    TI_array_NoMo_Hpe_Pos.append(TInomotionPos)
    TI_array_Mo_Hpe_Pos.append(TImotionHpePos)

    TI_array_NoMo_Hpe_Vel.append(TInomotionVel)
    TI_array_Mo_Hpe_Vel.append(TImotionHpeVel)

    TI_array_NoMo_Hpe_Acc.append(TInomotionAcc)
    TI_array_Mo_Hpe_Acc.append(TImotionHpeAcc)

    # Time delay
    tau_array_NoMo_Hpe_Pos.append(TaunomotionPos)
    tau_array_Mo_Hpe_Pos.append(TaumotionHpePos)
    tau_array_Mo_Hpxd_Pos.append(TaumotionHpxdPos)

    tau_array_NoMo_Hpe_Vel.append(TaunomotionVel)
    tau_array_Mo_Hpe_Vel.append(TaumotionHpeVel)
    tau_array_Mo_Hpxd_Vel.append(TaumotionHpxdVel)

    tau_array_NoMo_Hpe_Acc.append(TaunomotionAcc)
    tau_array_Mo_Hpe_Acc.append(TaumotionHpeAcc)
    tau_array_Mo_Hpxd_Acc.append(TaumotionHpxdAcc)

    # NM Frequency
    frequency_array_NoMo_Pos.append(NMFreqnomotionPos)
    frequency_array_Mo_Pos.append(NMFreqmotionHpePos)

    frequency_array_NoMo_Vel.append(NMFreqnomotionVel)
    frequency_array_Mo_Vel.append(NMFreqmotionHpeVel)

    frequency_array_NoMo_Acc.append(NMFreqnomotionAcc)
    frequency_array_Mo_Acc.append(NMFreqmotionHpeAcc)

    # NM Damping Coefficient
    damping_array_NoMo_Pos.append(NMDampingnomotionPos)
    damping_array_Mo_Pos.append(NMDampingmotionHpePos)

    damping_array_NoMo_Vel.append(NMDampingnomotionVel)
    damping_array_Mo_Vel.append(NMDampingmotionHpeVel)

    damping_array_NoMo_Acc.append(NMDampingnomotionAcc)
    damping_array_Mo_Acc.append(NMDampingmotionHpeAcc)

    
print('******* Kp  ******')
ttest_KpHpe_pos=ttest_ind(Kp_array_NoMo_Hpe_Pos, Kp_array_Mo_Hpe_Pos)
ttest_KpHpe_vel=ttest_ind(Kp_array_NoMo_Hpe_Vel, Kp_array_Mo_Hpe_Vel)
ttest_KpHpe_acc=ttest_ind(Kp_array_NoMo_Hpe_Acc, Kp_array_Mo_Hpe_Acc)
#ttestHpe_pos=ttest_ind(Kp_array_NoMo_Hpe_Pos, Kp_array_Mo_Hpe_Pos)

t_value_KpHpe_pos=ttestHpe_pos[0]
p_value_KpHpe_pos=ttestHpe_pos[1]
deg_freedom_KpHpe_pos=ttestHpe_pos[2]

t_value_KpHpe_vel=ttest_KpHpe_vel[0]
p_value_KpHpe_vel=ttest_KpHpe_vel[1]
deg_freedom_KpHpe_vel=ttest_KpHpe_vel[2]

t_value_KpHpe_acc=ttest_KpHpe_acc[0]
p_value_KpHpe_acc=ttest_KpHpe_acc[1]
deg_freedom_KpHpe_acc=ttest_KpHpe_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, Kp_Hpe***')
print('t_value=',round(t_value_KpHpe_pos,3), ',',  round(t_value_KpHpe_vel,3), ',',  round(t_value_KpHpe_acc,3))
print('p_value=',round(p_value_KpHpe_pos,3), ',',  round(p_value_KpHpe_vel,3), ',',  round(p_value_KpHpe_acc,3))
print('degrees of freedom:',deg_freedom_KpHpe_pos)
print('')


print('******* TL  ******')

ttest_TLHpe_pos=ttest_ind(TL_array_NoMo_Hpe_Pos, TL_array_Mo_Hpe_Pos)
ttest_TLHpe_vel=ttest_ind(TL_array_NoMo_Hpe_Vel, TL_array_Mo_Hpe_Vel)
ttest_TLHpe_acc=ttest_ind(TL_array_NoMo_Hpe_Acc, TL_array_Mo_Hpe_Acc)

t_value_TLHpe_pos=ttest_TLHpe_pos[0]
p_value_TLHpe_pos=ttest_TLHpe_pos[1]
deg_freedom_TLHpe_pos=ttest_TLHpe_pos[2]

t_value_TLHpe_vel=ttest_TLHpe_vel[0]
p_value_TLHpe_vel=ttest_TLHpe_vel[1]
deg_freedom_TLHpe_vel=ttest_TLHpe_vel[2]

t_value_TLHpe_acc=ttest_TLHpe_acc[0]
p_value_TLHpe_acc=ttest_TLHpe_acc[1]
deg_freedom_TLHpe_acc=ttest_TLHpe_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, TLHpe***')
print('t_value=',round(t_value_TLHpe_pos,3), ',',  round(t_value_TLHpe_vel,3), ',',  round(t_value_TLHpe_acc,3))
print('p_value=',round(p_value_TLHpe_pos,3), ',',  round(p_value_TLHpe_vel,3), ',',  round(p_value_TLHpe_acc,3))
print('degrees of freedom:',deg_freedom_TLHpe_pos)
print('')

print('******* TI  ******')

ttest_TIHpe_pos=ttest_ind(TI_array_NoMo_Hpe_Pos, TI_array_Mo_Hpe_Pos)
ttest_TIHpe_vel=ttest_ind(TI_array_NoMo_Hpe_Vel, TI_array_Mo_Hpe_Vel)
ttest_TIHpe_acc=ttest_ind(TI_array_NoMo_Hpe_Acc, TI_array_Mo_Hpe_Acc)

t_value_TIHpe_pos=ttest_TIHpe_pos[0]
p_value_TIHpe_pos=ttest_TIHpe_pos[1]
deg_freedom_TIHpe_pos=ttest_TIHpe_pos[2]

t_value_TIHpe_vel=ttest_TIHpe_vel[0]
p_value_TIHpe_vel=ttest_TIHpe_vel[1]
deg_freedom_TIHpe_vel=ttest_TIHpe_vel[2]

t_value_TIHpe_acc=ttest_TIHpe_acc[0]
p_value_TIHpe_acc=ttest_TIHpe_acc[1]
deg_freedom_TIHpe_acc=ttest_TIHpe_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, TIHpe***')
print('t_value=',round(t_value_TIHpe_pos,3), ',',  round(t_value_TIHpe_vel,3), ',',  round(t_value_TIHpe_acc,3))
print('p_value=',round(p_value_TIHpe_pos,3), ',',  round(p_value_TIHpe_vel,3), ',',  round(p_value_TIHpe_acc,3))
print('degrees of freedom:',deg_freedom_TIHpe_pos)
print('')

print('******* Tau  ******')

ttest_tauHpe_pos=ttest_ind(tau_array_NoMo_Hpe_Pos, tau_array_Mo_Hpe_Pos)
ttest_tauHpe_vel=ttest_ind(tau_array_NoMo_Hpe_Vel, tau_array_Mo_Hpe_Vel)
ttest_tauHpe_acc=ttest_ind(tau_array_NoMo_Hpe_Acc, tau_array_Mo_Hpe_Acc)

t_value_tauHpe_pos=ttest_tauHpe_pos[0]
p_value_tauHpe_pos=ttest_tauHpe_pos[1]
deg_freedom_tauHpe_pos=ttest_tauHpe_pos[2]

t_value_tauHpe_vel=ttest_tauHpe_vel[0]
p_value_tauHpe_vel=ttest_tauHpe_vel[1]
deg_freedom_tauHpe_vel=ttest_tauHpe_vel[2]

t_value_tauHpe_acc=ttest_tauHpe_acc[0]
p_value_tauHpe_acc=ttest_tauHpe_acc[1]
deg_freedom_tauHpe_acc=ttest_tauHpe_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, tauHpe***')
print('t_value=',round(t_value_tauHpe_pos,3), ',',  round(t_value_tauHpe_vel,3), ',',  round(t_value_tauHpe_acc,3))
print('p_value=',round(p_value_tauHpe_pos,3), ',',  round(p_value_tauHpe_vel,3), ',',  round(p_value_tauHpe_acc,3))
print('degrees of freedom:',deg_freedom_tauHpe_pos)
print('')


print('******* Frequency  ******')

ttest_frequency_pos=ttest_ind(frequency_array_NoMo_Pos, frequency_array_Mo_Pos)
ttest_frequency_vel=ttest_ind(frequency_array_NoMo_Vel, frequency_array_Mo_Vel)
ttest_frequency_acc=ttest_ind(frequency_array_NoMo_Acc, frequency_array_Mo_Acc)

t_value_frequency_pos=ttest_frequency_pos[0]
p_value_frequency_pos=ttest_frequency_pos[1]
deg_freedom_frequency_pos=ttest_frequency_pos[2]

t_value_frequency_vel=ttest_frequency_vel[0]
p_value_frequency_vel=ttest_frequency_vel[1]
deg_freedom_frequency_vel=ttest_frequency_vel[2]

t_value_frequency_acc=ttest_frequency_acc[0]
p_value_frequency_acc=ttest_frequency_acc[1]
deg_freedom_frequency_acc=ttest_frequency_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, frequency***')
print('t_value=',round(t_value_frequency_pos,3), ',',  round(t_value_frequency_vel,3), ',',  round(t_value_frequency_acc,3))
print('p_value=',round(p_value_frequency_pos,3), ',',  round(p_value_frequency_vel,3), ',',  round(p_value_frequency_acc,3))
print('degrees of freedom:',deg_freedom_frequency_pos)
print('')

print('******* Damping  ******')

ttest_damping_pos=ttest_ind(damping_array_NoMo_Pos, damping_array_Mo_Pos)
ttest_damping_vel=ttest_ind(damping_array_NoMo_Vel, damping_array_Mo_Vel)
ttest_damping_acc=ttest_ind(damping_array_NoMo_Acc, damping_array_Mo_Acc)

t_value_damping_pos=ttest_damping_pos[0]
p_value_damping_pos=ttest_damping_pos[1]
deg_freedom_damping_pos=ttest_damping_pos[2]

t_value_damping_vel=ttest_damping_vel[0]
p_value_damping_vel=ttest_damping_vel[1]
deg_freedom_damping_vel=ttest_damping_vel[2]

t_value_damping_acc=ttest_damping_acc[0]
p_value_damping_acc=ttest_damping_acc[1]
deg_freedom_damping_acc=ttest_damping_acc[2]

print('***1 Position, 2 velocity, 3 acceleration, frequency***')
print('t_value=',round(t_value_damping_pos,3), ',',  round(t_value_damping_vel,3), ',',  round(t_value_damping_acc,3))
print('p_value=',round(p_value_damping_pos,3), ',',  round(p_value_damping_vel,3), ',',  round(p_value_damping_acc,3))
print('degrees of freedom:',deg_freedom_damping_pos)
    
print("Ready")
