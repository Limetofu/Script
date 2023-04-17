# print('hello', end=' ')  # end의 basic값은 개행문자.  
# print('world')

# print('cats', 'dogs', 'mice', sep=':')  # seperate argument 인자 사이에 넣을 수 있음


######################################################################################3333
# Global / Local Scope

# def spam():
#     print(eggs)
#     # eggs = 'spam local' # error

# eggs = 'global'
# spam()

def spam(divideBy):
    try: # 실행하고자 하는 문장
        return 42/divideBy 
    except ZeroDivisionError: # zero division이 발생했을 떄
        print('Error: Invalid argument.')

print(spam(0))

import random

ages = [random.randint(1, 100) for n in range(20)]

if any(i < 18 for i in ages):
    print('미성년자 있음.')
else:
    print('모두 다 성인임')

print('모두 다 성인임.') if all(i >= 18 for i in ages) else print('미성년자 있음.')


# numbers = [random.randint(1, 99) for n in range(20)]

# def mul3_filter(n):
#     return n % 3 == 0
# result = list(filter(mul3_filter, numbers))

# result = list(filter(lambda n: n % 3 == 0, numbers))

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
squares_list = list(squares)

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, numbers)))

names = ["ALice", "Bob", "Charlie"]
ages = [25, 30, 35]
heights = [180.5, 172.1, 185.3]
zipped = zip(names, ages, heights) # 배열 요소들을 차례로 결합
print(list(zipped))
print(list(zipped)) # 한 번 사용하면 소진