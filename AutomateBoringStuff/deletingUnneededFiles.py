import os
from os import listdir

work_dir = os.getcwd()
work_dir_files = [f for f in listdir(work_dir) if os.path.getsize('.\\%s' % f) > 700]
for file in work_dir_files:
    print(os.path.abspath('.\\%s' % file))
