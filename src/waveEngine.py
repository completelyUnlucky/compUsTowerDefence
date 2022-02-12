import re


class WaveEngine:
    def __init__(self, file):
        self.open = open(file).readlines()
        self.waves = []
        self.numbers = []
        self.words = []
        self.army = []
        self.test = []

    def run(self):
        self.split()
        self.find_numbers()
        self.find_str()
        print(self.generation())

    def split(self):
        for i in self.open:
            self.waves.append(list(i.split()))

    def find_numbers(self):
        for i in self.waves:
            for j in i:
                find = re.findall(r'\d+', j)
                str_find = ' '.join(find)
                self.numbers.append(int(str_find))
        return self.numbers

    def find_str(self):
        for i in self.waves:
            for j in i:
                find = re.findall(r'\D', j)
                str_find = ''.join(find)
                self.words.append(str(str_find))
        return self.words

    def generation(self):
        for i, j in zip(self.numbers, self.words):
            self.army.append(i * j)
        return self.army


wave = WaveEngine('waves.txt')
wave.run()
