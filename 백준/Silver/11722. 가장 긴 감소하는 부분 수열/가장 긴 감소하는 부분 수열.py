n = int(input())
seq = list(map(int, input().split()))

memo = [1] * n # 최악의 경우 자기 혼자만 덩그러니 남는 길이

for i in range(0, n):

    for j in range(0, i):
        # 증가할 떄만 메모배열 갱신
        if seq[j] > seq[i]:
            memo[i] = max(memo[i], memo[j] + 1) # 어떻게? 현재 자기 자신과, 직전의 메모값과 1을 추가 카운팅한 값을 서로 비교

# print(memo)
print(max(memo))