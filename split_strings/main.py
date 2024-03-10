def solution(s: str):
    i = 0
    my_list = []
    while i < len(s):
        if i + 1 < len(s):
            my_list.append(s[i] + s[i + 1])
            i += 2
        else:
            my_list.append(s[i] + '_')
            break

    return my_list

