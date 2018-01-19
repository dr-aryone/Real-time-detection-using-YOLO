import cv2
cap = cv2.VideoCapture('http://192.168.0.3:8080/video')

while True:
  ret, frame = cap.read()
  gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  cv2.imshow('Video', gray)

  if cv2.waitKey(1) == 27:
    exit(0)