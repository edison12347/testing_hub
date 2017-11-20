def checkio(string, number):
    try:
        result = int(string, number)
    except ValueError:
        quit()
    return result

# if __name__ == "__checkio__":
print(checkio("AF", 16))
