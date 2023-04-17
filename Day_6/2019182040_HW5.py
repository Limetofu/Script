import pyperclip
import keyboard
import collections

# str을 나눠야 함. 특수문자, 숫자 모두 뺴버려야 함.
# how? =>> 빈 문자열 하나 만들고, input 한글자마다 알파벳인지 검사해서 넣기.

def make_split_list(input):
    output = ''
    for c in input:
        if c.isalpha():
            output += c
        else:
            output += ' ' # 일단 공백 넣기. 나중에 split 써주기.
    output = output.split()
    return output

# 단어 수를 세고자 함...
# 1. 정렬 해야 함.
# 2. collections의 Counter 함수 사용!
# 3. Counter --> dict return

# 키 입력은 keyboard 이용.
# shift windows w 동시에 3개 클릭 시 단어별로 카운트된 횟수 출력
# 단어들은 대문자 우선, 알파벳 순서대로 출력

def print_word_count():
    global output
    word_count = collections.Counter(output)
    print('========= Word Count =========') # 정렬된 문자 카운트 출력
    for word in sorted(word_count.keys()):
        print(f'{word.ljust(28)} {word_count[word]}')
    print('==============================')

# copy한 데이터를 가져와야 함.
# --> paste() 이용.

input = pyperclip.paste()
output = make_split_list(input)
keyboard.add_hotkey('shift+windows+w', print_word_count)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()