"""
https://www.acmicpc.net/problem/2666
"""

# 입력 처리
N = int(input())
open_a, open_b = map(int, input().split())

M = int(input())
targets = [int(input()) for _ in range(M)]

# print(doors)

"""
해당 문제가 그리디가 안 되는 이유

3번과 5번 문이 열려있고 다음 사용 벽장이 4번이면
(1) 닫힌 4번 문을 3번으로 옮긴다 -> 4, 5번이 열림
(2) 닫힌 4번 문을 5번으로 옮긴다 -> 3, 4번이 열림
두 가지가 되는데 둘 다 해당 분기에서 동등한 최적의 선택이 됨
근데 그 다음에 6번 벽장을 사용해야 한다면 전체적으로는 (1) 선택이 최적이 됨

그리디로는 위의 예시 상황을 커버할 수 없음

---

문 : 1 ~ N번까지(인덱스 == 문 번호)
현재 열어야 할 대상 벽장, 현재 열려있는 문 2개 -> 그때 시점에서의 이동 횟수
분기당 이동 횟수 == min(abs(현재 열어야 할 대상 벽장 - 현재 열린 문 중 하나), abs(현재 열어야 할 대상 벽장 - 현재 열린 문 중 다른 하나))

근데 이것만 쓰면 그리디고, 그리디로는 안되기 때문에 dp 활용
dp[현재 열어야 할 대상 벽장][현재 열려있는 문 a][현재 열려있는 문 b] == 이제까지 그 대상 문까지 이동한 총 최소 이동횟수 

분기당 '총' 이동 횟수 = min(
    abs(현재 열어야 할 대상 벽장 - 현재 열린 문 중 하나) + 재귀함수(문이 움직이기 시작하는 위치), 
    abs(현재 열어야 할 대상 벽장 - 현재 열린 다른 문) + 재귀함수(문이 움직이기 시작하는 위치)
)
"""

# dp 테이블(1~ N번 문)
# 가장 밖의 배열은 열어야 할 벽장들
dp = [[[None for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(M + 1)]


# 재귀함수(case 순서, 열린 문 a, 열린 문 b)
def recursion(i, open_a, open_b):

    # 탈출조건부터 합산 시작
    if i == M:
        return 0

    # 각 순서에 해당하는 열어야 할 대상 벽장
    target = targets[i]

    # 메모이제이션
    if dp[i][open_a][open_b] is not None:
        return dp[i][open_a][open_b]

    # 절댓값 의미 : ex) 현재 open_a까지 갈 예정(즉 지금 시점 열려있는 건 target과 open_b)
    dp[i][open_a][open_b] = min(
        abs(target - open_a) + recursion(i + 1, target, open_b),
        abs(target - open_b) + recursion(i + 1, open_a, target)
    )

    return dp[i][open_a][open_b]


print(recursion(0, open_a, open_b))