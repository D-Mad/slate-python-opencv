
import cv2
 
  
cap = cv2.VideoCapture('test2.mp4')
  
while(True):
      
    # Capture frames in the video
    ret, frame = cap.read()
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    x,y,w,h = 0,0,200,250

# Create background rectangle with color
    cv2.rectangle(frame, (0,height), (width, height-50), (0,0,0),-1)
    # describe the type of font
    # to be used.
    font = cv2.FONT_HERSHEY_PLAIN
  
    # Use putText() method for
    # inserting text on video
    cv2.putText(frame, 
                'thanh dat', 
                (int(width-200),height-20), 
                font, 0.65, 
                (255, 255, 255), 
                1,
                cv2.LINE_8
               )
  
    # Display the resulting frame
    cv2.imshow('video', frame)
  
    # creating 'q' as the quit 
    # button for the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()