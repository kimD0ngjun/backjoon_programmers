from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

memo = [] # memo[i] : 길이 i+1 부분수열의 최대값(마지막 값)
memo_idx = [] # memo_idx[i] : 길이 i+1 부분수열의 최대값(마지막 값)의 A 인덱스
prev = [-1] * N # prev[i] : i의 바로 직전 인덱스

for i in range(N):
    # print(f"{i}단계")
    el = A[i]
    idx = bisect_left(memo, el)

    # 인덱스 추적 메모도 추가
    if idx >= len(memo):
        memo.append(el)
        memo_idx.append(i)
    else:
        memo[idx] = el
        memo_idx[idx] = i

    # 메모 기준 인덱스(idx) + 1 == 부분수열의 길이
    if idx > 0:
        """
        바로 직전 길이((idx+1) - 1)의 부분수열의 마지막 값 A 인덱스 저장
        """
        prev[i] = memo_idx[idx - 1]

    # print(f"메모 : {memo}")
    # print(f"메모 인덱스 : {memo_idx}")
    # print(f"이전 인덱스 추적 : {prev}")

result = []
lis_idx = memo_idx[-1] # lis_idx는 A에서의 인덱스

while lis_idx != -1:
    result.append(A[lis_idx])
    lis_idx = prev[lis_idx]

print(len(memo))
print(*reversed(result))