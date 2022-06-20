
#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#multiply
def multiply(n1, n2):
    return n1 * n2


#divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(''' 
              _______________________
              |  _________________  |
              | | JO           0. | |
              | |_________________| |
              |  ___ ___ ___   ___  |
              | | 7 | 8 | 9 | | + | |
              | |___|___|___| |___| |
              | | 4 | 5 | 6 | | - | |
              | |___|___|___| |___| |
              | | 1 | 2 | 3 | | x | |
              | |___|___|___| |___| |
              | | . | 0 | = | | / | |
              | |___|___|___| |___| |
              |_____________________|''')
    num1 = float(input("Enter first number :\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:

        operation_symbol = input("pick an symbol for operation\n")
        num2 = float(input("Enter next number: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"press 'y' to continue calculating with {answer}, or type 'n' to start new calculator\n"
        ) == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
