import main
import re


class WaveEngine:
    def __init__(self, file):
        self.open = open(file).readlines()
        self.waves = []
        self.prepare_data()

    def prepare_data(self):
        self.split()
        # self.find_numbers()
        self.find_str()
        self.waves = self.find_str()
        self.dict()

    def split(self):
        for i in self.open:
            self.waves.append(list(i.split()))

    # def find_numbers(self):
    #     numbers = []
    #     for i in self.waves:
    #         for j in i:
    #             find = re.findall(r'\d+', j)
    #             num_find = ' '.join(find)
    #             numbers.append(int(num_find))
    #     return numbers

    def find_str(self):
        waves = []
        for line in self.open:
            string = line.split()
            waves.append([])
            for i in string:
                for nums, j in enumerate(i):
                    if j.isdigit():
                        waves[-1].append((i[:nums] + ' ') * int(nums))
                        break
        return waves

    def dict(self):
        dictionary = {}
        # for words in self.waves:
        #     for i in words[0]:
        #         if i == ' ':


wave = WaveEngine(main.find_file('example.waves'))

