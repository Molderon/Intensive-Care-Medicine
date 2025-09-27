

import pandas as pd
import numpy as np

class MechanicalPower:
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset.copy()



    @staticmethod
    def LinearModel_MP(row: pd.Series) -> float:
        try:
            RR = row['SET_RR_IPPV']
            TV = row['TV']
            PEEP = row['PEEP_MBAR']
            Delta_P_insp = row['SET_INSP_PRES']
            t_slope = row['t_slope']
            R = row['Resistance']

            if R == 0:
                return np.nan

            return 0.098 * RR * (TV * (PEEP + Delta_P_insp) - 0.15 * (Delta_P_insp**2) * (t_slope / R))
        except KeyError as e:
            print(f"Missing column for MP_LM calculation: {e}. Returning NaN.")
            return np.nan
        except Exception as e:
            print(f"Error calculating MP_LM: {e}. Returning NaN.")
            return np.nan



    @staticmethod
    def BecherComp_MP(row: pd.Series) -> float:
        try:
            RR = row['SET_RR_IPPV']
            TV = row['TV']
            PEEP = row['PEEP_MBAR']
            Delta_P_insp = row['SET_INSP_PRES']
            C = row['COMPLIANCE']
            t_slope = row['t_slope']
            R = row['Resistance']

            if t_slope == 0 or (R * C) == 0:
                return np.nan

            term1 = TV * (PEEP + Delta_P_insp)
            rc_tslope = (R * C) / t_slope
            exp_term_denom = R * C
            if exp_term_denom == 0:
                return np.nan

            exp_term = np.exp(-t_slope / exp_term_denom)
            bracket_term = 0.5 - rc_tslope + (rc_tslope**2) * (1 - exp_term)
            term2 = (Delta_P_insp**2) * C * bracket_term
            return 0.098 * RR * (term1 - term2)
    
        except KeyError as e:
            print(f"Missing column for MP_CB calculation: {e}. Returning NaN.")
            return np.nan
        except Exception as e:
            print(f"Error calculating MP_CB: {e}. Returning NaN.")
            return np.nan



    @staticmethod
    def VanderMeijen_MP(row: pd.Series) -> float:
        try:
            RR = row['SET_RR_IPPV']
            TV = row['TV']
            PEEP = row['PEEP_MBAR']
            Delta_P_insp = row['SET_INSP_PRES']
            t_insp = row['SET_INSP_TM']
            R = row['Resistance']
            C = row['COMPLIANCE']

            exp_term_denom = R * C
            if exp_term_denom == 0:
                return np.nan

            exp_term = np.exp(-t_insp / exp_term_denom)
            bracket_term = PEEP + Delta_P_insp * (1 - exp_term)
            return 0.098 * RR * TV * bracket_term
        except KeyError as e:
            print(f"Missing column for MP_vdM calculation: {e}. Returning NaN.")
            return np.nan
        except Exception as e:
            print(f"Error calculating MP_vdM: {e}. Returning NaN.")
            return np.nan
    


    @staticmethod
    def SimpleBecher_MP(row: pd.Series) -> float:
        try:
            RR = row['SET_RR_IPPV']
            TV = row['TV']
            PEEP = row['PEEP_MBAR']
            Delta_P_insp = row['SET_INSP_PRES']
            return 0.098 * RR * (TV * (PEEP + Delta_P_insp))
        except KeyError as e:
            print(f"Missing column for MP_SB calculation: {e}. Returning NaN.")
            return np.nan
        except Exception as e:
            print(f"Error calculating MP_SB: {e}. Returning NaN.")
            return np.nan
    


    def calculate_all(self) -> pd.DataFrame:
        df = self.dataset.copy()
        
        # Apply each method and store results in new columns
        df['MP_LM'] = df.apply(self.LinearModel_MP, axis=1)
        df['MP_CB'] = df.apply(self.BecherComp_MP, axis=1)
        df['MP_vdM'] = df.apply(self.VanderMeijen_MP, axis=1)
        df['MP_SB'] = df.apply(self.SimpleBecher_MP, axis=1)
        
        return df