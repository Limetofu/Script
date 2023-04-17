import os


import shelve
import random

import os
for root, subfolders, filenames in os.walk('e:/data'):
    print(f'ROOT:{root}'.center(80, '='))
    print('Subfolders: '.ljust(15), subfolders)
    print('Files: '.ljust(15), filenames)
    print('\n')