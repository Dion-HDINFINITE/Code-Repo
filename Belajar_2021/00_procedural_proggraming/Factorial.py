def main():
    num = int(input("Enter you number here to factorial it : "))
    print(factorial(num))


def factorial(number):
    if number < 0:
        return
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


main()