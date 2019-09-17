class Arith():
    def __init__(self, word):
        self.word = word

    def add(self, x):
        numbers = {'zero': 0, 'one': 1, 'two': 2,
                   'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8,
                   'nine': 9, 'ten': 10,'eleven': 11,
                   'twelve': 12, 'thirteen': 13, 'fourteen':14,
                   'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
                   'eighteen': 18, 'nineteen': 19, 'twenty': 20}
        total = numbers.get(self.word) + numbers.get(x)
        return [k for k, v in numbers.items() if v == total][0]
