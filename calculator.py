

def add(n1,n2):
    return n1 + n2

def subtruct(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operation={
    "+":add,
    "-":subtruct,
    "*":multiply,
    "/":divide,
}
def calculator():
    
    num1 = float(input("What is the firs num: "))
    for symbol in operation:
        print(symbol)

    should_continue=True

    while should_continue:
        operation_symbol=input("Pick an operation from the line above")
        num2 = float(input("What is the second num: "))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f" Type 'y' to continue calculating with {answer} or type 'no' to start new calculation")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()

