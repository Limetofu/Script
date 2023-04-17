import os

os.chdir('e:/3_1/Script/Day_8')

report_file = open('report.txt', 'w')

# 딕셔너리 하나 만들어서
# 모든 파일에 대해서

def getfile(dir):
    fileinfo = {}
    for root, subfolders, files in os.walk(dir):
        for filename in files:
            # file_loc_size.setdefault(os.path.getsize(root), filename)
            filepath = os.path.join(root, filename)
            filesize = os.path.getsize(filepath)
            fileinfo[filename] = filesize
    return fileinfo

fileInfo = getfile('e:/Python')

for result in sorted(fileInfo.items(), key=lambda x: x[1], reverse=True):
    report_file.write(f'{result[1]}'.ljust(12))
    report_file.write(result[0])
    report_file.write('\n')