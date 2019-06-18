def read_until_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            prompt ="Please enter a number"



def read_until_right_action(prompt):
    while True:
            action = str(input(prompt))
            if action == '+' or action == '-' or action == '*' or action == '/' or action == '^':
                return action
            else:
                prompt = "The action you requested is invalid.. please choose from those options: +, -, *, /, ^  "

def calculator(num1, num2, action):
    if action == '+':
        return num1 + num2
    if action == '-':
        return num1 - num2
    if action == '*':
        return num1 * num2
    if action == '/':
        while num2 == 0:
                num2 = read_until_number("Can't divide by zero, please reneter a number")
        return num1 / num2
    if action == '^':
        return num1 ** num2


while True:
        x = read_until_number("Enter 2 numbers: ")
        y = read_until_number("")
        z = read_until_right_action("Enter an action, options: +, -, *, /, ^: ")
        print(calculator(x, y, z))

