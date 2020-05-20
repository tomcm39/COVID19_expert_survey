#mcandrew

import sys
import numpy as np
import pandas as pd

class truth(object):
    def __init__(self):
        self.truth = {'questionLabel':[],'questionroot':[],'truth':[]}

    def addQuestionLabels(self,listOfLabels):
        for ql in listOfLabels:
            self.truth['questionLabel'].append(ql)
            self.truth['questionroot'].append(ql.split('_')[0])

    def addTruths(self,truths):
        for t in truths:
            self.truth['truth'].append(t)
            
    def export2DB(self,surveyIssuedDate):
        self.truthDB = pd.DataFrame(self.truth)
        self.truthDB['surveyIssued'] = surveyIssuedDate
        return self.truthDB

if __name__ == "__main__":

    # SURVEY1 (2020-02-17)
    survey1 = truth()
    survey1.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF-1-0','QF-1-1_1','QF-2-0','QF-2-0_1','QF-2-2_1','QF-2-2_2','QF-2-2_3','QF-3-0'])
    survey1.addTruths([np.nan,np.nan,np.nan,1,1,1,1,35,35,35,np.nan])
    survey1DB = survey1.export2DB('2020-02-17')
    
    # SURVEY2 (2020-02-24)
    survey2 = truth()
    survey2.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1','QF2_1','QF3','QF4_1','QF5_1','QF5_2','QF5_3','QF6_1','QF6_2','QF6_3','QF7'])
    survey2.addTruths([np.nan,np.nan,np.nan,1,1,1,1,62,62,62,7,7,7,np.nan])
    survey2DB = survey2.export2DB('2020-02-24')

    # SURVEY3 (2020-03-02)
    survey3 = truth()
    survey3.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF4_1','QF4_2','QF4_3','QF5_1','QF5_2','QF5_3','QF6_1','QF6_2','QF6_3','QF7'])
    survey3.addTruths([np.nan,np.nan,np.nan,423,423,423,3487,3487,3487,35,35,35,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,17,17,17,np.nan])
    survey3DB = survey3.export2DB('2020-03-02')
    
    # SURVEY4 (2020-03-09)
    survey4 = truth()
    survey4.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3','QF4_1','QF4_2','QF4_3','QF6_1','QF6_2','QF6_3','QF7','QF8','QF9'])
    survey4.addTruths([np.nan,np.nan,np.nan,3487,3487,3487,49,49,49,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey4DB = survey4.export2DB('2020-03-09')

    # SURVEY5 (2020-03-16)
    survey5 = truth()
    survey5.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF4_1','QF4_2','QF4_3','QF5_1','QF5_2','QF5_3','QF6_1','QF7','QF8'])
    survey5.addTruths([np.nan,np.nan,np.nan,33404,33404,33404,139061,139061,139061,32,32,32,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey5DB = survey5.export2DB('2020-03-16')
    
    # SURVEY6 (2020-03-23)
    survey6 = truth()
    survey6.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF4_1','QF4_2','QF4_3','QF5_1','QF5_2','QF5_3','QF6_1','QF6_4','QF6_5','QF6_6','QF6_7','QF6_8','QF7','QF8'])
    survey6.addTruths([np.nan,np.nan,np.nan,139061,139061,139061,332308,332308,332308,49,49,49,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey6DB = survey6.export2DB('2020-03-23')
   
    # SURVEY7 (2020-03-30)
    survey7 = truth()
    survey7.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF4_1','QF4_2','QF4_3','QF5_1','QF5_4','QF5_5','QF5_6','QF5_7','QF5_8','QF6_1','QF6_2','QF6_3','QF7_1','QF8','QF9'])
    survey7.addTruths([np.nan,np.nan,np.nan,332308,332308,332308,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey7DB = survey7.export2DB('2020-03-30')
    
    # SURVEY8 (2020-04-06)
    survey8 = truth()
    survey8.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF2_1','QF2_2','QF2_3','QF3_1','QF3_4','QF3_5','QF3_6','QF3_7','QF3_8','QF3_10','Q4_1','Q4_2','Q4_3','Q4_4','Q4_5','QF5_1','QF5_2','QF5_3','QF6','QF7'])
    survey8.addTruths([np.nan,np.nan,np.nan,576774,576774,576774,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,2,2,2,2,2,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey8DB = survey8.export2DB('2020-04-06')

    # SURVEY9 (2020-04-13)
    # true number of cases was 751,646 and corresponds to bin the 3rd bin which is labeled "3"
    
    survey9 = truth()
    survey9.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF1_5','QF1_6','QF1_7','QF1_8','QF1_9','QF2_1','QF2_2','QF2_3','QF2_4','QF2_5','QF3_1','QF3_2','QF3_3','QF3_4','QF3_5','QF3_6','Q4_1','Q4_2','Q4_3','QF5_1','QF5_2','QF5_3','QF6_1','QF7','QF8'])
    survey9.addTruths([np.nan,np.nan,np.nan,3,3,3,3,3,3,3,3,5,5,5,5,5,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey9DB = survey9.export2DB('2020-04-13')

    # SURVEY10 (2020-04-20)
    # true number of cases was 960,343 and corresponds to the fourth bin which is labeled "5"
    survey10 = truth()
    survey10.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF1_5','QF1_6','QF1_7','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','Q4_1','Q4_2','Q4_3','QF5_1','QF5_2','QF5_3','QF6_1','QF6_2'
,'QF6_3','QF6_4','QF6_5','QF7','QF8'])
    survey10.addTruths([np.nan,np.nan,np.nan,5,5,5,5,5,5,73291,73291,73291,3349,3349,3349,2267,2267,2267,np.nan,np.nan,np.nan,1,1,1,1,1,np.nan,np.nan])
    survey10DB = survey10.export2DB('2020-04-20')

    # SURVEY11 (2020-04-27)
    # 1,152,006 reported
    survey11 = truth()
    survey11.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF1_4','QF1_5','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF3_4','QF3_5','QF4_1','QF4_2','QF4_3','QF5_1','QF5_2','QF5_3'])
    survey11.addTruths([np.nan,np.nan,np.nan,4,4,4,4,4,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey11DB = survey11.export2DB('2020-04-27')
    
    # SURVEY12 (2020-05-04)
    survey12 = truth()
    survey12.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF1_4','QF1_5','QF1_6','QF1_7','QF2_1','QF2_2','QF2_3','QF2_4','QF2_5','QF2_6','QF2_7','QF3_1','QF3_2','QF3_3','QF3_4','QF3_5','QF4_1','QF4_2','QF4_3','QF4_4','QF4_5','QF5_1','QF5_2','QF5_3'])
    survey12.addTruths([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey12DB = survey12.export2DB('2020-05-04')

    #SURVEY13 - 2020-05-12
    survey13 = truth()
    survey13.addQuestionLabels(['Q0-1','QR-1-0','QR-2-0','QF1_1','QF1_2','QF1_3','QF1_4','QF1_5','QF1_6','QF1_7','QF2_1','QF2_2','QF2_3','QF3_1','QF3_2','QF3_3','QF4_1','QF4_2','QF4_3','QF5_1'])
    survey13.addTruths([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    survey13DB = survey13.export2DB('2020-05-11')

    entiredb = pd.DataFrame()
    for db in [survey1DB,survey2DB,survey3DB,survey4DB,survey5DB
              ,survey6DB,survey7DB,survey8DB,survey9DB,survey10DB
              ,survey11DB,survey12DB,survey13DB]:
        entiredb = entiredb.append(db)
    entiredb.to_csv('./database/truthDatabase.csv',index=False)
