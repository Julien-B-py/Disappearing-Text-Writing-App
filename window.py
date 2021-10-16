from tkinter import Tk, Text, END, messagebox, Label, WORD


class Window(Tk):
    def __init__(self, timer, user):
        super().__init__()
        self.title("Disappearing Text Writing App")
        # Call key_pressed function everytime a key is pressed
        self.bind("<Key>", self.key_pressed)
        # Make the close button call on_closing function to display a messagebox
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Create a dict with timer value as key and text background color as value.
        # Everytime the timer value will change we will change the background color.
        self.bg_color_vs_time = {
            "1": "#ffffff",
            "2": "#bfbfbf",
            "3": "#808080",
            "4": "#404040",
            "5": "#000000",
        }

        self.timer = timer
        self.user = user

        self.create_widgets()

    def create_widgets(self):
        """Widgets creation and layout setup"""
        self.top_label = Label(text="Don’t stop writing, or all progress will be lost", font=("Montserrat", 10))
        self.top_label.pack(pady=10)
        self.text_area = Text(self, width=46, height=25, font=("Montserrat", 14), wrap=WORD)
        self.text_area.pack(padx=20)
        self.text_area.focus_set()
        self.count_label = Label()
        self.count_label.config(text="0 words")
        self.count_label.pack(pady=10)

    def clear_text(self):
        """Clear the text widget content"""
        self.text_area.delete("1.0", END)

    def change_text_bg_color(self):
        """
        Change the Text widget background color depending on the current timer value.
        """
        # Transform value to string to pass it as key and get the corresponding color value from the dict.
        timer_value = str(self.timer.value)
        self.text_area.config(bg=self.bg_color_vs_time.get(timer_value))

    def reset_text_bg_color(self):
        """
        Change the Text widget background color to default value: white.
        """
        self.text_area.config(bg="white")

    def on_closing(self):
        """
        Prompt user when he clicks on close button.
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def update_words_count(self):
        """
        Change the label text to display the current amount of words typed by the user.
        """
        self.count_label.config(text=f"{self.user.typed_words} words")

    def ask_try_again(self):
        """
        Prompt user when he failed to type any text after 5 seconds.
        If answer is no app will close.
            Returns:
                bool: True if user wants to restart.
        """
        user_answer = messagebox.askquestion("You failed",
                                             f"You wrote {self.user.typed_words} words before the app deleted "
                                             f"everything\nTry again?")
        if user_answer == "no":
            self.destroy()
        return True

    def key_pressed(self, event):
        """
        Key presses analyze function.
        Detect the first keypress to start the timer.
        Detect any space character typed by the user to increase the total number of words.
        As long as the user is typing, set the timer to 0.
            :param event: Any keypress (tkinter.Event) performed by the user on the app window.
        """
        if not self.user.typed:
            self.user.typed = True

        if event.char == " ":
            self.user.increment_words_count()
            self.update_words_count()

        self.timer.reset()
