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

def sort_merge(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        mid_index = len(numbers) // 2
        left = sort_merge(numbers[:mid_index])
        right = sort_merge(numbers[mid_index:])
        return merge(left, right)

def merge(left,right):
    """
    주어진 리스트 2개를 비교하여 정렬하며 병합. 
    """
    result = list()
    left_tail = 0
    right_tail = 0
    
    while (left_tail < len(left) and right_tail < len(right)): #한 쪽 리스트를 다 비울 때 까지 비교하며 병합
        if left[left_tail] <= right[right_tail]:
            result.append(numbers[left_tail])
            left_tail += 1
        else:
            result.append(numbers[right_tail])
            right_tail += 1
    
    while (left_tail <= mid): #왼쪽 다 비우기
        result.append(numbers[left_tail])
        left_tail += 1
    
    while (right_tail <= right): #오른쪽 다 비우기
        result.append(numbers[right_tail])
        right_tail += 1
    
    return result

def main():
    user_input = input_numbers()
    after_sorted = sort_merge(user_input)
    print(after_sorted)
    
if __name__ == "__main__":
    main()
