import numpy as np

def pce_ascvd(is_black, is_man, age, total_cholesterol, hdl, htn_treatment, blood_pressure, smoking, diabetes):
    '''
    is_black: [0 for white, 1 for black]
    is_man: [0 for woman, 1 for man]
    age: age in years
    total_cholesterol: total cholesterol 
    hdl: hdl cholesterol
    htn_treatment: [0 for untreated, 1 for treated]
    blood_pressure: blood pressure
    smoking: [0 for nonsmoker, 1 for smoker]
    diabetes: [0 for non-diabetes, 1 for diabetes]
    '''
    risk = -1
    risk_raw = -1
    if is_black == 0 and is_man == 0: # white woman
        if htn_treatment == 0: # untreated
            risk_raw = ((-29.799 * np.log(age)) + (4.884 * np.log(age)**2) + (13.540 * np.log(total_cholesterol)) + (-3.114 * np.log(age) * np.log(total_cholesterol))
                        + (-13.578 * np.log(hdl)) + (3.149 * np.log(age) * np.log(hdl)) + (1.957 * np.log(blood_pressure)) + (0 * np.log(age) * np.log(blood_pressure))
                        + (7.574 * smoking) + (-1.665 * np.log(age) * smoking) + (0.661 * diabetes))
            
        elif htn_treatment == 1: # treated
            risk_raw = ((-29.799 * np.log(age)) + (4.884 * np.log(age)**2) + (13.540 * np.log(total_cholesterol)) + (-3.114 * np.log(age) * np.log(total_cholesterol))
                    + (-13.578 * np.log(hdl)) + (3.149 * np.log(age) * np.log(hdl)) + (2.019 * np.log(blood_pressure)) + (0 * np.log(age) * np.log(blood_pressure))
                    + (7.574 * smoking) + (-1.665 * np.log(age) * smoking) + (0.661 * diabetes))

        risk = 1 - np.power(0.9665, np.exp(risk_raw + 29.18))

    if is_black == 1 and is_man == 0: # black woman
        if htn_treatment == 0: # untreated
            risk_raw = ((17.114 * np.log(age)) + (0 * np.log(age)**2) + (0.940 * np.log(total_cholesterol)) + (0 * np.log(age) * np.log(total_cholesterol))
                        + (-18.920 * np.log(hdl)) + (4.475 * np.log(age) * np.log(hdl)) + (27.820 * np.log(blood_pressure)) + (-6.087 * np.log(age) * np.log(blood_pressure))
                        + (0.691 * smoking) + (0 * np.log(age) * smoking) + (0.874 * diabetes))

        elif htn_treatment == 1: # treated
            risk_raw = ((17.114 * np.log(age)) + (0 * np.log(age)**2) + (0.940 * np.log(total_cholesterol)) + (0 * np.log(age) * np.log(total_cholesterol))
                    + (-18.920 * np.log(hdl)) + (4.475 * np.log(age) * np.log(hdl)) + (29.291 * np.log(blood_pressure)) + (-6.432 * np.log(age) * np.log(blood_pressure))
                    + (0.691 * smoking) + (0 * np.log(age) * smoking) + (0.874 * diabetes))
            
        risk = 1 - np.power(0.9533, np.exp(risk_raw - 86.61))
            
    print(risk)
    return risk


pce_ascvd(1, 0, 55, 213, 50, 0, 120, 0, 0)
