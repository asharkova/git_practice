import os
import re

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

for file in missed_files:
    created_file = open(file, "w")
    created_file.close()
