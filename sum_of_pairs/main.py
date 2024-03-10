def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
