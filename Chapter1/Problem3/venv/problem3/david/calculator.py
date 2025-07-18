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
        exit()

    
def input_num():
    """
    숫자를 입력받아 return한다. 올바른 숫자를 받을 때 까지 반복한다.
    """
    while True:
        try:
            number = float(input("Enter number: "))
            return number
        except ValueError:
            print("Invalid number input.") #ex) string with letter, two or more dot
            exit()
        else: break # check valid input 

def input_operator():
    """
    연산자를 입력받아 return한다. 약속된 연산자를 받을 때 까지 반복한다.
    """
    while True:
        try:
            command = input("Enter operator: ").strip()
            if command not in operator_list:
                raise 
            return command
        except:
            print("Invalid operator")
            exit()
        else: break

def menu():
    """
    사용자에게 두 가지 모드 중 하나를 선택할 수 있도록 인터페이스를 제공한다.
    """
    print("(0): basic\n(1): expression")
    command = input().strip()
    return command

def check_valid_expr(expression):
    """
    주어진 표현식이 정당한 지 확인한다.
    """
    if len(expression) < 3: #빈 입력
        return False

    numbers = [expression[0], expression[2]]
    operator = expression[1]

    try:
        float(numbers[0])
        float(numbers[1]) #실수가 아님, 형식이 잘못됨
    except:
        return False

    return True 

def cut_expression(expr):
    """
    주어진 표현식에서 처리가 애매한 표현식을 다시 정리한다
    즉 음수의 경우 -와 숫자를 띄어서 입력하는 것을 허용한다.
    """
    for index, data in enumerate(expr):
        if data == '-' and expr[index + 1]:
            expr[index:index+2] = [-float(data)]

    return expr 
    

def calculate(a, b, operator):
    """
    두 수 a, b를 operator에 맞게 계산한다. 이 때 a가 항상 수식의 왼쪽이다.
    """
    if operator == '+':
        return add(a,b)
    elif operator == '-':
        return subtract(a,b)
    elif operator == '*':
        return multiply(a,b)
    elif operator == '/':
        return divide(a,b)
    else:
        print("Invalid operator")
        exit()


def print_sol(command):
    """
    사용자가 선택한 모드에 맞게 계산을 실행하고 결과를 출력한다.
    """
    if command == '0':
        printed = f"Result: {calculate(input_num(), input_num(), input_operator())}"
        print(printed)
    elif command == '1':
        input_expression = input("Enter expression: ").split() #default split(separate, maxsplit)
        input_expression = cut_expression(input_expression)
        if not check_valid_expr(input_expression):
            print("Invalid expression")
            exit()
        printed = f"Result: {calculate(float(input_expression[0]), float(input_expression[2]), input_expression[1])}"
        print(printed)

def main():
    try:
        print_sol(menu())
    except ValueError:
        print("Invalid number input.")
    
if __name__ == "__main__":
    main()
