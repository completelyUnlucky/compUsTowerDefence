
import os

# game = Battlefield()
# game.mainLoop()

#
# ROOT = os.getcwd()
# print(ROOT + '/maps')


for address, dirs, files in os.walk('.'):
    if not '.git' in address:
        print(address + '|||' + str(dirs) + '|||' + str(files))
