def print_lines():
    print('''
    Hello
    World
    Python    
    ''')

# print_lines()

'hello'.isalpha()    # 모두 알파벳인지?
'hello123'.isalpha() # 숫자가 들어있기 떄문에 False
'hello'.isalnum()    # 알파벳 혹은 숫자인지?

'    '.isspace()     # 공백, 개행 문자 등도 해당. 글자만 찍히지 않으면 True

data = 'Hello'
data.upper()

'Hello world!'.startswith('Hello')
'Hello world!'.endswith('!')

'my name is choi'.split()
'my name isis choi and i am student'.split('is')
        
'hello'.rjust(10)
'hello'.ljust(10)
'hello'.rjust(20, '*')
'hello'.center(20, '=')

d = '       hello     world           '
d.strip()   # 좌우 끝 공백 삭제
d.lstrip()  # 왼쪽 끝 공백 삭제
d.rstrip()  # 오른쪽 끝 공백 삭제

import pyperclip
pyperclip.copy('Hello from Python') # 컴퓨터의 클립보드에 들어감. 다른데에 붙여넣기 가능
pyperclip.paste() # 클립보드에 있는 것을 붙여넣기 가능.



import keyboard

def write_alphabet():
    keyboard.write('abcdeffhjsjpfojsdfghsdlkflwoeiruwe')

keyboard.add_hotkey('shift+windows+w', write_alphabet) # shift windows w 키를 같이 누르면, 함수 실행
keyboard.wait('esc')
keyboard.remove_all_hotkeys()