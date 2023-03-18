if __name__ == '__main__':
    numbers = list(range(1, 22))
    print(f'Three first nums: {numbers[:3]}')
    mid = round(len(numbers) / 2)
    print(f'Three nums in the middle: {numbers[mid - 1:mid + 2]}')
    print(f'Three last nums: {numbers[-3:]}')

