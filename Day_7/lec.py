import re

text = 'hello world'

p = re.compile('hello') # hello라는 단어 패턴 정의
p.search(text)  # 
p.search('HELLO world') # 해당 텍스트가 없으면 None return0

p = re.compile(r'(010-)?(\d\d\d\d)-(\d\d\d\d)')
mo = p.search('my phone number is 010-9700-9998')
p.search('my phone number is 9700-9998')

mo.group() # 매칭된 결과. == 0
mo.group(0) # 전체
mo.group(1) # 첫번째 element
mo.group(2) # 두번째 element

mo.groups() # 매칭된 모든 element를 tuple로 return

p = re.compile(r'Bat(wo)?man') # (  )? --> 없거나 하나 있는 요소에 대한 매칭
p.search('Batman')
p.search('Batwoman')


bat_re = re.compile(r'Bat(wo)*man')
mo1 = bat_re.search('The Adventures of Batman')
mo1.group()

mo2 = bat_re.search('The Adventures of Batwoman')
mo2.group()

mo3 = bat_re.search('The Adventures of Batwowowowowoman')
mo3.group()


bat_re = re.compile(r'Bat(wo)+man')
mo1 = bat_re.search('The Adventures of Batwoman')
mo1.group()

mo2 = bat_re.search('The Adventures of Batwowowowoman')
mo2.group()

text = 'smile hahahaha'
p = re.compile('(ha){4}') # 4개 까지만 matching
p = re.compile('(ha){3,5}?') # 물음표 O : Non-Greedy, 처음 발견된 것만
                             # 물음표 X : Greedy, 발견된 것 모두

p.search('smile hahaha')
p.search('smile hahahaha')
p.search('smile hahahahahahaha')


phone_re = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phone_re.findall('Cell: 415-555-9999 Work: 212-555-0000')
 # ['415-555-9999', '212-555-0000’]

phone_re = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phone_re.findall('Cell: 415-555-9999 Work: 212-555-0000')
 # [('415', '555', '1122'), ('212', '555', '0000')]

p = re.compile(r'성:(.*)이름:(.*)') # (.*) : 모든 문자열에 matching
mo = p.search('성: 최 이름: 수민')
mo.group()
mo = p.search('성:        이름:         ')
mo.group()
mo.groups()
mo = p.search('성:이름:')
mo.group()
mo.groups()
mo.group(1)
mo.group(2)


p = re.compile(r'<.*>') # Greedy : 끝까지 감!
p.search('<최수민> 님 입장하셨습니다.>')

p = re.compile(r'<.*?>') # Non-Greedy : 빨리 나온 것만 매칭
p.search('<최수민> 님 입장하셨습니다.>')

p = re.compile(r'hello', re.I)
p.search('HELLO WORLD').group()
p.search('Hello World').group()

text = '''This
is
multiple
lines
'''

p = re.compile('.*', re.DOTALL)
p.search(text)

text = '제 1회 복권 당첨자는 <최수민>입니다.'
p = re.compile(r'<\D{2,4}>')
p.search(text)
p.sub('***', text)


p = re.compile(r'<(\D)\D{1,3}>') # Group 
p.sub(r'\1**', text) # 첫번째 매칭된 것을 보여줌. 위처럼 Group을 주어야 가능