def front_back(str):
    str = list(str)

    str[0], str[len(str) - 1] = str[len(str) - 1], str[0]

    return ''.join(str)

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print(front_back(''))