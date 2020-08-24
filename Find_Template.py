import numpy as np
import os

video_name_1 = "FoodMarket.yuv"
video_name_2 = "PierSeaside.yuv"

template_name_1 = "template_1.yuv"
template_name_10 = "template_10.yuv"

w = 1920  # 가로
h = 1080  # 세로
px = w * h

video_size = os.path.getsize(video_name_1)  # 파일 사이즈
video_frames = video_size // (px*3 // 2)  # 비디오 총 프레임

# 파일 불러오기
video_YUV = np.fromfile(video_name_1, dtype='uint8')

template_YUV_1 = np.fromfile(template_name_1, dtype='uint8')
template_Y_1 = template_YUV_1[0:px]

template_YUV_10 = np.fromfile(template_name_10, dtype='uint8')
template_Y_10 = template_YUV_10[0:px]

# (비디오 - template) 의 절대값의 최소값
ab_min_1 = 229452970  # 임의의 최대값으로 시작
ab_min_10 = 229452970  # 임의의 최대값으로 시작
min_frame_1 = 0
min_frame_10 = 0

for i in range(video_frames):
    start = i * (px*6)//4
    end = start + px
    video_Y = video_YUV[start:end]

    ab_1 = abs(video_Y.astype(float) - template_Y_1)  # 각 항의 차의 절대값을 배열로 만듦
    ab_sum_1 = np.sum(ab_1)  # 배열의 숫자를 모두 더함
    if(ab_min_1 > ab_sum_1):  # 더한 값이 최소값보다 작으면 최소값에 더한 값을 넣음
        min_frame_1 = i
        ab_min_1 = ab_sum_1

    ab_10 = abs(video_Y.astype(float) - template_Y_10)  # 위와 동일
    ab_sum_10 = np.sum(ab_10)
    if(ab_min_10 > ab_sum_10):
        min_frame_10 = i
        ab_min_10 = ab_sum_10

if(min_frame_1 > min_frame_10):
    start_frame = min_frame_10
    end_frame = min_frame_1
else:
    start_frame = min_frame_1
    end_frame = min_frame_10
print(start_frame)
print(end_frame)
