def checkio(expression):
    # differentiate between brackets
    open_bracket = ['(', '{', '[']
    close_bracket = [')', '}', ']']

    # filter brackets only
    filtered = list(filter(lambda x: x in open_bracket + close_bracket, expression))

    # Start deleting bracket pairs until it is empty
    for j in range(len(filtered)):
        for i in range(len(filtered)):
            try:
                if open_bracket.index(filtered[i]) == close_bracket.index(filtered[i+1]):
                    del filtered[i:i+2]
            except (IndexError, ValueError):
                continue

    return len(filtered) == 0

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"



