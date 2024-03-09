import re


def to_camel_case(text):
    my_list = re.split(r'[-_]', text)
    final = ''
    for word in my_list:
        if my_list[0].istitle() and word == my_list[0]:
            final += word.title()
        elif not my_list[0].istitle() and word == my_list[0]:
            final += word.lower()
        else:
            final += word.title()

    return final


print(to_camel_case('The-Cat_was-evil'))