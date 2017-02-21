# checkio(15) == "Fizz Buzz"
# checkio(6) == "Fizz"
# checkio(5) == "Buzz"
# checkio(7) == "7"

a = int(input("?"))
def checkio(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return "Fizz Buzz"
        else:
            return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

print(checkio(a))