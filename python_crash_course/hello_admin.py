if __name__ == '__main__':
    users = ['Karen', 'Henry', 'Angela', 'Jim', 'Admin']
    # greetings to each user
    if users:
        for user in users:
            if user == 'Admin':
                print('Admin is online, would you like to see the last report?')
            else:
                print(f'Hi, {user}! It\'s nice to see you\'re back')
    else:
        print('We definitely need to find some users!')
