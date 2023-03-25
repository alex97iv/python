if __name__ == '__main__':
    glossary = {
        'if-elif-else': 'allows to control execution flow',
        'for': 'allows to execute same actions many times',
        'array[]': 'allows to keep many values of the same type',
        '+': 'summarize two arguments',
        '-': 'subtracts two arguments'
    }
    for key in glossary.keys():
        print(f'\'{key}\' means:\n {glossary[key]}')
