import sys

import numpy as np

import cv2

cap = cv2.VideoCapture('./output.avi')

if not cap.isOpened():
    print("Video open failed!")
else:
    # 이미지 프레임 사이즈값을 받습니다.
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 전체 프레임 수값을 받습니다.
    frame_cnt = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 초당 프레임 값을받습니다.
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 한 프레임당 걸리는 시간을 받습니다.
    delay = int(1000 / fps)
    # 영상을 저장할 코덱정보를 저장합니다.
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # *'DIVX' == 'D', 'I', 'V', 'X'
    # 영상을 저장할 이름을 지정합니다.
    outputVideo = cv2.VideoWriter('Labeled_Output.avi', fourcc, fps, (w, h))

    # 전체 프레임까지 영상 루프를 돌립니다.
    for i in range(frame_cnt):
        ret, frame = cap.read()
        print(i)

        if not ret:  break
        label = '%d' % (i)


        # 좌표는 (X,Y 임을 잊지맙시다)
        frame = cv2.putText(frame, label, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        #cv2.imshow('Labeled', frame)

        outputVideo.write(frame)
        # 프레임당 기존의 딜레이를 줍니다.
        cv2.waitKey(delay)

        if cv2.waitKey(10) == 27:  break  #

    print("finished")

outputVideo.release()
cap.release()
cv2.destroyAllWindows()