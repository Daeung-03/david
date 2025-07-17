"""
수식을 입력 받아 우선순위를 고려한 사칙연산 계산
"""

operator_list = ['+', '-', '*', '/', '(', ')']

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


def stris_float(string):
    """
    넘겨받은 인자가 float로 바꿀 수 있는 string인지 확인한다.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False

def check_valid(list):
    """
    입력받은 expression이 타당한지 확인
    """
    for data in list:
        if not stris_float(data) and data not in operator_list: #숫자도 아니고 오퍼레이터도 아니면 error
            print("Invalid input.")
            exit()

def expression_cut(expression):
    """
    리스트로 구성된 expression을 숫자와 연산자로 구분하여 리스트 반환
    """
    numbers = [float(x) for x in expression if stris_float(x)]
    operators = [x for x in expression if x in operator_list]
    return numbers, operators

def find_paren_first(expression):
    """
    가장 먼저 처리해야 할 괄호를 찾아 인덱스 반환
    """
    
    index_start = -1
    index_end = -1
    for index in range(len(expression)):
        if expression[index] == '(':
            index_start = index
        elif expression[index] == ')':
            index_end = index
            return index_start, index_end
    return index_start, index_end
    
def calculate_priority(numbers_div, operators_div):
    """
    제공받은 숫자들을 (+, -, *, /)의 우선순위에 맞게 연산
    """
    index_1th = 0
    index_2th = 0

    while '*' in operators_div or '/' in operators_div: #곱셉, 나눗셈 찾아 연산
        if operators_div[index_1th] == '*' or operators_div[index_1th] == '/':
            temp = calculate(numbers_div[index_1th], numbers_div[index_1th+1], operators_div[index_1th])
            numbers_div[index_1th] = temp
            numbers_div.pop(index_1th+1)
            operators_div.pop(index_1th)
            index_1th -= 1
        
        index_1th += 1
                           
    while '+' in operators_div or '-' in operators_div: #더하기, 빼기 찾아 연산
        if operators_div[index_2th] == '+' or operators_div[index_2th] == '-':
            temp = calculate(numbers_div[index_2th], numbers_div[index_2th+1], operators_div[index_2th])
            numbers_div[index_2th] = temp
            numbers_div.pop(index_2th+1)
            operators_div.pop(index_2th)
            index_2th -= 1

        index_2th += 1
    
    return numbers_div

def div_for_paren(expression):
    """
    괄호가 있는 표현식(리스트)을 없어질 때까지 계산 후 표현식 수정, 이를 재귀적으로 반복 후 리턴
    """
    while '(' in expression: #계속해서 표현식을 수정하며 재귀적으로 반복
        index_start, index_end = find_paren_first(expression) #닫는 괄호를 만나면 맨 앞의 괄호까지의 숫자와 연산자 계산함
        if index_start == -1: break

        sub_expression = expression[index_start + 1:index_end]

        sub_numbers, sub_operators = expression_cut(sub_expression)

        temp = calculate_priority(sub_numbers, sub_operators)

        expression = expression[:index_start] + temp + expression[index_end + 1:] #표현식 수정하고 다시 반복
    return expression

def solve_expr(expression):
    """
    괄호를 제거한 표현식 계산 후 결과값 리턴
    """
    numbers, operators = expression_cut(expression)
    result = calculate_priority(numbers, operators)

    return result[0]

def main():
    """
    표현식 입력받고, 잘못된 입력인지 검증. 이후 괄호로 구성된 식을 계산하여 치환한 후, 남아있는 수와 연산자 처리
    """
    expression = input().split()
    check_valid(expression)

    remove_paren = div_for_paren(expression)
    solution = solve_expr(remove_paren)
    print(solution)

    
if __name__ == "__main__":
    main()