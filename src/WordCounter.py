class WordCounter:
    def __init__(self, sentence) -> None:
        self.sentence = sentence
        self.__count = 0
    

    def count_words(self):
        self.__count = len(self.sentence.split())
    
    def get_word_count(self):
        return self.__count
    
    def get_shortest_word(self):
        words = self.sentence.split()
        min_len = len(words[0])
        for word in words:
            if len(word) < min_len:
                min_len = len(word)
        return min_len
    
    def get_longest_word(self):
        words = self.sentence.split()
        max_len = len(words[0])
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
        return max_len