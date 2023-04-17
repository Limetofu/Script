import os
import random
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(filename)s(%(lineno)d): %(levelname)s - %(message)s'
)

folder_no = 0

ext = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']

# quota 를 가지고서, 폴더에 들어간 후에, 남겨진 quota 를 다시 분배해서 들어가면 된다.


def make_random_folders(count):
    global folder_no

    if not count: return

    os.mkdir(f'folder{folder_no}')
    os.chdir(f'folder{folder_no}')

    folder_no += 1
    count -= 1
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount


report_home = 'E:/3_1/Script/Day_10/for_test'


def make_random_root_folder():
    try:
        os.mkdir('root_folder')
    except FileExistsError:
        logging.critical(f'root_folder already exists')
        quit()
    except: # 알 수 없는 원인으로
        logging.critical(f'unknown error')
        quit()

    assert os.path.exists('root_folder')
    os.chdir('root_folder')
    make_random_folders(10)
    os.chdir('..')


os.chdir(report_home)
make_random_root_folder()