if __name__ == '__main__':
    my_pizzas = ['pepperoni', 'chicken ranch', 'burger']
    my_friends_pizzas = my_pizzas[:]
    # add my new favourite pizza
    my_pizzas.append('hawai')
    print(f'My favourite pizzas are: {my_pizzas}')
    # add my friend's new favourite pizza
    my_friends_pizzas.append('cheese')
    print(f'My friend\'s favourite pizzas are: {my_friends_pizzas}')

