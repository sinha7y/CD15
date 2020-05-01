import scipy.io
import scipy.optimize
import numpy as np
import csv

# Clear files everytime the program runs, to avoid overwritting the files
Kpfile = open("Kpvalues.csv", "w")
Kpfile.truncate()
Kpfile.close()

TLfile = open("TLvalues.csv", "w")
TLfile.truncate()
TLfile.close()

TIfile = open("TIvalues.csv", "w")
TIfile.truncate()
TIfile.close()

Taufile = open("Tauvalues.csv", "w")
Taufile.truncate()
Taufile.close()

Freqfile = open("NMFreqvalues.csv", "w")
Freqfile.truncate()
Freqfile.close()

Dampingfile = open("NMDampingvalues.csv", "w")
Dampingfile.truncate()
Dampingfile.close()

with open('Kpvalues.csv', 'w') as Kpdata, open('TLvalues.csv', 'w') as TLdata, open('TIvalues.csv', 'w') as TIdata, \
        open('Tauvalues.csv', 'w') as Taudata, open('NMFreqvalues.csv', 'w') as NMFreqdata, \
        open('NMDampingvalues.csv', 'w') as NMDampingdata:

    Kpwriter = csv.writer(Kpdata, delimiter=',')
    Kpwriter.writerow([r'$K_p$'] + ['Motion'] + ['Control Mode'])

    TLwriter = csv.writer(TLdata, delimiter=',')
    TLwriter.writerow([r'$T_L$'] + ['Motion'] + ['Control Mode'])

    TIwriter = csv.writer(TIdata, delimiter=',')
    TIwriter.writerow([r'$T_I$'] + ['Motion'] + ['Control Mode'])

    Tauwriter = csv.writer(Taudata, delimiter=',')
    Tauwriter.writerow([r'$\tau$'] + ['Motion'] + ['Control Mode'])

    NMFreqwriter = csv.writer(NMFreqdata, delimiter=',')
    NMFreqwriter.writerow([r'$\omega_{nm}$'] + ['Motion'] + ['Control Mode'])

    Dampingwriter = csv.writer(NMDampingdata, delimiter=',')
    Dampingwriter.writerow([r'$damping_{nm}$'] + ['Motion'] + ['Control Mode'])

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
            Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                                   variables[5])

            # Sum each element (response and model at each frequency) to get the cost
            for i in range(len(w_FC)):
                # Function only takes an array of variables instead of individual variables
                J += W_abs * abs((Hpe_FC_C4[i] - Y_precision_Hpe[i]) ** 2) + abs(
                    (Hpxd_FC_C4[i] - Y_precision_Hpxd[i]) ** 2)
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
        TImotionHpxdPos = minimumcost_motion[0][8]

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
            Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                                   variables[5])

            # Sum each element (response and model at each frequency) to get the cost
            for i in range(len(w_FC)):
                # Function only takes an array of variables instead of individual variables
                J += W_abs * abs((Hpe_FC_C5[i] - Y_precision_Hpe[i]) ** 2) + abs(
                    (Hpxd_FC_C5[i] - Y_precision_Hpxd[i]) ** 2)
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
        TImotionHpxdVel = minimumcost_motion[0][8]

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
            Y_precision_Hpxd = Y_p(variables[6], variables[7], variables[8], variables[9], variables[4],
                                   variables[5])

            # Sum each element (response and model at each frequency) to get the cost
            for i in range(len(w_FC)):
                # Function only takes an array of variables instead of individual variables
                J += W_abs * abs((Hpe_FC_C6[i] - Y_precision_Hpe[i]) ** 2) + abs(
                    (Hpxd_FC_C6[i] - Y_precision_Hpxd[i]) ** 2)

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
        TImotionHpxdAcc = minimumcost_motion[0][8]

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
        Kpwriter.writerow([str(KpnomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        Kpwriter.writerow([str(KpmotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        Kpwriter.writerow([str(KpmotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        Kpwriter.writerow([str(KpnomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        Kpwriter.writerow([str(KpmotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        Kpwriter.writerow([str(KpmotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        Kpwriter.writerow([str(KpnomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        Kpwriter.writerow([str(KpmotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        Kpwriter.writerow([str(KpmotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

        # Lead time constant
        TLwriter.writerow([str(TLnomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        TLwriter.writerow([str(TLmotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        TLwriter.writerow([str(TLmotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        TLwriter.writerow([str(TLnomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        TLwriter.writerow([str(TLmotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        TLwriter.writerow([str(TLmotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        TLwriter.writerow([str(TLnomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        TLwriter.writerow([str(TLmotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        TLwriter.writerow([str(TLmotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

        # Lag time constant
        TIwriter.writerow([str(TInomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        TIwriter.writerow([str(TImotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        TIwriter.writerow([str(TImotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        TIwriter.writerow([str(TInomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        TIwriter.writerow([str(TImotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        TIwriter.writerow([str(TImotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        TIwriter.writerow([str(TInomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        TIwriter.writerow([str(TImotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        TIwriter.writerow([str(TImotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

        # Time delay
        Tauwriter.writerow([str(TaunomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        Tauwriter.writerow([str(TaumotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        Tauwriter.writerow([str(TaumotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        Tauwriter.writerow([str(TaunomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        Tauwriter.writerow([str(TaumotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        Tauwriter.writerow([str(TaumotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        Tauwriter.writerow([str(TaunomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        Tauwriter.writerow([str(TaumotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        Tauwriter.writerow([str(TaumotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

        #Neuromuscular frequency
        NMFreqwriter.writerow([str(NMFreqnomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        NMFreqwriter.writerow([str(NMFreqmotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        NMFreqwriter.writerow([str(NMFreqmotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        NMFreqwriter.writerow([str(NMFreqnomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        NMFreqwriter.writerow([str(NMFreqmotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        NMFreqwriter.writerow([str(NMFreqmotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        NMFreqwriter.writerow([str(NMFreqnomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        NMFreqwriter.writerow([str(NMFreqmotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        NMFreqwriter.writerow([str(NMFreqmotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

        #Neuromuscular Dampingg

        Dampingwriter.writerow([str(NMDampingnomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        Dampingwriter.writerow([str(NMDampingmotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        Dampingwriter.writerow([str(NMDampingmotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])

        Dampingwriter.writerow([str(NMDampingnomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        Dampingwriter.writerow([str(NMDampingmotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        Dampingwriter.writerow([str(NMDampingmotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])

        Dampingwriter.writerow([str(NMDampingnomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        Dampingwriter.writerow([str(NMDampingmotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        Dampingwriter.writerow([str(NMDampingmotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])
        
        # # Lag time constant
        # TIwriter.writerow([str(TInomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        # TIwriter.writerow([str(TImotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        # TIwriter.writerow([str(TImotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])
        #
        # TIwriter.writerow([str(TInomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        # TIwriter.writerow([str(TImotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        # TIwriter.writerow([str(TImotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])
        #
        # TIwriter.writerow([str(TInomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        # TIwriter.writerow([str(TImotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        # TIwriter.writerow([str(TImotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])
        #
        # # Lag time constant
        # TIwriter.writerow([str(TInomotionPos)] + ['No - ' + r'$H_{pe}$'] + ['Pos'])
        # TIwriter.writerow([str(TImotionHpePos)] + ['Yes - ' + r'$H_{pe}$'] + ['Pos'])
        # TIwriter.writerow([str(TImotionHpxdPos)] + ['Yes - ' + r'$H_{pxd}$'] + ['Pos'])
        #
        # TIwriter.writerow([str(TInomotionVel)] + ['No - ' + r'$H_{pe}$'] + ['Vel'])
        # TIwriter.writerow([str(TImotionHpeVel)] + ['Yes - ' + r'$H_{pe}$'] + ['Vel'])
        # TIwriter.writerow([str(TImotionHpxdVel)] + ['Yes - ' + r'$H_{pxd}$'] + ['Vel'])
        #
        # TIwriter.writerow([str(TInomotionAcc)] + ['No - ' + r'$H_{pe}$'] + ['Acc'])
        # TIwriter.writerow([str(TImotionHpeAcc)] + ['Yes - ' + r'$H_{pe}$'] + ['Acc'])
        # TIwriter.writerow([str(TImotionHpxdAcc)] + ['Yes - ' + r'$H_{pxd}$'] + ['Acc'])

Kpdata.close()
TLdata.close()
TIdata.close()
Taudata.close()
NMFreqdata.close()
NMDampingdata.close()

print("Ready")
