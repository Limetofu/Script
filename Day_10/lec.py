# raise Exception
# raise Exception('This is critical error')

# raise ValueError
# raise ValueError('Too Young')

try:
    age = int(input('Enter Age'))
    if age < 18:
        raise ValueError('Too Young Age')
    assert type(age) is int, 'age should be integer'

except Exception as err:
    print(f'{err=}, {type(err)=}')

def print_box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol muse be a single character string.')
    if width <= 2:
        raise Exception('Width muse be greater than 2.')
    if height <= 2:
        raise Exception('Height muse be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ('  ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        print_box(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))


### test ###
import traceback

def bacon():
    try:
        raise Exception('My Error')
    except:
        with open('error_story.txt', 'a') as ef:
            for line in traceback.format_stack():
                ef.write(line)

def spam():
    bacon()

def ham():
    spam()

ham()



import logging

logging.basicConfig(
    filename='mylog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.disable(logging.CRITICAL)
a = 10

logging.debug('this is debug')
logging.info('this is simple info')
logging.warning(f'value {a=} is a warning')
logging.error('Error')
logging.critical('Critical error')