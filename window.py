from tkinter import Tk, Text, END, messagebox, Label, WORD


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.title('Disappearing Text Writing App')
        self.bg_color_vs_time = {
            "1": "#ffffff",
            "2": "#bfbfbf",
            "3": "#808080",
            "4": "#404040",
            "5": "#000000",
        }
        self.create_widgets()

    def create_widgets(self):
        self.top_label = Label(text='Don’t stop writing, or all progress will be lost', font=('Montserrat', 10))
        self.top_label.pack(pady=10)
        self.text_area = Text(self, width=46, height=25, font=('Montserrat', 14), wrap=WORD)
        self.text_area.pack(padx=20)
        self.text_area.focus_set()
        self.count_label = Label()
        self.count_label.config(text='0 words')
        self.count_label.pack(pady=10)

    def clear_text(self):
        self.text_area.delete('1.0', END)

    def change_text_bg_color(self, timer_value):
        timer_value = str(timer_value)
        self.text_area.config(bg=self.bg_color_vs_time.get(timer_value))

    def reset_text_bg_color(self):
        self.text_area.config(bg='white')

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def update_words_count(self, count):
        self.count_label.config(text=f'{count} words')
