"""
Created on Thu Jan  7 20:16:56 2021

@author: Robert
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Robert Alward/Desktop/Spreadsheet2/formedium-296418-ca1ec050ec23.json',scope)

gc = gspread.authorize(credentials)

#### 0. Loading Data
spreadsheetName = "Copy of Hiring Process Tracking Sheet: Working Copy"
sheetName1 = "Data"  # <--- please set the sheet name here.
sheetName2 = "BE Data"  
sheetName3 = "History" 
sheetName4 = "Comparison" 
wks = gc.open(spreadsheetName)
sheet_1 = wks.worksheet(sheetName1)
sheet_2 = wks.worksheet(sheetName2)
sheet_3 = wks.worksheet(sheetName3)
sheet_4 = wks.worksheet(sheetName4)

# 0.1 Sheet 1 to Pandas
sheet_1_data = sheet_1.get_all_values()
headers_1 = sheet_1_data.pop(0)

panda_sheet_1 = pd.DataFrame(sheet_1_data, columns=headers_1)

# 0.3 Sheet 3 to Pandas
sheet_3_data = sheet_3.get_all_values()
headers_3 = sheet_3_data.pop(0)

panda_sheet_3 = pd.DataFrame(sheet_3_data, columns = headers_3)

# 0.4 Sheet 4 to Pandas
sheet_4_data = sheet_4.get_all_values()
headers_4 = sheet_4_data.pop(0)

panda_sheet_4 = pd.DataFrame(sheet_4_data, columns = headers_4)


#### 1. Creating Automatically Updating Historical Data Tab

start_row = 1

for i in range(panda_sheet_1.Data.count()): 
      
     print("for loop:", panda_sheet_1.iloc[i, 5])       
   
     if panda_sheet_1.iloc[i, 5] != panda_sheet_4.iloc[i, 5]:
          sheet1_temp_row = panda_sheet_1.iloc[i,:]
        
          panda_sheet_3.loc[i] = sheet1_temp_row 
          
sheet_3.update([panda_sheet_3.columns.values.tolist()] + panda_sheet_3.values.tolist())

panda_sheet_4 = panda_sheet_1

sheet_4.update([panda_sheet_4.columns.values.tolist()] + panda_sheet_4.values.tolist())




