def is_valid_walk(walk):
    person_position = [0, 0]

    if len(walk) != 10:
        return False

    for side in walk:
        if side == 'n':
            person_position[0] += 1
        elif side == 's':
            person_position[0] -= 1
        elif side == 'e':
            person_position[1] += 1
        elif side == 'w':
            person_position[1] -= 1

    if person_position == [0, 0]:
        return True
    else:
        return False


# def is_valid_walk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



