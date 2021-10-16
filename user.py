class User:
    def __init__(self):
        self.typed = False
        self.reset_words_count()

    def increment_words_count(self):
        self.typed_words += 1

    def reset_words_count(self):
        self.typed_words = 0
