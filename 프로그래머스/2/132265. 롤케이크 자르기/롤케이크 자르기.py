"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""


def solution(topping):
    answer = 0

    # 왼쪽과 오른쪽의 고유한 요소를 저장하는 set
    left = set()
    right = set()

    # 메모
    left_memo = [0] * len(topping) # 인덱스 0에서부터
    right_memo = [0] * len(topping) # 인덱스 -1에서부터

    # 왼쪽에서부터 종류 수 세리기
    for i in range(len(topping)):
        
        left.add(topping[i])
        left_memo[i] = len(left)

    # 오른쪽에서부터 역으로 종류 수 세리기
    for i in range(len(topping) - 1, -1, -1):
        
        right.add(topping[i])
        right_memo[i] = len(right)

    # 왼쪽, 오른쪽 나눈 종류 수 비교
    for i in range(len(topping) - 1):
        
        if left_memo[i] == right_memo[i + 1]:
            answer += 1

    return answer
