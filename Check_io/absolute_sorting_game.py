def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

print(checkio((-20, -5, 10, 15)))

# def checkio(tuple):
#     return sorted(list(map(abs, tuple)))