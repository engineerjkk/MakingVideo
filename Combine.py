import sys

import numpy as np

import cv2






# 두 개의 동영상을 열어서 cap1, cap2로 지정

cap1 = cv2.VideoCapture('./Dash1000.avi')

cap2 = cv2.VideoCapture('./Bird1000.avi')

if not cap1.isOpened() or not cap2.isOpened():

    print('video open failed!')

    sys.exit()



# 두 동영상의 크기, FPS는 같다고 가정함

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap1.get(cv2.CAP_PROP_FPS)



print('frame_cnt1:', frame_cnt1)

print('frame_cnt2:', frame_cnt2)

print('FPS:', fps)



delay = int(1000 / fps)



w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))

h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')


# 출력 동영상 객체 생성

out = cv2.VideoWriter('output.avi', fourcc, fps, (w*2, h))








for i in range(frame_cnt1):

    ret1, frame1 = cap1.read()

    ret2, frame2 = cap2.read()



    if not ret1 or not ret2:

        print('frame read error!')

        sys.exit()



    dx = int(w)


    frame = np.zeros((h, w*2, 3), dtype=np.uint8)

    #세로크기, 가로크기, 컬러영상이니까 3



    frame=cv2.hconcat([frame1,frame2])


    out.write(frame)

    print('.', end='')

    #cv2.imshow('output', frame)

    #cv2.waitKey(delay)




print('\noutput.avi file is successfully generated!')



cap1.release()

cap2.release()

out.release()

cv2.destroyAllWindows()

