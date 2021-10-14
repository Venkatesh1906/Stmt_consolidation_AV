# -*- coding: utf-8 -*-
import pandas as pd
import os
import win32com.client
import glob


# Converting all the files into .xlsx
o = win32com.client.Dispatch("Excel.Application")
o.Visible = False
input_dir = r"Consolidation\Data\OneDrive_3_10-13-2021"
output_dir = r"Consolidation\Data\OneDrive_3_10-13-2021_xlsx"
files = glob.glob(input_dir + "/*.xls")
for filename in files:
    file = os.path.basename(filename)
    output = output_dir + '/' + file.replace('.xls','.xlsx')
    wb = o.Workbooks.Open(filename)
    wb.ActiveSheet.SaveAs(output,51)
    wb.Close(True)


# File Consolidation
dir_to_read = r'Consolidation\Data\OneDrive_4_10-13-2021_xlsx'
file_names = os.listdir(dir_to_read)

df_from_each_file = (pd.read_excel(os.path.join(dir_to_read,file),
                                   skiprows=3) for file in file_names)

full_txns_df   = pd.concat(df_from_each_file, ignore_index=True)
full_txns_df.dropna(axis=0, how='all', inplace=True)


# File Consolidation
dir_to_read = r'Consolidation\Data\OneDrive_3_10-13-2021_xlsx'
file_names = os.listdir(dir_to_read)

df_from_each_file = (pd.read_excel(os.path.join(dir_to_read,file),
                                   skiprows=3) for file in file_names)

full_pos_df   = pd.concat(df_from_each_file, ignore_index=True)
full_pos_df.dropna(axis=0, how='all', inplace=True)

# Saving to disk
dir_to_save = r'\Consolidation\Output'

full_txns_df.to_excel(os.path.join(dir_to_save, 'full_txns_df.xlsx'),
                      index=False)

full_pos_df.to_excel(os.path.join(dir_to_save, 'full_pos_df.xlsx'),
                     index=False)