if __name__ == '__main__':
    pet_1 = {
        'kind': 'turtle',
        'owner': 'jhon',
    }
    pet_2 = {
        'kind': 'dog',
        'owner': 'tim',
    }
    pet_3 = {
        'kind': 'cat',
        'owner': 'anna',
    }
    # pet list
    pets = [pet_1, pet_2, pet_3]
    # print out pets info
    for pet in pets:
        for k, v in pet.items():
            print(f'{k} : {v}')
