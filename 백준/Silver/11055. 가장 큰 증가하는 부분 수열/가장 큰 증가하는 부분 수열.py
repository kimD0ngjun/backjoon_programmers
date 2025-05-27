n = int(input())
seq = list(map(int, input().split()))

memo = seq[:] # i번쨰 인덱스까지의 최대합 업데이트용 메모이제이션

# 바로 직전까지의 최대합 + 현재 인덱스값과 비교... 비교... 비교

for i in range(0, n):

    for j in range(0, i):
        # 증가할 떄만 메모배열 갱신
        if seq[j] < seq[i]:
            memo[i] = max(memo[i], memo[j] + seq[i]) # 어떻게? 현재 자기 자신과, 직전의 메모값과 seq[i]를 더한 값을 서로 비교


print(max(memo))