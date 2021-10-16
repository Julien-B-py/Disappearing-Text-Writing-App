import threading
import time

from timer import Timer
from user import User
from window import Window


def countdown():
    while True:
        if user.typed:
            timer.increment()
            if timer.value >= 5:
                window.clear_text()
        time.sleep(1)


def key_pressed(event):
    if not user.typed:
        user.typed = True
    timer.reset()


window = Window()
window.bind("<Key>", key_pressed)
timer = Timer()
user = User()

t1 = threading.Thread(target=countdown)
# Kill thread when main program exits
t1.daemon = True
t1.start()

window.mainloop()
