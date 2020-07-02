# python3

import os
import shutil
from os import listdir

# TODO: Walk through a working directory and search with certain file extension

os.chdir('C:/Users/Anna/Pictures')
working_directory = os.getcwd()
extension = 'jpg'
file_list_to_copy = []
for file in listdir(working_directory):
    if file.endswith('.' + extension):
        file_list_to_copy.append(file)
print(file_list_to_copy)

# TODO: Copy files to a new location
new_wd = 'C:/Users/Anna/Pictures/' + extension
if not os.path.isdir(new_wd):
    os.mkdir(new_wd)
for file in file_list_to_copy:
    src = working_directory + '\\' + file
    shutil.copy(src, new_wd)
shutil.rmtree(new_wd)

