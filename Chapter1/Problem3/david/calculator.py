"""
실수형인 두 숫자의 사칙연산 구현
"""

operator_list = ['+', '-', '*', '/']

def add(a, b):
    """
    a+b return
    """
    return a+b

def subtract(a, b):
    """
    a-b return
    """
    return a-b
    
def multiply(a, b):
    """
    a*b return
    """
    return a*b

def divide(a, b):
    """
    a/b return, b!=0
    """
    try:
        sol = a/b
        return sol
    except ZeroDivisionError:
        print("Error: Division by zero")

    
def input_num():
    while True:
        try:
            number = float(input("Enter number: "))
            return number
        except ValueError:
            print("Invalid number input.") #ex) string with letter, two or more dot
            
        else: break # check valid input 

def input_operator():
    while True:
        try:
            command = input("Enter operator: ").strip()
            if command not in operator_list:
                raise 
            return command
        except:
            print("Invalid operator")
        else: break

def menu():
        print("(0): basic\n(1): expression")
        command = input().strip()
        return command

def calculate(a, b, operator):
    if operator == '+':
        return add(a,b)
    elif operator == '-':
        return subtract(a,b)
    elif operator == '*':
        return multiply(a,b)
    elif operator == '/':
        return divide(a,b)

def main():
    if menu() == '0':
        num1 = input_num()
        num2 = input_num()
        operator = input_operator()
        printed = f"Result: {calculate(num1, num2, operator)}"
        print(printed)
    
    
    
if __name__ == "__main__":
    main()
