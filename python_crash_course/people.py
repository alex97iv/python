if __name__ == '__main__':
    person_1 = {
        'first_name': 'Aleksey',
        'last_name': 'Navalniy',
        'age': 39,
        'city': 'Moscow',
    }
    person_2 = {
        'first_name': 'Mike',
        'last_name': 'Tyson',
        'age': 23,
        'city': 'New York',
    }
    person_3 = {
        'first_name': 'Adolf',
        'last_name': 'Hitler',
        'age': 33,
        'city': 'Berlin',
    }

    people = [person_1, person_2, person_3]

    # print out info about every person
    for man in people:
        for k, v in man.items():
            print(f'{k} : {v}')
