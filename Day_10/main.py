import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2




operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    first_num = float(input("Enter the first number: "))
    continue_operation = True
    while continue_operation:
        operation = input(f"Enter a operation between {', '.join(operations)} : ")
        operation_func = operations[operation]
        second_num = float(input("Enter the second number: "))
        answer = operation_func(first_num, second_num)
        print(f"Answer >> {answer}")
        if input("Do you want to do further calculations with the answer provided? 'y'/'n': ") == "n":
            continue_operation = False
        else:
            first_num = answer
    calculator()

calculator()