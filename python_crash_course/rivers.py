if __name__ == '__main__':
    rivers = {
        'nile': 'egypt',
        'volga': 'russia',
        'senna': 'france',
        'thames': 'great britain',
    }

    # print out info about every river
    for k, v in rivers.items():
        print(f'The {k.title()} runs through {v.title()}.')

    # print names of rivers
    for river in rivers:
        print(river.title())

    # print countries
    for country in rivers.values():
        print(country.title())
