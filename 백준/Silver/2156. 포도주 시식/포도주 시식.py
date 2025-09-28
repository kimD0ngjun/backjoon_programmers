N = int(input())
# A = list(map(int, input().split()))

"""
memo[i][0] : 이번 잔은 안 마심
memo[i][1] : 직전 잔은 안 마시고 이번 잔은 마심
memo[i][2] : 직전 잔도 마시고 이번 잔도 마심

memo[i][0] = max(memo[i-1])
memo[i][1] += memo[i-1][0]
memo[i][2] += max(memo[i-1][1], memo[i-1][2])
"""
memo = [[0, 0, 0] for _ in range(N)]
arr = [int(input()) for _ in range(N)] # EOFerror를 처음 봄.... 기왕이면 이렇게 미리 받아서 처리하는 게 좋다고 함

if N < 2:
    print(arr[0])
else:
    # idx 0, idx 1
    for i in range(2):
        if i == 0:
            memo[i][1] = arr[i]
            memo[i][2] = arr[i]
        elif i == 1:
            memo[i][0] = memo[i - 1][1]
            memo[i][1] = arr[i] + memo[i - 1][0]
            memo[i][2] = arr[i] + memo[i - 1][1]

    # idx 2...
    for i in range(2, N):
        memo[i][0] = max(memo[i - 1])
        memo[i][1] = arr[i] + memo[i - 1][0]
        memo[i][2] = arr[i] + memo[i - 1][1]

    print(max(memo[N - 1]))