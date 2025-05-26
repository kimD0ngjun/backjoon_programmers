n = int(input())
seq = list(map(int, input().split()))

memo = seq[:] # i번쨰 인덱스까지의 최대합 업데이트용 메모이제이션

# memo[i] = max(seq[i], memo[i - 1] + seq[i]) : 바로 직전까지의 최대합 + 현재 인덱스값과 비교... 비교... 비교

for i in range(1, n):
    memo[i] = max(seq[i], memo[i - 1] + seq[i])

print(max(memo))