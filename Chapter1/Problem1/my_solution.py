""" 
hello() 함수를 실행하여 Hello를 출력하는 파일
"""

import sys

def hello():
    """
    Hello 문자열을 반환
    """
    return "Hello"

if __name__ == "__main__":
    print(hello(), sep = ' ', end='') #print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
