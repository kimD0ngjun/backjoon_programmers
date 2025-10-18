from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

memo = []

for el in A:
    low = bisect_left(memo, el)

    if low >= len(memo): memo.append(el)
    else: memo[low] = el

print(len(memo))