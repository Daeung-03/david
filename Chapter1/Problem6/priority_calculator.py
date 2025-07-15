"""
수식을 입력 받아 우선순위를 고려한 사칙연산 계산
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
    ㅉ
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
            print("Invalid number input.")
            exit()

def main():
    expression = input().split()
    check_valid(expression)
    numbers = [float(x) for x in expression if stris_float(x)]
    operators = [x for x in expression if x in operator_list] #숫자와 문자열 나누어 저장
    index_1th = 0 #곱하기, 나누기 할 숫자 인덱스
    index_2nd = 0 #더하기, 빼기 할 숫자 인덱스
    
    for i in operators: #곱셉, 나눗셈 찾아 연산
        if i == '*' or i == '/':
            temp = calculate(numbers[index_1th], numbers[index_1th+1], i)
            numbers.pop(index_1th)
            numbers.pop(index_1th)
            numbers.insert(index_1th, temp)
        else: index_1th += 1
            
                
    for j in operators: #더하기, 빼기 찾아 연산
        if j == '+' or j == '-':
            temp = calculate(numbers[index_2nd], numbers[index_2nd+1], j)
            numbers.pop(index_2nd)
            numbers.pop(index_2nd)
            numbers.insert(index_2nd, temp)
        else: index_2nd += 1
    
    print(numbers[0]) #최종적으로 남은 결과값 출력
    
if __name__ == "__main__":
    main()