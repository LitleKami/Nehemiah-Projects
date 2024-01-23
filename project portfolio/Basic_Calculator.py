import time

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
}

def calculator():
    num1 = float(input("Whats the first number?: "))
    for symbols in operations:
        print(symbols)
    continue_operation = True
    while continue_operation == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Whats the next number?: "))

        calculation_function = operations[operation_symbol]
        time.sleep(1)
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        option = (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start anew.: ")).lower()
        if option == 'y':
            num1 = answer
        else:
            should_continue = False
            print("************************************")
            calculator()

calculator()

