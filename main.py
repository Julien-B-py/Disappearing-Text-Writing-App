import threading
import time

from timer import Timer
from user import User
from window import Window


def countdown():
    while True:
        if user.typed:
            timer.increment()
            window.change_text_bg_color(timer.value)
            if timer.value >= 5:
                window.clear_text()
                user.reset_words_count()
                window.update_words_count(user.typed_words)
        time.sleep(1)


def key_pressed(event):
    if not user.typed:
        user.typed = True

    if event.char == ' ':
        user.increment_words_count()
        window.update_words_count(user.typed_words)

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
