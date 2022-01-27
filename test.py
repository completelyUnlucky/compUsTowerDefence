import os
import sys
path = '/Users/mac2/PycharmProjects/pythonProject1/compUsTowerDefence'

# for dirs, folder, files in os.walk(path):
#     print('каталог ', dirs)
#     print('папка ', folder)
#     print('файл ', files)
#     for file in files:
#         print(os.path.join(dirs, file))
#     print('\n')

# print(os.getcwd())
# print(sys.path[0])
print(os.path.dirname('compUsTowerDefence'))
ROOT_DIR = os.path.dirname(os.path.abspath("test.py"))
print(ROOT_DIR)