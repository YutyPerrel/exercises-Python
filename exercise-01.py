def check_evenr_or_odd(num):
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"


while True:
    try:
        x = int(input("Enter number: "))
        print(check_evenr_or_odd(x))
        break
    except ValueError:
        pass
