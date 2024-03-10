def find_missing_letter(chars):
    return [chr(ord(char) + 1) for index, char in enumerate(chars) if index + 1 != len(chars) and ord(char) + 1 != ord(chars[index + 1])][0]
