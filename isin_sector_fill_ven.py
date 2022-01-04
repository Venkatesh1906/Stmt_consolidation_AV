# Important Libs
import os
import pandas as pd
import numpy as np 
from tqdm import tqdm


# Data folder
files_folder = r'C:\Users\Desktop\Analytics_Projects\POS_Consolidation\Codes\Sid_request_23rddec'

# Save file to 
output_file_path = r'C:\Users\Desktop\Analytics_Projects\POS_Consolidation\Codes\Sid_request_23rddec'

# Reading all the files
bos_filename = 'BOS 1 Year Data.xlsx'
all_bank_data_filename = 'BOS,DBS,DB,LGT,JPM Bank data (1).csv'
db_filename = 'DB 1 year bank data.xlsx'
dbs_filename = 'DBS Updated1 year.xlsx'
jpmorgan_filename = 'JP Morgan_appended_File.xlsx'
lgt_filename = 'LGT 1 year.xlsx'
mapping_filename = 'mapping sheet wrt to banks and power bi.xlsx'

# Save the file with name
output_filename = 'all_bank_data_with_isin_sec.csv'


# Reading all the files
print("Reading BOS Data")
bos_df = pd.read_excel(os.path.join(files_folder, bos_filename))
print("Reading All Bank Data")
all_bank_df = pd.read_csv(os.path.join(files_folder, all_bank_data_filename))
print("Reading All DB Data")
db_df = pd.read_excel(os.path.join(files_folder, db_filename))
print("Reading DBS Data")
dbs_df = pd.read_excel(os.path.join(files_folder, dbs_filename))
print("Reading JP Morgan Data")
jpmorgan_df = pd.read_excel(os.path.join(files_folder, jpmorgan_filename))
print("Reading LGT Data")
lgt_df = pd.read_excel(os.path.join(files_folder, lgt_filename))
print("Reading Mapping File Data")
mapping_df = pd.read_excel(os.path.join(files_folder, mapping_filename), \
    sheet_name='ISIN')


# Creating a column ISIN And Sector
all_bank_df['ISIN'] = np.nan

# BOS
all_bank_df['ISIN'] = np.where(all_bank_df['Bank']=='BOS', \
    bos_df['ISIN'],\
        all_bank_df['ISIN'])

# DB
all_bank_df['ISIN'] = np.where(all_bank_df['Bank']=='DB', \
    db_df['ISIN'],\
        all_bank_df['ISIN'])

# JPM
all_bank_df['ISIN'] = np.where(all_bank_df['Bank']=='JPM', \
    jpmorgan_df['ISIN'],\
        all_bank_df['ISIN'])

# DBS
all_bank_df['ISIN'] = np.where(all_bank_df['Bank']=='DBS', \
    dbs_df['ASSET_ISIN'],\
        all_bank_df['ISIN'])

# LGT
all_bank_df['ISIN'] = np.where(all_bank_df['Bank']=='LGT', \
    lgt_df['ISIN/ContrNr'],\
        all_bank_df['ISIN'])


# Sector
sector_df = mapping_df[['ISIN', 'Sector', 'Bank']].copy()
sector_df = sector_df.drop_duplicates()

final_df = pd.merge(all_bank_df, sector_df, on=['Bank', 'ISIN'], \
    how='left')

print("Saving File")
final_df.to_csv(os.path.join(output_file_path, output_filename), index=False)
print("File Saved")
print("Process Completed")
