# a, b, c의 값을 3중 리스트로 저장시키는 메모이제이션
memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def recursion(a, b, c):
    # 첫 번째 조건
    if a <= 0 or b<= 0 or c<=0:
        return 1

    # 두 번째 조건
    if a > 20 or b > 20 or c > 20:
        return recursion(20, 20, 20)

    # 메모이제이션 활용
    if memo[a][b][c]:
        return memo[a][b][c]

    # 그게 아니라면 그냥 계산 시이작...(재귀 호출)
    if a < b < c:
        memo[a][b][c] = recursion(a, b, c - 1) + recursion(a, b - 1, c - 1) - recursion(a, b - 1, c)
        return memo[a][b][c]

    # 4번 식에서 리턴된 값을 다시 윗단계의 함수 복귀 과정에서 메모이제이션 저장
    # 재귀함수는 다시 착착착 올라가는 과정에서 밑에 있는 남은 로직들을 전부 실행하고 착착착 올라감
    # 그 과정에서 메모이제이션 저장 과정을 거치게 하기
    memo[a][b][c] = recursion(a - 1, b, c) + recursion(a - 1, b - 1, c) + recursion(a - 1, b, c - 1) - recursion(a - 1, b - 1, c - 1)
    return memo[a][b][c]


# 입력 단계
while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
       
    print(f'w({a}, {b}, {c}) = {recursion(a,b,c)}')