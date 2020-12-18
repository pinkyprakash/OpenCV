import cv2
import datetime
cap = cv2.VideoCapture(0)

#cap.set(3,1208)
#cap.set(4,720)

#Default Size
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Rseting the video frame size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#Print the size of the frame after resize
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame  = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        #frame = cv2.putText(frame, 'Jayaprakash Veugopal', (150, 500),font, 3, (0, 255, 255), 5, cv2.LINE_AA)

        #text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        #Above code and belwo code both are same
        datet = 'Date Time: ' + str(datetime.datetime.now())
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) +\
               ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #+\

        frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        frame = cv2.putText(frame, datet, (10, 100), font, 1,(0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, 'Sana and JP', (10, 150), font, 1,(0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()