import cv2

cv2.namedWindow('Take A Picture',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Take A Picture',700,700)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Cant\'t open Camera')
    exit()


# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Failed to grab Frame')
        break

    cv2.imshow('Take A Picture',frame)

    key = cv2.waitKey(1)
    if key == ord('p'):
        cv2.imwrite('testpic2.jpg',frame)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


