if __name__ == '__main__':
    prompt = 'Please enter desirable pizza topping.'
    prompt += '\n Write "quit" if you want to finish.\n'

    toppings = []
    while True:
        ans = input(prompt)
        if ans == 'quit':
            break
        else:
            toppings.append(ans)

    print('U\'ve ordered the following toppings:')
    for topping in toppings:
        print(f'\t{topping}')
