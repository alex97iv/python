if __name__ == '__main__':
    current_users = ['Mike', 'Kate', 'Kevin', 'Freddy']
    low_current_users = [user.lower() for user in current_users]
    new_users = ['Alex', 'KATE', 'KeViN']

    for name in new_users:
        if name.lower() in low_current_users:
            print(f'Name {name} is not available, please choose another one')
        else:
            print(f'Name {name} is available!')


