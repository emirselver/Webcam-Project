import cv2
import time


class Third:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):

        cv2.namedWindow("Third Window", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("Third Window", 1008, 210)

        while True:

            frame = self.webcam.show_frame("Delay : 1 Sec.")
            cv2.imshow("Third Window", frame)
            time.sleep(1)

            if cv2.waitKey(1) & 0xff == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()
