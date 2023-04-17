from collections import defaultdict

student = {'name':'tom', 'grade':'a+'}  # 초기화
student['name']                         # key를 통해 value찾기 가능
student['height'] = 178.5               # dict에 key value를 넣는 방법
student['height']

student.keys()      # dict의 key들만 리스트로 제공
student.values()    # dict의 value들만 리스트로 제공
student.items()     # dict의 모든 key, value 쌍들을 [(), ()]으로 제공

student.get('address') # key가 있으면 value 출력, 없으면 출력 x (key가 없는 에러 방지)
student.setdefault('color', 'black')
student



# 글자 수 세기

text = 'It was a bright cold day in April, and the olocks were striking thirteen'
# count = {} # 빈 dict를 만드는 방법
count = defaultdict(lambda: 0)
for c in text:
    # count.setdefault(c, 0) # defaultdict를 사용하면 필요없어짐
    count[c] = count[c] + 1

print(count)



# set - 중복 비허용, 순서 상관x (집합이라고 생각)

s1 = {1, 2, 3}
type(s1)
s1 = {1, 2, 2, 4}
s1
l1 = [1,2,2,2,2,3,3,3,3,5,5,5,5,5]
s1 = set(l1) # 중복허용 x
s1
s2 = {3,5,6,7}
s1 + s2 # 합하는 건 안됨! 중복이 안되기 때문
s1 | s2 # 합집합은 가능
s1 & s2 # 교집합
s1 - s2
s1.add(8)
s2.remove(6)
s2

