class EvenNumbers:
    """Перебор чётных чисел в определённом числовом диапазоне"""

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1

        while self.i in range(self.start, self.end):
            if self.i % 2 == 0:
                return self.i

            if self.i >= self.end:
                raise StopIteration()

            if self.i < self.start:
                pass

            elif self.i / 2 != 0:
                pass


en = EvenNumbers(10, 25)
for i in en:
    print(i)
