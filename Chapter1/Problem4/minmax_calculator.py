"""
숫자들을 입력받아 최대값, 최소값을 출력하는 프로그램
"""

def input_numbers():
    """
    숫자들을 입력받아 리스트에 저장 후 리턴. 공백을 기준으로 숫자 구분.
    숫자가 아닌 입력을 받으면 프로그램 종료함.
    """
    try:
        list_numbers = list(map(float, input().split())) #default map(function, iterable)
        if len(list_numbers) < 1: raise ValueError
        return list_numbers
    except ValueError:
        print("Invalid input.")
        exit()

def Cal_min(numbers):
    """
    숫자가 들어있는 리스트를 입력받아 최소값 리턴
    """
    sol = numbers[0]
    for data in numbers:
        if sol > data:
            sol = data
    
    return sol

def Cal_max(numbers):
    """
    숫자가 들어있는 리스트를 입력받아 최대값 리턴
    """
    sol = numbers[0]
    for data in numbers:
        if sol < data:
            sol = data
    
    return sol    

def main():
    numbers_user = input_numbers()
    printed = f"Min: {Cal_min(numbers_user)}, Max: {Cal_max(numbers_user)}"
    print(printed)

if __name__ == '__main__':
    main()
