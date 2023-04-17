import os

file_info = {}

for root, subfolders, files in os.walk('E:/Python'):
    for fn in files: # 각각의 파일 이름을 가지고 와서,
        abs_path = root + '\\' + fn
        file_info[abs_path] = os.path.getsize(abs_path) # 파일 이름과 사이즈를 연결

sorted_info = sorted(file_info.items(), key=lambda x: x[1], reverse=True)
print(sorted_info)

with open('report.txt', 'w') as f:
    for info in sorted_info:
        f.writelines(f'{info[1]:12} {info[0]} \n')