"""
사용자에게 숫자와 제곱할 횟수를 입력받아 거듭제곱 결과 출력
"""

def input_number():
    """
    number를 입력받음. float 형변환에서 ValueError를 일으키면 숫자형이 아님
    올바른 number를 입력받을 때 까지 반복
    """
    while True:
        try:
            number = float(input("Enter number: "))
            return number
        except ValueError:
            print("Invalid number input.") #ex) string with letter, two or more dot
            
        else: break # check valid input 
   
def input_exponent():
    """
    exponent를 입력받음. 이때 소수점 아래가 0이라면 정수로 판단
    ex)2.0과 2는 수학적인 계산에서 본질이 같고, 값에 영향을 주지 않음.
    올바른 exponent를 입력받을 때 까지 반복
    """
    while True:
        try:
            exponent = float(input("Enter exponent: "))
            if exponent.is_integer():
                exponent = int(exponent)
                return exponent
            else: raise ValueError
        except ValueError:
            print("Invalid exponent input.") #ex) string with letter
            
        else: break # check valid input 

def calculate(number, exponent):
    """
    number ** exponent 값 return
    int로 표현할 수 있으면 int로 형변환
    """
    if exponent == 0:
        return 1 #exponent 0일 때 예외 처리
    elif exponent < 0:
        return 1/calculate(number, -exponent) #exponent 음수일 때 양수의 역수 계산 후 역수 리턴

    solution = 1.0
    while exponent >= 1:
        if exponent % 2 == 1:
            solution *= number #number**1을 미리 곱함
        
        number *= number #base = number*number
        exponent = exponent//2 #exp = exponent//2, 홀수일 때 (n-1)//2 == n//2
        
    if solution.is_integer(): return int(solution)
    else: return(solution)


def main():
    """
    number 입력받고, exponent 입력받아 거듭제곱 print
    """
    number = input_number()
    exponent = input_exponent()
    print(calculate(number, exponent))
    
if __name__ == "__main__":
    main()
