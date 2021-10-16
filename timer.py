class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = 0

    def increment(self):
        self.value += 1
