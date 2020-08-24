# Find YUV 사용법

같은 폴더 안에 

- "FoodMarket.yuv"
- "PierSeaside.yuv"
- "template_1.yuv"
- "template_10.yuv"

파일이 들어있어야 합니다.

## 비디오 파일 바꾸기

아래의 두 문장에서 video_name_1을 video_name_2 로 바꿔야 합니다.

``` python
video_size = os.path.getsize(video_name_1)  # video_name_2
video_YUV = np.fromfile(video_name_1, dtype='uint8') # video_name_2
```
