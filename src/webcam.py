import cv2
import time


class Webcam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def show_frame(self, text):

        ret, frame = self.cap.read()

        if ret:
            resized_frame = cv2.resize(frame, (479, 360))
            cv2.rectangle(resized_frame, (6, 6), (150, 25), (0, 0, 0), cv2.FILLED)
            cv2.putText(resized_frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, color=(0, 255, 0), fontScale=1, thickness=2)

            return resized_frame

        self.cap.release()

    def release(self):
        self.cap.release()

