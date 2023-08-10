import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,650)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,650)


reference_img = cv2.imread("reference.jpg")

counter =0
face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        try:
            threading.Thread(target=check_face, args=(frame.copy())

    key = cv2.waitKey(1)
    if key == ord(q):
        cv2.destroyAllWindows()




