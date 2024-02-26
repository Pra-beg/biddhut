import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
data = {
    "id":[1,2,3,4],
    "Name":["rakesh","hari","shyam","govinda"],
    "Age": [18,16,17,20]
}
df = pd.DataFrame(data, index = ['a','b','c','d'])
File_Path = r'C:\Users\acer\Desktop\bidutth\data.xlsx'
#it loads the excel file temporary in the memory
#represent entire workbook
Load_file = load_workbook(File_Path)
Work_Sheet_Car = Load_file['Car']
print(Work_Sheet_Car)
for rows in dataframe_to_rows(df,index= False):
    Work_Sheet_Car.append(rows)
Load_file.save(File_Path)
