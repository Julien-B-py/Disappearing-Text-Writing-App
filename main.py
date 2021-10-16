import threading
import time

from timer import Timer
from user import User
from window import Window


def main():
    while True:
        # If user typed any character: increment the timer and make text background color darker over time
        if user.typed:
            timer.increment()
            window.change_text_bg_color()

            # If timer reached 5s: delete all the text
            if timer.value >= 5:
                window.clear_text()

                # If user want to start again:
                if window.ask_try_again():
                    user.typed = False
                    user.reset_words_count()
                    window.reset_text_bg_color()
                    window.update_words_count()
                    timer.reset()

        time.sleep(1)


if __name__ == "__main__":
    timer = Timer()
    user = User()
    window = Window(timer, user)

    # Using thread to run main loop and be able to display the user interface at the same time
    # daemon = True: kill the thread when main program exits
    t = threading.Thread(target=main, daemon=True)
    # Start the main loop
    t.start()
    # Required to display app window
    window.mainloop()
