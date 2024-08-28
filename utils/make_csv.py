import pandas as pd
import os

def write_to_csv(file_name,data):
    new_data_frame = pd.DataFrame(data)
    if os.path.exists(file_name):
        dataFrame = pd.DataFrame(file_name)
        combined_data = pd.concat([dataFrame,new_data_frame],index=False)
        print(combined_data)
        combined_data.to_csv()
    else:
        new_data_frame.to_csv(file_name,index=False)