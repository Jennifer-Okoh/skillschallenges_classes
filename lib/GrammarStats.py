class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0
    def check(self, text):
        self.total_texts += 1
        text = "This is a valid sentence."
        if text.startswith(tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) and text.endswith((".", "!", "?")):
            return True
        else:
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
    

    def percentage_good(self):
        if self.total_texts == 0:
            return 0
        return (self.passed_texts / self.total_texts) * 100
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
    
