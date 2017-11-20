def checkio(data):
    sorted_list = sorted(data)
    middle = int(len(data) / 2)
    if len(data) % 2 == 0:
        return (sorted_list[middle] + sorted_list[middle - 1]) / 2
    else:
        return sorted_list[middle]







# print(checkio([1, 2, 3, 4, 5])) # == 3
# print(checkio([3, 1, 2, 5, 3])) # == 3
# print(checkio([1, 300, 2, 200, 1])) # == 2
print(checkio([3, 6, 20, 99, 10, 15])) # == 12.5