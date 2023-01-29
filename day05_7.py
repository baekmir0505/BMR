# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# 외부 모듈 설치 : pip install 모듈명

# pip install python-opencv  (일반 파이썬)
# pip install opencv-python (아나콘다)
import cv2

# img = cv2.imread('img1.png')           # 이미지를 스캔해줘 (읽어줘)
# cv2.imshow('title', img)               # 보여줘

# cv2.waitKey(0)                         # 무한대기 (안하면 img 바로 사라짐)

def cv_img(path):
    img = cv2.imread('bogati.png')
    cv2.imshow('title', img)
    cv2.waitKey(0)

cv_img('bogati.png')
# cv_img('../img1.png')   # ..은 뒤로가기 설정이다.