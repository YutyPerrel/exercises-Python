def print_sterisks (num):
    for i in range (num):
        for _ in range (num - i):
            print(" ", end="")
        for _ in range (1, (i+1)*2):
            print(f'*', end="")
        print()
    return


while True:
    try:
        x = int(input("Enter a number: "))
        print_sterisks(x)
        break
    except ValueError:
        print("Need enter only number, please try again...")
