num = ['0123456789ABCDEF']

black_pink = ['jisu', 'jeni', 'rose', 'risa']
black_pink[0] = 'daehyun'
black_pink.append('JYP')
black_pink += ['YG']
black_pink.remove('JYP')
del black_pink[0]
black_pink.insert(2, 'IU')

for member in black_pink:
    print(member)

for i, member in enumerate(black_pink):
    print('%d th member is %s' % (i, black_pink[i]))

'YG' not in black_pink


spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)

data = ['A', 'B', 'C', 'D']
new_data = data
new_data is data
new_data == data
id(new_data) == id(data)


t1 = (3, 2, 3)
type(t1)
t2 = (100,)
type(t2)
t3 = (100)
type(t3)
t4 = ()
type(t4)
t5 = (2,3,4,5)
t6 = (5,6,7,8)

def add(*values):
    return sum(values)

add(1, 2, 3)
