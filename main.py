import threading
import cv2
from cv2.typing import MatLike
from deepface import DeepFace

cap = cv2.VideoCapture(0)

cv2.namedWindow('Check Face Match',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Check Face Match',600,600)


reference_img = cv2.imread("testpic2.jpg")

counter = 0
face_match = False

def check_face(frame: MatLike)-> None:
    """
    Takes a frame from the capture of cv2 and assigns true / false to the variable
    """
    global face_match

    try:
        if DeepFace.verify(frame,reference_img.copy())['verified'] :
            face_match = True
            print('Matching')
        else:
            face_match = False
            print('Not Matching')

    except ValueError:
        pass


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 5 == 0:
            try:
                threading.Thread(target=check_face, args=(frame,)).start()
            except ValueError:
                pass
        counter +=1 



        if face_match:

            cv2.putText(frame,"Match",(20,450),
                        cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,"No Match",(20,450),
                        cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

        cv2.imshow('Check Face Match',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


