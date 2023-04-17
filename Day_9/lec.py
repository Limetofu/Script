import shutil

open('hello.jpg', 'w').close()
shutil.copy('hello.jpg', 'new_hello.jpg')       # 파일 하나 복사
shutil.copytree('.', 'new_folder')              # 폴더 전체 복사
shutil.move('new_hello.jpg', 'old_hello.jpg')   # 파일 또는 폴더 이동 (or 이름 변경)
shutil.move('new_folder', 'new_new_folder')
shutil.move('old_hello.jpg', 'new_new_folder')






import os

os.unlink('hello.jpg')          # 파일 삭제, remove도 동일
os.rmdir()                      # 폴더가 비어있어야 삭제 가능
shutil.rmtree('new_new_folder') # 폴더 전체 삭제






import winshell
winshell.delete_file('hello.jpg')

trash = winshell.recycle_bin()

if list(trash):
    for item in trash:
        print(item.real_filename(), item.original_filename())

if list(trash):
    trash.empty()






import zipfile
zf = zipfile.ZipFile('test.zip')    # 압축파일 클래스 return
zf.namelist()                       # 파일을 리스트로
zinfo = zf.getinfo('main.py')
zinfo.file_size      # 정보 확인 가능
zinfo.compress_size
zf.close()  # 꼭 닫아주기

zf.extractall('./outfolder') # outfolder에 모두 압축풀기
zf.extract('main.py')        # 파일 하나만 뽑아내기


# 새로운 압축 파일 만들고 파일 추가
zf = zipfile.ZipFile('new.zip', 'w')
zf.write('main.py', compress_type=zipfile.ZIP_DEFLATED)
zf.close()

# 기존 압축 파일에 추가
zf = zipfile.ZipFile('new.zip', 'a')
zf.write('lec.py')
zf.close()

os.path.getsize('new.zip')
ctime = os.path.getctime('new.zip') # 생성 시각
mtime = os.path.getmtime('new.zip') # 최종 변경 시각    
                                    # 1970 01 01 00시 기준 지난 초를 반환. format 필요

import time
time.ctime(ctime) # 초를 넣으면 반환해줌

import datetime
datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d') # str format time, 년 월 일
datetime.datetime.fromtimestamp(ctime).strftime('%c')     # ctime과 같이
datetime.datetime.fromtimestamp(ctime).strftime('%X')     # 시간만 출력