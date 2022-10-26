import cv2
  
  
cap = cv2.VideoCapture('test2.mp4')
  

ret, frame = cap.read()
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(type(height),width)