def check_multiplication_of_numbers(num1, num2, num3):
    if num1 + num2 == num3:
        return f"{num1} + {num2} = {num3}"
    elif num1 +num3 == num2:
        return f"{num1} + {num3} = {num2}"
    elif num2 + num3 == num1:
        return f"{num2} + {num3} = {num1}"

while True:
    try:
        x = int(input("Enter 3 numbers: "))
        y = int(input())
        z = int(input())
        print(check_multiplication_of_numbers(x, y, z))
        break
    except ValueError:
        print("Need enter only numbers, please start from beginning...")
