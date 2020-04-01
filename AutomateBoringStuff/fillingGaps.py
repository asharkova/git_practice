import os
import re
from os import listdir

work_dir = os.getcwd()
prefix = 'capitalquiz'
prefix_files = [f for f in os.listdir(work_dir) if prefix in os.path.basename('\\%s' % f)]
missed_files = []
j = 1
print(sorted(prefix_files))
for file in sorted(prefix_files):
    while True:
        checking_prefix = prefix + '%s.txt' % j
        if checking_prefix != file:
            missed_files.append(checking_prefix)
            j += 1
        else:
            j += 1
            break
print(missed_files)

missing_place = int(re.search('\d', missed_files[0]).group(0))
for index in range(missing_place - 1, len(prefix_files)):
    os.rename(r'.\\' + prefix_files[index], r'.\\{0}{1}.txt'.format(prefix, str(index + 1)))
renamed_files = [f for f in os.listdir(work_dir) if prefix in os.path.basename('\\%s' % f)]
print(renamed_files)
