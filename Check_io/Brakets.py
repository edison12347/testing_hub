def checkio(expression):
    # differentiate between brackets
    open_bracket = ['(', '{', '[']
    close_bracket = [')', '}', ']']

    # filter brackets only
    filtered = list(filter(lambda x: x in open_bracket + close_bracket, expression))
    print(filtered)
    # compare open bracket with corresponding closed one
    for i, j in zip(range(len(filtered)), reversed(range(len(filtered)))):
        try:
            if open_bracket.index(filtered[i]) != close_bracket.index(filtered[j]):
                try:
                    if open_bracket.index(filtered[i]) != close_bracket.index(filtered[i+1]):
                        return False
                except ValueError:
                    return False
        except ValueError:
            continue
    return True

# if __name__ == '__main__':
#     assert checkio("((5+3)*2+1)") == True, "Simple"
#     assert checkio("{[(3+1)+2]+}") == True, "Different types"
#     assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
#     assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#     assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#     assert checkio("2+3") == True, "No brackets, no problem"

# print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))
#
# print(checkio("((5+3)*2+1)"))
print(checkio("[(3)+(-1)]*{3}"))
# print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))