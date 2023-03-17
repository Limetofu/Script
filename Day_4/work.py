def merge(*s):
    result = ''
    for i in range(len(s) - 1):
        result += s[i] + ', '
    result += 'and ' + s[len(s) - 1]
    return result


final = merge('orange', 'apple', 'mango', 'banana', 'peanut')
final
type(final)