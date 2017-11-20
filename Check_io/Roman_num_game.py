regular = (1000, 500, 100, 50, 10, 5, 1)
reg_roman = ('M', 'D', 'C', 'L', 'X', 'V', 'I')

data = 44

roman_num = ''
C = regular[2] # 100 = C
X = regular[4]
I = regular[6]
spec = (C, X, I)
for i in range(len(regular)):
    # General case
    multiplier, data = divmod(data, regular[i])
    roman_num = roman_num + multiplier * reg_roman[i]
    # Special  case
    if 1000 > data >= 400 and data >= (regular[i] - C):
        data = data - regular[i] + C
        roman_num = roman_num + 'C' + reg_roman[i]
    elif 100 > data >= 40 and data >= (regular[i] - X):
        data = data - regular[i] + X
        roman_num = roman_num + 'X' + reg_roman[i]
    elif 10 > data >= 4 and data >= (regular[i] - I):
        data = data - regular[i] + I
        roman_num = roman_num + 'I' + reg_roman[i]
print(roman_num)
