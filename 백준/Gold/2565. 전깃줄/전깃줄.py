N = int(input())

"""
한쪽을 오름차순 정렬했을 때, 다른 한쪽이 얼마나 오름차순을 준수하는지를 파악한다 
그리고 그것은 곧 다른 한쪽의 가장 긴 증가하는 수열의 최대 길이를 구하는 것과 같다
"""
arr = []

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[0])

# 반대편은 얼마나 오름차순을 지키고 있는가?
memo = [1 for i in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if arr[i][1] > arr[j][1]:
            memo[i] = max(memo[i], memo[j] + 1)

print(N - max(memo)) # 오름차순 안 지킨 애들이 제거해야 할 전깃줄