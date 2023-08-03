import cv2
import time


class Second:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):

        cv2.namedWindow("Second Window", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("Second Window", 519, 210)

        while True:
            frame = self.webcam.show_frame("Delay : 0.5 Sec.")
            cv2.imshow("Second Window", frame)
            time.sleep(0.5)

            if cv2.waitKey(1) & 0xff == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()
