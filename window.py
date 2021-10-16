from tkinter import Tk, Text, END, messagebox


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title('Disappearing Text Writing App')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.create_widgets()

    def create_widgets(self):
        self.text_area = Text(self, width=140, height=30)
        self.text_area.grid(row=0, column=0)
        self.text_area.focus_set()

    def clear_text(self):
        self.text_area.delete('1.0', END)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
