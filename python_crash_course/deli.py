if __name__ == '__main__':
    sandwich_orders = ['chicken', 'black star', 'red hot', 'the last hero', 'chicken']
    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(f'{sandwich} sandwich is ready for you')

    print('We\'ve already cooked the following sandwiches:')
    for sandwich in finished_sandwiches:
        print(f'\t {sandwich}')
