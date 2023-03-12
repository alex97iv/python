if __name__ == '__main__':
    guests_names = ['Adolf', 'Marlene Monro', 'Stalin']
    print(f'Unfortunately, {guests_names[0]}, can\'t be with us tonight, so there\'s new list of invitations:')
    guests_names[0] = 'Kutuzov Misha'
    for i in range(len(guests_names)):
        print(f'My dear, {guests_names[i]}, I\'ll be pleased to see at my party tonight!')
