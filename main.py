import pandas as pd
import numpy as np
def contain(ev):
    if type(ev) != str:
        return False
    ev = ev.lower()
    if 'electric' in ev:
        for keywords in ['car','bus','cycle','motorbike']:
            if keywords in ev:
                return True
    return False

#dataimport from excel
filenames = ['shrawan.xlsx','FTS_upto_Bhadra2080_81.xlsx','FTS_UptoAsoj_2080_81.xlsx','FTS_Uptokartik_2080_81.xlsx','FTS_UptoMangsir_2080_81.xlsx','FTS.xlsx','FTS_Upto-Magh_2080_81-1 (1).xlsx'] 
months = ['shrawan','bhadra','ashwin','kartik','mangsir','poush','magh','falgun','chaitra','baishak','jestha']
dfs= []
for i,filename in enumerate(filenames):
    df = pd.read_excel(filename,sheet_name="5_Imports_By_Commodity",header=2)
    df =df[df["Description"].apply(contain)]
    quantities = df['Quantity']
    df['Month'] =  months[i]
    dfs.append(df)
merge_df = pd.concat(dfs)
