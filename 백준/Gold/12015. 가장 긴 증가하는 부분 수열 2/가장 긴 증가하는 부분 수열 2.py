# https://www.acmicpc.net/problem/12015
# import sys
#
# input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

"""
기존 dp 기반 문제점 : O(N**2) = 전체 수열 탐색 N에 각 인덱스별 최대길이 갱신 작업 N
어떤 인덱스의 요소는 최대 길이를 계산에 고려할 필요조차 없는 값일 수도 있지만,
dp는 그걸 고려하지 않기 때문에 갱신 작업도 O(N) 
[10, 20, 30, 40, 0, 50, 60] 
-> 이런 경우에서 idx 4의 요소는 별 필요 없지만 얘를 거쳐야 dp 메모가 갱신 가능(불필요한 연산)

위의 케이스에서, idx 3은 길이 2, 3, 4 부분수열 최대값 -> 차후 50을 마주하면 또 갱신됨
"""
# memo[idx] : 길이가 idx + 1인 부분수열의 최대값
memo = []

for el in A:
    # 이진 탐색
    # memo에서 수열 요소 el이 들어갈 자리를 찾는다
    # low = 0 # 분기당 memo 낮은 idx
    # high = len(memo) - 1 # 분기당 memo 높은 idx
    # # temp_idx = 1
    #
    # while low <= high:
    #     # print(f"{temp_idx} 단계")
    #     mid = (low + high) // 2
    #
    #     if memo[mid] < el:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    low = bisect_left(memo, el)

    # print(f"도출된 memo : {memo}\n도출된 인덱스 : {low}\nmemo 밖의 값인가? : {low >= len(memo)}")

    # memo 범위를 넘어서는 요소면 현재 memo 내의 값들보다 가장 큰 값
    if low >= len(memo):
        memo.append(el)
    # memo 범위 내라면 더 늘일 여지가 있는 해당 길이의 낮은 값(1, 2, 4 .... 3, 4 ...)
    else:
        memo[low] = el

    # print(f"갱신된 memo : {memo}")

print(len(memo))