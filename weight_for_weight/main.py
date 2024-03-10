def order_weight(string: str):
    return ' '.join(sorted([num for num in string.split()], key=lambda num: (sum([int(char) for char in num]), num)))
