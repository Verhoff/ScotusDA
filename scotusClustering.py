import pandas as pd
import numpy as np
from matplotlib import pyplot
data = pd.read_csv("C:\\Users\\johnv\\Desktop\\Projects\\SCOTUS\\SCDB_2020_01_justiceCentered_Vote.csv\\SCDB_2020_01_justiceCentered_Vote.csv", encoding = 'ISO-8859-1')
columns = data.columns.values

justicesFull = data[['caseId','justice','justiceName','vote','opinion','direction','majority']]
#justices = justices['justiceName'].unique()

justicesName = justicesFull["justiceName"].unique()
#print(justicesName)

justiceList = justicesName.tolist()
#print(justiceList);

justicesCases = []
for name in justiceList:
    print(name)
    df = justicesFull.loc[justicesFull['justiceName'] == name]
    test = df.loc[(df['vote'] == 1 && df['majority'] == 1) || (df['vote'] == 2 && df['majority'] == 2)]
    print(test)
    #df2 = df.loc[df.vote == df.majority]
    #print(df2.head())
    #print(df)
    df = df['caseId'].unique()
    #print(df)
    justicesCases.append(df)
    casesIn = df.size
    #casesInMajority = df2.size
    #print(casesInMajority)
    #print(casesIn)
    #print(casesInMajority/casesIn)

#print(np.shape(justicesCases))
#print(justicesCases.shape)

#cases = data["caseId"].unique()
#print(cases)
