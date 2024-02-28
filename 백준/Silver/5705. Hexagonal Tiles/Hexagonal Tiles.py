import sys


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


# DP 함수
# 메모이제이션 명시
# 두 칸 나아가고 한 칸 나아가고... 결국 k칸 나아갔을 때 가짓수는 늘 두 가지(1칸 / 2칸)
# 얘도 내려가는 거로 생각해보자
def dp(n, memo):
    # n이 0이란 말은 딱 맞춰서 내려왔단 의미니까 경우의 수 추가
    if n == 0:
        return 1
    # n이 0보다 작다면 결국 들어맞지 못하단 의미니까 경우의 수 x
    elif n < 0:
        return 0

    # 메모이제이션 : 이미 저장된 이전 계산값이 있으면 굳이 재귀로 파고들지 않고 바로 리턴
    if n in memo:
        return memo[n]

    # 모든 케이스든 무조건 한 칸, 혹은 두 칸 내려가는 경우로 갈리니까
    # 두 케이스로 재귀호출해서 경우의 수 카운팅
    memo[n] = dp(n - 1, memo) + dp(n - 2, memo)

    return memo[n]


# 입력 처리
results = []

while True:
    count = int(sys_input())
    memo = {}

    if count == 0:
        break

    result = dp(count, memo)
    results.append(result)

for result in results:
    print(result)