#먼저 해당 폴더내에 분리하고싶은 폴더를 만든뒤 실행합니다

import os
import shutil

for i in os.listdir('./frames/'):
    print(i)
    if '_b' in i:
        shutil.copyfile('./frames/'+i,'./BirdeyeView/'+i)
    else:
        shutil.copyfile('./frames/'+i,'./DashView/'+i)

print("Finished")