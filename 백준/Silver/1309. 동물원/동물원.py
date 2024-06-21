"""
https://www.acmicpc.net/problem/1309
"""
import sys
sys.setrecursionlimit(100000)

# 우리 한 줄 크기
N = int(input())

# 메모이제이션 최적화 -> 인덱스 1부터 활용
memo = [0] * (N + 1)

# 점화식 기반 재귀함수
def recursion(n):
    if n == 1:
        return 3

    if n == 2:
        return 7

    # 메모이제이션
    if memo[n] != 0:
        return memo[n]

    memo[n] = (recursion(n-1) * 2 + recursion(n-2)) % 9901
    return memo[n]


print(recursion(N))