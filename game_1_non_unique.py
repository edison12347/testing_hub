
result = []
data = [5,5,5,5,5]

def checkio(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j] and i != j:
                result.append(data[j])
                break
    data = result
    return result

print(checkio(data))

# best solution will be:
# checkio=lambda d:[x for x in d if d.count(x)>1]

# Also nice:
# def checkio(data):
#     return [i for i in data if data.count(i) != 1]

