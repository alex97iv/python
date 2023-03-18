if __name__ == '__main__':
    ord_nums = list(range(1, 10))
    for n in ord_nums:
        if n == 1:
            suf = 'st'
        elif n == 2:
            suf = 'nd'
        elif n == 3:
            suf = 'rd'
        elif (n > 3) and (n < 10):
            suf = 'th'
        print(str(n) + suf)

