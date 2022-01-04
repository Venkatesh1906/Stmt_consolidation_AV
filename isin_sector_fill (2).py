# Important Libs
import os
import pandas as pd
import numpy as np 
from tqdm import tqdm


# Data folder
files_folder = r'C:\Users\Shubham\Desktop\Analytics_Projects\POS_Consolidation\Codes\Sid_request_23rddec'

# Save file to 
output_file_path = r'C:\Users\Shubham\Desktop\Analytics_Projects\POS_Consolidation\Codes\Sid_request_23rddec'

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

# # BOS
# bos_df_ = all_bank_df[all_bank_df['Bank']=='BOS'].copy().reset_index(drop=True)
# bos_df_['ISIN'] = np.where(bos_df_['Bank']=='BOS', \
#     bos_df['ISIN'],\
#         bos_df_['ISIN'])

# DB
db_df_ = all_bank_df[all_bank_df['Bank']=='DB'].copy().reset_index(drop=True)
db_df_['ISIN'] = np.where(db_df_['Bank']=='DB', \
    db_df['ISIN'],\
        db_df_['ISIN'])

# JPM
jpm_df_ = all_bank_df[all_bank_df['Bank']=='JPM'].copy().reset_index(drop=True)
jpm_df_['ISIN'] = np.where(jpm_df_['Bank']=='JPM', \
    jpmorgan_df['ISIN'],\
        jpm_df_['ISIN'])

# DBS
dbs_df_ = all_bank_df[all_bank_df['Bank']=='DBS'].copy().reset_index(drop=True)
dbs_df_['ISIN'] = np.where(dbs_df_['Bank']=='DBS', \
    dbs_df['ASSET_ISIN'],\
        dbs_df_['ISIN'])

# LGT
lgt_df_ = all_bank_df[all_bank_df['Bank']=='LGT'].copy().reset_index(drop=True)
lgt_df_['ISIN'] = np.where(lgt_df_['Bank']=='LGT', \
    lgt_df['ISIN/ContrNr'],\
        lgt_df_['ISIN'])

# Combining all the data
all_bank_df_ = pd.concat([#bos_df_,
 db_df_, jpm_df_, dbs_df_, lgt_df_],\
    axis=0,
    ignore_index=True
)


# Sector
sector_df = mapping_df[['ISIN', 'Sector', 'Bank']].copy()
sector_df = sector_df.drop_duplicates()

final_df = pd.merge(all_bank_df_, sector_df, on=['Bank', 'ISIN'], \
    how='left')

print("Saving File")
final_df.to_csv(os.path.join(output_file_path, output_filename), index=False)
print("File Saved")
print("Process Completed")
