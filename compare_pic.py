import cv2
from deepface import DeepFace
from cv2.typing import MatLike

def check_face(pic1: MatLike,pic2: MatLike)-> bool:
    """
    Takes 2 pic and compares the face and returns a boolean
    """

    return DeepFace.verify(pic2.copy(),pic1.copy())['verified']

pic1 = cv2.imread('testpic.jpg')
pic2 = cv2.imread('testpic2.jpg')


if __name__ == "__main__":
    if check_face(pic1,pic2):
        print('Matching')
    else:
        print('Not Matching')
