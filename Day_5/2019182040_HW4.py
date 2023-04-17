from random import randint

# list를 만들어서, 그 안에 하나씩 dict 저장.
# 인원은 20명
# 그 안에 0부터 100까지 과목들 점수를 하나씩 저장. 과목은 KOR ENG MATH로 3개.

# 마지막에 출력할 때 그 점수들을 사용해서 평균 출력

score_lists = []

def SetRandInt():
    result = randint(0, 100)
    return result

def InitScore():
    count = 0
    while(count < 20):
        score = {}
        score.setdefault('KOR', SetRandInt())
        score.setdefault('ENG', SetRandInt())
        score.setdefault('MATH', SetRandInt())
        score_lists.append(score)
        count += 1

def PrintScore():
    count = 1
    for s in score_lists:
        print('%2d' % count, end='')
        print('%11d' % s['KOR'], end='')
        print('%7d' % s['ENG'], end='')
        print('%7d    ' % s['MATH'], end='')
        avg = (s['KOR'] + s['ENG'] + s['MATH']) / 3
        print(round(avg, 2))
        count += 1

def PrintAvg():
    print('AVG', end='')
    avg = 0.0
    for s in score_lists:
        avg += s['KOR']
    avg /= 20
    print('     ', round(avg, 2), end='')

    avg = 0.0
    for s in score_lists:
        avg += s['ENG']
    avg /= 20
    print(' ', round(avg, 2), end='')
    
    avg = 0.0
    for s in score_lists:
        avg += s['MATH']
    avg /= 20
    print(' ', round(avg, 2))
    


print('====================================')
print('Student   KOR    ENG    MATH    AVG ')
print('------------------------------------')
InitScore()
PrintScore()
print('------------------------------------')
PrintAvg()
print('====================================')

