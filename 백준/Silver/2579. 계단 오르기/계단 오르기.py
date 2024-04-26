def max_score(stairs):
    # 메모이제이션
    memo = {}

    def recursion(n):
        # 끝자락에 안착한 경우는 끝자락 값 추가
        if n == 0:
            return stairs[0]
        # 한 칸 나아간 케이스의 최대갑 비교
        elif n == 1:
            return max(stairs[0], stairs[0] + stairs[1])
        # 두 칸 나아간 케이스의 최대값 비교
        elif n == 2:
            return max(stairs[0] + stairs[2], stairs[1] + stairs[2])

        # 이미 해당 계단 스텝이 메모이제이션에 존재하면 굳이 재귀 접근 x
        if n in memo:
            return memo[n]

        # 현재 계단을 밟는 경우와 밟지 않는 경우 중 큰 값 선택
        step_one = stairs[n] + max(recursion(n - 2), recursion(n - 3) + stairs[n - 1])
        memo[n] = step_one
        return step_one

    return recursion(len(stairs) - 1)

# 입력 단계
count = int(input())
stairs = []

for _ in range(count):
    stairs.append(int(input()))

print(max_score(stairs))
