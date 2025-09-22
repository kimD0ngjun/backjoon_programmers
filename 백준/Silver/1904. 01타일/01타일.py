N = int(input())
# count = 0
#
# def recur(n):
#     global count
#
#     if n == N:
#         count += 1
#         return
#     elif n > N:
#         return
#
#     recur(n + 1)
#     recur(n + 2)
#
# recur(0)
# print(count % 15746)

"""
memo[n] = memo[n-1] + memo[n-2]
"""
# memo = [0 for _ in range(N + 1)]
# memo[1] = 1 # "1"
# memo[2] = 2 # "11", "00"
#
# for i in range(3, N + 1):
#     memo[i] = memo[i - 1] + memo[i - 2]
#
# print(memo[N] % 15746)

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a = 1
    b = 2
    count = 0

    for _ in range(3, N + 1):
        count = (a + b) % 15746
        a = b # 다음 단계 이동
        b = count # 다음 단계 이동

    print(count % 15746)