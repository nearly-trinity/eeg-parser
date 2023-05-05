import os
import pandas as pd

# will use this for actual set
from concurrent.futures import ProcessPoolExecutor

# with ProcessPoolExecutor() as executor:
#         futures = []
#         for csv_file in csv_files:
#             futures.append(executor.submit(pd.read_csv, csv_file.path, usecols=[
#                 "Fp1","Fp2","F7","F3","Fz","F4","F8","FC3","FCz","FC4","T7","C3","Cz",
#                 "C4","T8","CP3","CPz","CP4","P7","P3","Pz","P4","P8","O1","Oz","O2",
#                 "VPVA","VNVB","HPHL","HNHR","Erbs","OrbOcc","Mass"
#             ]))
        
#         # Store the loaded data in parsed_data
#         for future in futures:
#             data = future.result().astype('float')
#             parsed_data[subject_number] = data.copy(deep=True)


dir_path = "C:\\Users\\early\\OneDrive\\eeg-parser\\data\\derivatives"

parsed_data = {}

for entry in os.scandir(dir_path):

    if not entry.is_dir():
        continue

    subject_path = os.path.join(entry.path, "ses-1", "eeg")
    
    if not os.path.isdir(subject_path):
        continue

    subject_number = entry.name.split('-')[1]
    # print(subject_path)
    
    if os.path.isdir(subject_path):
        
        for file in os.listdir(subject_path):
    
            print(file) 

            data = pd.read_csv(os.path.join(subject_path, file))
            
            data = data.astype('float')

            parsed_data[subject_number] = data.copy(deep=True)
    

