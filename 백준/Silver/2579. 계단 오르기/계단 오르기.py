def max_score(stairs):
    # 메모이제이션
    memo = {}

    def recursion(n):
        # 끝자락에 안착한 경우는 끝자락 값 추가
        if n == 0:
            return stairs[0]
        # 두 개의 계단이 남은 시점에서 나아갈 방법
        # 연속으로 두 칸 밟는 게 무조건 이득이니 연속으로 밟고 리턴시키기
        elif n == 1:
            return stairs[0] + stairs[1]
        # 세 계의 계단이 남은 시점에서의 나아갈 방법
        # 2, 3 이렇게 밟거나 1, 3 이렇게 밟거나
        elif n == 2:
            return max(stairs[0] + stairs[2], stairs[1] + stairs[2])

        # 이미 해당 계단 스텝의 점수값이 존재하면 메모이제이션에 존재하면 굳이 재귀 접근 x
        if n in memo:
            return memo[n]

        # 현재 계단을 밟는 경우와 밟지 않는 경우 중 큰 값 선택
        step = stairs[n] + max(recursion(n - 2), recursion(n - 3) + stairs[n - 1])
        memo[n] = step
        return step

    return recursion(len(stairs) - 1)

# 입력 단계
count = int(input())
stairs = []

for _ in range(count):
    stairs.append(int(input()))

print(max_score(stairs))
