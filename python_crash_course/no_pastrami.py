if __name__ == '__main__':
    sandwich_orders = ['chicken', 'pastrami', 'black star',
                       'red hot', 'the last hero', 'pastrami',
                       'chicken', 'pastrami']
    finished_sandwiches = []

    print('Unfortunately our restaurant ran out of pastrami.')
    # remove pastrami from orders list
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    # cooking other sandwiches
    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(f'{sandwich} sandwich is ready for you')

    # summing up results
    print('We\'ve already cooked the following sandwiches:')
    for sandwich in finished_sandwiches:
        print(f'\t {sandwich}')
