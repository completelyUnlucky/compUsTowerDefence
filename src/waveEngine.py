import main
import re
from npcs.runner import Warrior


class WaveEngine:
    def __init__(self, file):
        self.open = open(file).readlines()
        self.waves = []
        self.prepare_data()

    def prepare_data(self):
        self.split()
        self.find_numbers()
        self.find_str()
        self.dict()

    def split(self):
        for i in self.open:
            self.waves.append(list(i.split()))

    def find_numbers(self):
        numbers = []
        for line in self.open:
            numbers.append([])
            for i in line:
                for j in i:
                    if j.isdigit():
                        numbers[-1].append(int(j))
        return numbers

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
        dictionary = {'warrior': Warrior}
        tmp = []
        for i, j in zip(dictionary, self.find_numbers()):
            tmp.append([])
            for nums in range(len(self.find_numbers())):
                for num in range(len(self.find_numbers()[nums])):
                    tmp[-1].append(dictionary[i])
        print(tmp)


wave = WaveEngine(main.find_file('example.waves'))
