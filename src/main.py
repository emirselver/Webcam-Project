import threading
from webcam import Webcam
from first_window import First
from second_window import Second
from third_window import Third

webcam = Webcam()

t1 = threading.Thread(target=First(webcam).show)
t2 = threading.Thread(target=Second(webcam).show)
t3 = threading.Thread(target=Third(webcam).show)

t2.daemon = True
t3.daemon = True

t1.start()
t2.start()
t3.start()

t1.join()



