if __name__ == '__main__':
    active = True
    poll_results = {}
    while active:
        user_name = input('What\'s your name\n')
        ans = input(f'{user_name} if you could visit one place '
                    'in the world where would you go?\n')
        poll_results[user_name] = ans
        ans = input('Would you like to ask one more user? (yes/no)\n')
        if ans == 'no':
            print('Congrats! Polling is over')
            active = False

    # print out poll's results
    for user_name, place in poll_results.items():
        print(f'{user_name.title()} would go to {place.title()}')

