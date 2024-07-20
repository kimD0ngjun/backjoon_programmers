"""
https://www.acmicpc.net/problem/2295
"""

# 입력 처리
N = int(input())
U = []

for _ in range(N):
    U.append(int(input()))

# print(U)

"""
ex) {2, 3, 5, 10, 18}

x + y + z = k
x + y = k - z

x + y 를 모은 배열 : plus
k - z 를 모은 배열 : minus

plus의 특정 값을 minus가 가지고 있는가?
-> 이진 탐색
"""
# 최적화를 위한 U 솔팅
U.sort()

# plus 배열
plus = []

for x in range(N):
    for y in range(x, N):
        plus.append(U[x] + U[y])

# 이진탐색 전제 정렬
plus.sort()
# print(plus)

# answer 초기화
answer = 0

for z in range(N):
    for k in range(z, N):
        value = U[k] - U[z]

        # 이진 탐색 초기화
        # 인덱스 기반 접근 잊지 말 것
        left = 0
        right = len(plus) - 1

        while left <= right:
            mid = (left + right) // 2

            # 설령 일치하는 값을 찾아도 더 큰 값이 있을 수 있기에
            # 이진 탐색은 찾았다고 끝이 아니라 틈이 없을 때까지 꽉 죄는 알고리즘
            if plus[mid] < value:
                left = mid + 1
            elif plus[mid] > value:
                right = mid - 1
            else:
                answer = max(answer, U[k])
                break

print(answer)