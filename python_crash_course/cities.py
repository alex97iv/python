if __name__ == '__main__':
    cities = {
        'Moscow': {'country': 'Russia',
                   'population': 15_000_000,
                   'fact': 'The biggest city in the country'},
        'Berlin': {'country': 'Germany',
                   'population': 6_000_000,
                   'fact': 'was divided into 2 parts before 1965'},
        'New York': {'country': 'USA',
                     'population': 20_000_000,
                     'fact': 'big apple city'},
    }
    for city, info in cities.items():
        print(city)
        for k, v in info.items():
            print(f'\t{k}: {v}')

