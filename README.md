# MakingVideo
1. Bird's eye view와 Dash View 프레임이 합쳐진 파일을 먼저 두개로 나눈다. [Divide.py](https://github.com/engineerjkk/MakingVideo/blob/main/divide.py)  
2. 시퀀스 이미지 프레임에서 먼저 번호순으로 정렬한다.(이미 정렬돼있다면 안해도된다.) [Sorting](https://github.com/engineerjkk/MakingVideo/blob/main/sorting.py)  
3. 프레임을 동영상으로 만든다. 원하는대로 프레임 속도를 설정할 수 있다. [Convert](https://github.com/engineerjkk/MakingVideo/blob/main/Convert.py)  
4. 각각이 만든 두개의 동영상을 이어 붙인다. [Combine.py](https://github.com/engineerjkk/MakingVideo/blob/main/Combine.py)

> 주의할 점 : 본인의 PC의 경우에는 한번에 1000장을 초과해 프레임을 처리할경우 Fail to allocate가 되어 error가 떴다. 

> 따라서 본인은 1000장씩만 했지만 사양이 좋다면 한번에 큰 동영상을 처리할 수 있다.

> input
![image](https://user-images.githubusercontent.com/76835313/126627074-6dd815e3-5abd-4da4-9abc-29d7db10d390.png)
> output
![image](https://user-images.githubusercontent.com/76835313/126627137-ad7672c6-5ab8-4d5d-95d9-fb68fc2237df.png)
