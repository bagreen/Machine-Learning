from collections import defaultdict
from random import choices

# gives by Peter, adds a default entry of each letter
def distribution():
    result = defaultdict(int)
    
    for i in range(26):
        result[chr(i + ord('a'))] = 0.0001
    return result

# class that babbles
class babbler:
    # initalizes number of letters to make ngrams from, the text, and the counts dict
    # also assembles the dict
    def __init__(self, n, filename):
        self.n = n
        self.counts = defaultdict(distribution)
        self.text = open(filename).read().lower().replace('\n', ' ')

        for i in range(0, len(self.text)):
            ngram = self.text[i:i + n]

            if i + n < len(self.text):
                self.counts[ngram][self.text[i + n]] += 1

    # babbles based on a starting sentence and continues until num_more_chars
    def babble(self, start, num_more_chars):
        babbling = start[:self.n]

        # gets last characters to look at, checks the following possible entries and their weights, then picks one at random
        for i in range(num_more_chars):
            last_char = babbling[-self.n:]
            entries = list(self.counts[last_char].keys())
            values  = list(self.counts[last_char].values())
            babbling += choices(entries, values)[0]
        return babbling

b = babbler(5, 'moby.txt')
print(b.babble('Especially', 200))
