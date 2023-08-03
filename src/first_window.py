import cv2


class First:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):

        cv2.namedWindow("First Window", cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow("First Window", 30, 210)

        while True:

            frame = self.webcam.show_frame("Delay : No")
            cv2.imshow("First Window", frame)

            if cv2.waitKey(1) & 0xff == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()
