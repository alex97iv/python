if __name__ == '__main__':
    guests_names = ['Adolf', 'Marlene Monro', 'Stalin']
    # Adolf died, plan has changed
    print(f'Unfortunately, {guests_names[0]}, can\'t be with us tonight, so there\'s new list of invitations:')
    # Found a new guest
    guests_names[0] = 'Kutuzov Misha'
    for i in range(len(guests_names)):
        print(f'My dear, {guests_names[i]}, I\'ll be pleased to see at my party tonight!')
    # Found one more table
    print('Hey, I\' found one more table!\n'
          'So there\'s my new invitation list:')
    # Add new guests to the list
    guests_names.insert(0, 'Donald Trump')
    guests_names.insert(round(len(guests_names) / 2), 'Joe Byden')
    guests_names.append('Vova Putin')
    # Printing new invitation list
    for i in range(len(guests_names)):
        print(f'My dear, {guests_names[i]}, I\'ll be pleased to see at my party tonight!')
    # Sad news come
    print('Oh no! I won\'t get my new dinner table in time! I can invite only two guests!')

    for i in range(2, len(guests_names)):
        print(f'I\'m so sorry my dear, {guests_names.pop()}, don\'t have a place for you tonight. May be next time...')

    for i in range(len(guests_names)):
        print(f'My dear, {guests_names[i]}, I\'ll be pleased to see you at my party tonight!')
