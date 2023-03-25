if __name__ == '__main__':
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python',
    }

# people who should take part in the poll
poll_candidates = ['jen', 'mike', 'anna', 'eric']

# send msg to people who should take part in the poll
for name in poll_candidates:
    if name in favorite_languages:
        print(f'Thanks for ur participation {name.title()}')
    else:
        print(f'Hi, {name.title()} please take the poll')

