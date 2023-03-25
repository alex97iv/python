if __name__ == '__main__':
    favorite_places = {
        'Mike': ['Moscow', 'New York', 'Paris'],
        'Tom': ['Prague', 'Berlin', 'Tomsk'],
        'Ken': ['Rome', 'Larnaka', 'Warsaw'],
    }

    for k, v in favorite_places.items():
        print(f'{k}\'s favorite places are:')
        for place in v:
            print(f'\t{place}')
