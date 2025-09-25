N = int(input())
A = list(map(int, input().split()))

"""
2차원 리스트?
memo[a][b] = a부터 b까지의 가장 긴 증가하는 부분 수열 길이 갱신?
-> 시간복잡도 n**2

memon[i] = 인덱스 i까지의 최단 배열 길이?
"""

memo = [1 for i in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            # 인덱스 j까지의 최대 길이 + 1
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))