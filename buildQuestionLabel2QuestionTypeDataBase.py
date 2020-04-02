#mcandrew

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    qDB = pd.DataFrame()
    
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}

    # SURVEY1 (2020-02-17)
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    q['questionLabel'].append('QF-1-0')
    q['questionLabel'].append('QF-1-1_1')
    q['questionLabel'].append('QF-2-0')
    q['questionLabel'].append('QF-2_1')
    q['questionLabel'].append('QF-2_2_1')
    q['questionLabel'].append('QF-2_2_2')
    q['questionLabel'].append('QF-2_2_3')
    q['questionLabel'].append('QF-3-0')

    #targets
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append(np.nan)

    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append(np.nan)

    #forecastdate
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append('2020-02-23')
    q['forecastdate'].append('2020-02-23')
    q['forecastdate'].append('2020-02-23')
    q['forecastdate'].append(np.nan)
    
    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-02-17'
    qDB = qDB.append(q)

    # SURVEY2 (2020-02-24)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}
    
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    q['questionLabel'].append('QF1')
    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF3')
    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF5_1')
    q['questionLabel'].append('QF5_2')
    q['questionLabel'].append('QF5_3')
    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF6_2')
    q['questionLabel'].append('QF6_3')
    q['questionLabel'].append('QF7')

    #target
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('countries')
    q['target'].append('countries')
    q['target'].append('countries')
    q['target'].append(np.nan)

    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append(np.nan)

    #forecastdate
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append('2020-03-1')
    q['forecastdate'].append('2020-03-1')
    q['forecastdate'].append('2020-03-1')
    q['forecastdate'].append('2020-03-8')
    q['forecastdate'].append('2020-03-8')
    q['forecastdate'].append('2020-03-8')
    q['forecastdate'].append(np.nan)

    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-02-24'
    qDB = qDB.append(q)

    # SURVEY3 (2020-03-02)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}
    
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')

    q['questionLabel'].append('QF1_1')
    q['questionLabel'].append('QF1_2')
    q['questionLabel'].append('QF1_3')

    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF2_2')
    q['questionLabel'].append('QF2_3')

    q['questionLabel'].append('QF3_1')
    q['questionLabel'].append('QF3_2')
    q['questionLabel'].append('QF3_3')

    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF4_2')
    q['questionLabel'].append('QF4_3')

    q['questionLabel'].append('QF5_1')
    q['questionLabel'].append('QF5_2')
    q['questionLabel'].append('QF5_3')

    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF6_2')
    q['questionLabel'].append('QF6_3')

    q['questionLabel'].append('QF7')

    #target
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')

    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('states')

    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('percent')

    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('percent')

    q['target'].append('countries')
    q['target'].append('countries')
    q['target'].append('countries')
    
    q['target'].append(np.nan)
    
    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    q['surveillanceSystem'].append('WHO')
    
    q['surveillanceSystem'].append(np.nan)
   
    #forecastdate
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    
    q['forecastdate'].append('2020-03-02')
    q['forecastdate'].append('2020-03-02')
    q['forecastdate'].append('2020-03-02')
    
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    
    q['forecastdate'].append('2020-03-08')
    q['forecastdate'].append('2020-03-08')
    q['forecastdate'].append('2020-03-08')

    q['forecastdate'].append(np.nan)
    

    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-03-02'
    qDB = qDB.append(q)

    # SURVEY4 (2020-03-09)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}
    
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    
    q['questionLabel'].append('QF1_1')
    q['questionLabel'].append('QF1_2')
    q['questionLabel'].append('QF1_3')
    
    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF2_2')
    q['questionLabel'].append('QF2_3')
    
    q['questionLabel'].append('QF3')
    
    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF4_2')
    q['questionLabel'].append('QF4_3')
    
    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF6_2')
    q['questionLabel'].append('QF6_3')
    
    q['questionLabel'].append('QF7')
    q['questionLabel'].append('QF8')
    q['questionLabel'].append('QF9')

    #truth
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    
    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('states')
    
    q['target'].append(np.nan)
    
    q['target'].append('community')
    q['target'].append('community')
    q['target'].append('community')
    
    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('percent')
    
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)

    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append(np.nan)
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)

    #forecastdate
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    q['forecastdate'].append('2020-03-16')
    
    q['forecastdate'].append(np.nan)
    
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    q['forecastdate'].append('2020-03-09')
    
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)


    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-03-09'
    qDB = qDB.append(q)

    # SURVEY5 (2020-03-16)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}

    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    q['questionLabel'].append('QF1_1')
    q['questionLabel'].append('QF1_2')
    q['questionLabel'].append('QF1_3')
    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF2_2')
    q['questionLabel'].append('QF2_3')
    q['questionLabel'].append('QF3_1')
    q['questionLabel'].append('QF3_2')
    q['questionLabel'].append('QF3_3')
    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF4_2')
    q['questionLabel'].append('QF4_3')
    q['questionLabel'].append('QF5_1')
    q['questionLabel'].append('QF5_2')
    q['questionLabel'].append('QF5_3')
    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF7')
    q['questionLabel'].append('QF8')

    #truth
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)

    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)

    #forecastdate
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-22')
    q['forecastdate'].append('2020-03-15')
    q['forecastdate'].append('2020-03-15')
    q['forecastdate'].append('2020-03-15')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)

    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-03-16'
    qDB = qDB.append(q)
 
    
    # SURVEY6 (2020-03-23)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}
    
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    q['questionLabel'].append('QF1_1')
    q['questionLabel'].append('QF1_2')
    q['questionLabel'].append('QF1_3')
    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF2_2')
    q['questionLabel'].append('QF2_3')
    q['questionLabel'].append('QF3_1')
    q['questionLabel'].append('QF3_2')
    q['questionLabel'].append('QF3_3')
    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF4_2')
    q['questionLabel'].append('QF4_3')
    q['questionLabel'].append('QF5_1')
    q['questionLabel'].append('QF5_2')
    q['questionLabel'].append('QF5_3')
    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF6_4')
    q['questionLabel'].append('QF6_5')
    q['questionLabel'].append('QF6_6')
    q['questionLabel'].append('QF6_7')
    q['questionLabel'].append('QF6_8')
    q['questionLabel'].append('QF7')
    q['questionLabel'].append('QF8')

    #target
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('states')
    q['target'].append('total')
    q['target'].append('total')
    q['target'].append('total')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)


    #surveillanceSystem
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)

    #surveillanceSystem
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-04-05')
    q['forecastdate'].append('2020-04-05')
    q['forecastdate'].append('2020-04-05')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-29')
    q['forecastdate'].append('2020-03-23')
    q['forecastdate'].append('2020-03-23')
    q['forecastdate'].append('2020-03-23')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append('2020-12-31')
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
    q['forecastdate'].append(np.nan)
 
    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-03-23'
    qDB = qDB.append(q)


    # SURVEY7 (2020-03-30)
    q = {'questionLabel':[],'target':[], 'surveillanceSystem':[], 'forecastdate':[]}
    
    q['questionLabel'].append('Q0-1')
    q['questionLabel'].append('QR-1-0')
    q['questionLabel'].append('QR-2-0')
    q['questionLabel'].append('QF1_1')
    q['questionLabel'].append('QF1_2')
    q['questionLabel'].append('QF1_3')
    q['questionLabel'].append('QF2_1')
    q['questionLabel'].append('QF2_2')
    q['questionLabel'].append('QF2_3')
    q['questionLabel'].append('QF3_1')
    q['questionLabel'].append('QF3_2')
    q['questionLabel'].append('QF3_3')
    q['questionLabel'].append('QF4_1')
    q['questionLabel'].append('QF4_2')
    q['questionLabel'].append('QF4_3')
    q['questionLabel'].append('QF5_1')
    q['questionLabel'].append('QF5_4')
    q['questionLabel'].append('QF5_5')
    q['questionLabel'].append('QF5_6')
    q['questionLabel'].append('QF5_7')
    q['questionLabel'].append('QF5_8')
    q['questionLabel'].append('QF6_1')
    q['questionLabel'].append('QF6_2')
    q['questionLabel'].append('QF6_3')
    q['questionLabel'].append('QF7_1')

    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('cases')
    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('percent')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append('death')
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append(np.nan)
    q['target'].append('peak')
    q['target'].append('peak')
    q['target'].append('peak')
    q['target'].append(np.nan)

    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append('COVIDtracker')
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append(np.nan)
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append('CDC')
    q['surveillanceSystem'].append(np.nan)


    q = pd.DataFrame(q)
    q['surveyIssued'] = '2020-03-30'
    qDB = qDB.append(q)

    truthDB.to_csv('./database/questionLabel2QuestionType.csv')
