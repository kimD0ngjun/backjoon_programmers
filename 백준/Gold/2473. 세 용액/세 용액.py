"""
https://www.acmicpc.net/problem/2473
"""
import sys

# 입력
N = int(input())
solution = list(map(int, input().split()))

"""
얘도 이진탐색 같은데
용액1 + 용액2 + 용액3 -> 가장 0에 가까운(즉, 절댓값이 최솟값인)

그럼 똑같이 용액1 + 용액2 리스트를 먼저 계산해두고
정렬 후, 용액3을 순회하면서 정렬 계산 리스트 기준으로 이진탐색하기
"""

# # 두 개만 더해서 정렬
# plus = []
# # 정답 출력을 위한 메모
# memo = {}

"""
이 부분이 메모리 초과가 발생하는듯?
"""
# for i in range(N):
#     for j in range(i + 1, N):
#         plus.append(solution[i] + solution[j])
#         memo[solution[i] + solution[j]] = (solution[i], solution[j])
#
# plus.sort()

"""
left랑 right가 좀 붕 뜨는 느낌이 들기도
기존의 이진탐색은 left와 right를 기준으로 mid를 찾아감
지금의 이진탐색은 mid를 기준으로 left와 right를 찾아가기?

정답 => 0에 가깝기
i => 임의의 특정 용액
left, right => 이진 탐색으로 찾으려는 용액
"""
# 결과 초기화 후, 이진탐색
solution.sort()

standard = sys.maxsize
zero = False
a = 0
b = 0
c = 0

for i in range(N - 2):
    # 이진탐색 변용 투 포인터 인덱스 초기화
    left = i + 1
    right = N - 1

    while left < right:

        # 용액 전부 더한 값
        value = solution[left] + solution[right] + solution[i]

        # 표준값 업데이트하면서 0에 가장 가까운 값 산출
        if abs(value) <= standard:
            a = solution[left]
            b = solution[right]
            c = solution[i]

            standard = abs(value)

        # 인덱스 옮기기
        # 기준: value가 0보다 작으면 left(중간값)을 옮기고, 0보다 크면 right(끝값)을 옮겨서 0에 가까워지게
        if value < 0:
            left += 1
        elif value > 0:
            right -= 1
        # 0이면 걍 아무 값이나 출력하랬으니 반복문 파괴해서 최적화
        else:
            zero = True
            break

    if zero:
        break

# print(standard)
result = [a, b, c]
result.sort()

print(' '.join(map(str, result)))