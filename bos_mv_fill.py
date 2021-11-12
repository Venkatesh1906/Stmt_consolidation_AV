import pandas as pd
import numpy as np
import os


base_dir = "./Data/pos_consolidation"
filename = 'Appended_File_Bos.csv'
des_filename = 'bos_description.csv'

bos_df = pd.read_csv(os.path.join(base_dir, filename))
bos_desc = pd.read_csv(os.path.join(base_dir, des_filename))
bos_desc = bos_desc.replace('Market Value', 'MarketValue')

bos_df['SubAssetDescription'] = bos_df['SubAssetDescription'].str.strip()
bos_desc['Sub Asset Description'] = bos_desc['Sub Asset Description'].str.strip()
bos_desc['MV Col'] = bos_desc['MV Col'].str.strip()

bos_df['MV_value'] = np.nan

for asset, col_to_take in zip(bos_desc['Sub Asset Description'], bos_desc['MV Col']):
 
    if not asset in bos_df['SubAssetDescription'].unique().tolist():
        print(f"Asset Not Found {asset}")
        
    if not col_to_take in bos_df.columns.tolist():
        print(f"MV Col Not found {col_to_take}")
    try:
        bos_df['MV_value'] = np.where(bos_df['SubAssetDescription'] == asset, \
            bos_df[col_to_take], \
                bos_df['MV_value'])
    except Exception as exc:
        print (f"Exception occured at {asset}, {col_to_take}")

# bos_df.to_csv('./Output/bos_mv_col_v0.2.csv', index=False)