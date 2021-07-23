import os
import shutil
#선 조건 : 용량이 0KB TXT 파일은 직접 삭제해주어야 합니다.

#라벨링된 텍스트 파일을 먼저 지정 폴더에 옮긴다.
for i in os.listdir('./data/img/'):
    print(i)
    if 'txt' in i:
        shutil.copyfile('./data/img/'+i,'./data/DataSet/'+i)
        print("Passing TxT : "+i)

#텍스트 파일명을 리스트에 담는다.
temp=[]
for i in os.listdir('./data/DataSet/'):
    #print(k)
    a = i[:-4]
    temp.append(a)
    print("Listing.. : "+i)

#리스트에 있는 이름명의 이미지만 옮긴다.
for i in os.listdir('./data/img/'):
    b=i[:-4]
    print(b)
    if b in temp:
        shutil.copyfile('./data/img/' + i, './data/DataSet/' + i)
        print("Passing Img : "+i)


print("Finished")

