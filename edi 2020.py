import urllib.request
import urllib
import cv2
import numpy as np
import ssl
#background subtraction for detecting changes in the environment
#fgbg = cv2.createBackgroundSubtractorMOG2()
video=cv2.VideoCapture(0)
check,first=video.read()
while True:
    video=cv2.VideoCapture(0)
    check,frame=video.read()
    print(check)
    print(frame)
    cv2.imshow('frrr',frame)
    cv2.imshow('first frame',first)
    d=cv2.absdiff(first,frame)
    print(d)
    cv2.imshow('diff',d)
    print(check)
    print(frame)
    #f=fgbg.apply(frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
'''ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://192.168.43.1:8080/'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('temp',img)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;'''

