# Rename files in the folders and sub folder
# Customize the naming pattern
import os

file_location = r'D:\Workspace\OneDrive - ICIMOD\2020\DataTools\Renamefiles'
network_location = r'\\192.168.10.67\e$\Data\Cordex\future\5km\tmin'
file_extension = '.nc'
update_text = "Cordex_tmin"

os.chdir(network_location)


# print(os.getcwd())


def rename_file(filename, extension):
    day_pos = filename.find('day_')
    if day_pos != -1:
        new_name = update_text + filename[day_pos + 3:] + extension
        return new_name
    return file_name + extension


for root, dirs, files in os.walk(network_location):
    name = root.split('\\')
    print(name[-1])
    for file in files:
        # print(file)
        if file.endswith(file_extension):
            file_name, file_extension = os.path.splitext(file)

            update_name = rename_file(file_name, file_extension)
            # os.rename(os.path.join(root, file), os.path.join(root, update_name))
            # print(os.path.join(root, file),'\n', os.path.join(root, update_name))
