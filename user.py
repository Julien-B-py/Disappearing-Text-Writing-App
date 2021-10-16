class User:
    def __init__(self):
        # Has the user started to type anything ?
        self.typed = False
        self.reset_words_count()

    def increment_words_count(self):
        """
        Add 1 to the total amount of words typed by the user
        """
        self.typed_words += 1

    def reset_words_count(self):
        """
        Set the amount of words typed by the user to 0.
        """
        self.typed_words = 0
