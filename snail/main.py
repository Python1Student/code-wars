def snail(snail_map):
    final = []
    new_map = snail_map.copy()

    for num in snail_map[0]:
        final.append(num)
    del new_map[0]

    for num in snail_map[1:-1]:
        final.append(num[-1])
        if new_map:
            del new_map[snail_map.index(num) - 1][-1]

    for num in snail_map[-1][::-1]:
        final.append(num)

    if new_map:
        del new_map[-1]

    for num in snail_map[-2:0:-1]:
        final.append(num[0])

    for num in new_map:
        num.pop(0)

    if new_map:
        for num in snail(new_map):
            final.append(num)

    return final[:len(snail_map) ** 2]


array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
print(snail(array))
