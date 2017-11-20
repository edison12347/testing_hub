def checkio(data):
    return eval(str(data).replace(",", "+"))[0]




print(checkio([1, 2, 3])) # == 6

print(checkio([2, 2, 2, 2, 2, 2])) # == 12

# return eval('\x73um')(data)  # interesting solution