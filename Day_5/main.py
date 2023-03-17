def merge(*values):
    # result = ''
    result = ', '.join(values[:-1])
    # for s in values[:-1]:
    #     result += s + ', '

    result += (' and ' if result else '') + values[-1]
    return result

merge('orange', 'mango', 'berry')