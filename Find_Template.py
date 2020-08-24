import numpy as np
import matplotlib.pyplot as plt
import os

video_name_1 = "FoodMarket.yuv"
video_name_2 = "PierSeaside.yuv"

template_name_1 = "template_1.yuv"
template_name_10 = "template_10.yuv"

w = 1920
h = 1080
px = w * h

video_size = os.path.getsize(video_name_1)
video_frames = video_size // (px*3 // 2)

video_YUV = np.fromfile(video_name_1, dtype='uint8')

template_YUV_1 = np.fromfile(template_name_1, dtype='uint8')
template_Y_1 = template_YUV_1[0:px]

template_YUV_10 = np.fromfile(template_name_10, dtype='uint8')
template_Y_10 = template_YUV_10[0:px]

ab_min_1 = 229452970
ab_min_10 = 229452970
min_frame_1 = 0
min_frame_10 = 0
for i in range(video_frames):
    start = i * (px*6)//4
    end = start + px
    video_Y = video_YUV[start:end]

    ab_1 = abs(video_Y.astype(float) - template_Y_1)
    ab_sum_1 = np.sum(ab_1)
    if(ab_min_1 > ab_sum_1):
        min_frame_1 = i
        ab_min_1 = ab_sum_1

    ab_10 = abs(video_Y.astype(float) - template_Y_10)
    ab_sum_10 = np.sum(ab_10)
    if(ab_min_10 > ab_sum_10):
        min_frame_10 = i
        ab_min_10 = ab_sum_10

print(min_frame_1)
print(min_frame_10)

if(min_frame_1 > min_frame_10):
    start_frame = min_frame_10
    end_frame = min_frame_1
else:
    start_frame = min_frame_1
    end_frame = min_frame_10


start = start_frame * (px*6)//4
end = (end_frame+1) * (px*6)//4

write_YUV = video_YUV[start:end]

# U  (px*6)//4
# sse , sad
#start = min_frame * (px*6)//4
#end = start + px
#video_Y = video_YUV[start:end].reshape(h, w)

# plt.imshow(video_Y)
# plt.show()
