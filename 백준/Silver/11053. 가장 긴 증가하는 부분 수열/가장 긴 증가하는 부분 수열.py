count = int(input())  # 수열의 길이
array = list(map(int, input().split()))  # 주어진 수열

# memoization
# 각 요소별 시작 길이 카운팅에서 이전 머리에 해당하는 수열이 있으면 이어붙이는 식
memo = [1] * count

"""
반복문
"""
for i in range(1, count):
    for j in range(0, i):
        # 만일 기준 요소보다 이전의 요소들 중에 작은 값이 있으면
        if array[j] < array[i]:
            # 특정 지점에서 역순으로 바라보며 현 시점의 길이와 
            # 이전 시점의 길이를 카운팅한 것들 중 큰 값으로 메모 업데이트
            memo[i] = max(memo[i], memo[j] + 1)

# 메모들 요소가 곧 해당 요소까지의 증가분 길이
result = max(memo)
print(result)