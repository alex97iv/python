if __name__ == '__main__':
    guests_num = int(input('How many people in your dinner group?\n'))
    if guests_num < 8:
        print('Your table is ready')
    else:
        print('Unfortunately, you have to wait')
