N = int(input())
A = list(map(int, input().split()))

"""
2차원 리스트?
memo[a][b] = a부터 b까지의 가장 긴 증가하는 부분 수열 길이 갱신?
-> 시간복잡도 n**2

memon[i] = 인덱스 i까지의 최단 배열 길이?
"""

memo = [[1, 1] for i in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            # 인덱스 j까지의 최대 길이 + 1
            memo[i][0] = max(memo[i][0], memo[j][0] + 1)

for i in range(N-2, -1, -1):
    # for j in range(N-1, i, -1): -> N이 너무 작으니까 돌아야 할 인덱스 변수가 사라져버리네 자꾸
    for j in range(i+1, N):
        if A[i] > A[j]:
            memo[i][1] = max(memo[i][1], memo[j][1] + 1)

print(max(memo[i][0] + memo[i][1] - 1 for i in range(N)))
