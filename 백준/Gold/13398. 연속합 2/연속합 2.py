"""
https://www.acmicpc.net/problem/13398
"""

# 입력 처리
N = int(input())
nums = list(map(int, input().split()))

"""
쌓아가면서 

수를 하나 제거해도 된다 -> 제거한 케이스와 제거하지 않은 케이스 둘 다 비교
dp 배열 2개 각각 비교?
"""

# 빼지 않은 경우, 뺀 경우
dp = [[x for x in nums], [x for x in nums]]

for i in range(1, N):
    # 더한 게 더 클지 아니면 그냥 놔둔 게 더 클지
    dp[0][i] = max(dp[0][i - 1] + nums[i], dp[0][i])

    # 그냥 놔둔 게 더 클지, 이전꺼 생략시키고 현재 요소 포함시키는 합이 더 클지
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + nums[i])

# 뺴지 않은 경우와 뺀 경우의 최대값을 각각 구하고 둘 중 최대값 최종 산출
print(max(max(dp[0]), max(dp[1])))