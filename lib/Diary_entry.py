#====================================
# class DiaryEntry:
#     def __init__(self, title, contents):
#         self.title = title
#         self.contents = contents
#         self.words = contents.split()
#         self.current_position = 0


#     def format(self):
#         return f"{self.title}: {self.contents}"

#     def count_words(self):
#         return len(self.words)

#     def reading_time(self, wpm):
#         return self.count_words() // wpm +int(self.count_words() % wpm > 0)
    
#     def reading_chunk(self, wpm, minutes):
#         if wpm == 0 or minutes == 0:
#             return ""
    
#         words_to_read = wpm * minutes
#         chunk = ' '.join(self.words[self.current_position:self.current_position + words_to_read])
#         self.current_position += words_to_read
#         if self.current_position >= len(self.words):
#             self.current_position = 0
#             return chunk
        
        
#==========================================




import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.current_position = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        contents_word_count = len(self.contents.split())
        # return self.count_words() // wpm + int(self.count_words() % wpm > 0)
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        if wpm == 0 or minutes == 0:
            return ""
        
        words_to_read = wpm * minutes
        chunk = ' '.join(self.words[self.current_position:self.current_position + words_to_read])
        self.current_position += words_to_read
        if self.current_position >= len(self.words):
            self.current_position = 0  # Restart from the beginning
        return chunk