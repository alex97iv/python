if __name__ == '__main__':
    prompt = 'What\'s your age?'
    prompt += '\n "quit" if you want to finish.\n'

    while True:
        age = input(prompt)
        if age == 'quit':
            break
        age = int(age)
        if age <= 3:
            print('It\'s free for you')
        if age < 12:
            print('It\'s 10$ for you')
        if age >= 12:
            print('It\'s 15$ for you')



