def verify_anagrams(*arg):
    """
    Make a comparison for anagrams for any number of words
    :param arg:
    :return:
    """
    args = list(locals().values())
    comparison = []
    for word in args[0]:
        print(type(word))
        print(type(args))
        comparison.append(sorted(word.lower().replace(" ", "")))

    return all(word == comparison[0] for word in comparison)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"