#정렬이 안된 숫자를 1~ 정렬해 나열합니다.

import os

file_path = 'I:\junekoo.kang\yolo_mark\data\DataSet'
file_names = os.listdir(file_path)
print(file_names)

i = 1

for name in file_names:
    if 'jpg' in name:
        src = os.path.join(file_path, name)
        dst = str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)

    if 'txt' in name:
        src = os.path.join(file_path, name)
        dst = str(i) + '.txt'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1

print("Finished")