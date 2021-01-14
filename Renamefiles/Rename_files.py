# Rename files inside the single folder only
import os

file_location = r'D:\Workspace\OneDrive - ICIMOD\2020\DataTools\Renamefiles\files'
network_location = r'\\192.168.10.67\e$\Data\Cordex\future\5km\pr\SMHI-CNRM-CM5-r1i1p1_rcp85'
file_extension = '.nc'
update_text = "Cordex_pr"

os.chdir(network_location)


# print(os.getcwd())


def rename_file(filename, extension):
    day_pos = filename.find('day_')
    # print(day_pos)
    if day_pos != -1:
        new_name = update_text + filename[day_pos + 3:] + extension
        return new_name


for file in os.listdir():
    if file.endswith(file_extension):
        file_name, file_extension = os.path.splitext(file)
        update_name = rename_file(file_name, file_extension)
        # os.rename(file, update_name)
