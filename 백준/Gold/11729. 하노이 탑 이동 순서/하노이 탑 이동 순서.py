"""
https://www.acmicpc.net/problem/11729
"""

# 입력 처리
K = int(input())

"""
K -> 3
K-1 -> 2
K-2 -> 3
K-3 -> 2

...
"""

# count = 0

def recursion(n, pop, pull):
    # # 카운팅
    # global count
    # count += 1

    # 탈출
    if n == 1:
        print(pop, pull)
        return

    # `n번 이전의 번호들 원판`을 n번이 옮겨질 곳과 다른 곳으로 옮기기
    recursion(n - 1, pop, 6 - pop - pull)

    # n번 원판을 옮길 곳으로 옮기기
    print(pop, pull)

    # 옮겨진 n번 원판 위로 `n번 이전의 번호들 원판` 옮기기
    recursion(n - 1, 6 - pop - pull, pull)


# 연산 및 출력
print(2**K - 1)
# 마지막 번호 원판은 3번에 위치시켜야 하므로
recursion(K,1, 3)