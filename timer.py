class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Set the amount of seconds elapsed since the user typed for the last time to 0.
        """
        self.value = 0

    def increment(self):
        """
        Add 1 to the total amount of seconds elapsed since the user typed for the last time.
        """
        self.value += 1
