def checkio(cipher_grille, ciphered_password):
    a = list(map(list, cipher_grille))
    b = list(map(list, ciphered_password))

    row = []
    for k in range(len(a)):
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] == "X":
                    row.append(b[i][j])
        a = list(zip(*a[::-1]))
    return ''.join(row)

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recall_password(
#         ('X...',
#          '..X.',
#          'X..X',
#          '....'),
#         ('itdf',
#          'gdce',
#          'aton',
#          'qrdi')) == 'icantforgetiddqd', 'First example'