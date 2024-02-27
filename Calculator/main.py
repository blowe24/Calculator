def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x, y

def main():
    operation = input("which operation?\n(1. Add, 2. Subtract, 3. Multiply, 4. Divide)")
    x = float(input("Enter the first number " ))
    y = float(input('Enter the second number ' ))

    if operation == '1':
        print(x, '+' ,y, '=', add(x, y))
    elif operation == '2':
        print(x, '-' ,y, '=', sub(x, y))
    elif operation == '3':
        print(x, '*' ,y, '=', multiply(x, y))
    elif operation == '1':
        print(x, '/' ,y, '=', divide(x, y))    

main()
