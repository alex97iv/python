if __name__ == '__main__':
    places = ['New York', 'London', 'Tokyo', 'Berlin', 'Paris']
    print(f'That\'s original list: {places}')
    print(f'That\'s sorted list: {sorted(places)}')
    print(f'That\'s original list again: {places}')
    print(f'That\'s list sorted in reverse alphabetical order: {sorted(places, reverse=True)}')
    places.reverse()
    print(f'That\'s reversed list: {places}')
    places.reverse()
    print(f'That\'s original list again: {places}')
    places.sort()
    print(f'That\'s alphabetically sorted list: {places}')
    places.sort(reverse=True)
    print(f'That\'s reverse-alphabetically sorted list: {places}')

