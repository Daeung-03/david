"""
사용자에게 공백으로 구분된 숫자를 받아 오름차순으로 정렬하고, 출력
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

def sort_buble(numbers):
    """
    버블 정렬 실행
    """
    for determined in range(len(numbers)-1, 0, -1): #determined는 자리가 결정된(여기 인덱스의 숫자는 위치가 고정) data를 의미
        for index_com in range(determined): #비교를 하기 위한 index = index_com
            if numbers[index_com] > numbers[index_com + 1]:
                numbers[index_com], numbers[index_com + 1] = numbers[index_com + 1], numbers[index_com]

def main():
    user_input = input_numbers()
    sort_buble(user_input)
    printed = str(user_input)[1:-1]
    print(printed)
    
if __name__ == "__main__":
    main()
