# N, M = map(int, input().split())
#
#
# def backtrack(N, M, sequence, start):
#
#     if len(sequence) == M:
#         print(" ".join(map(str, sequence)))
#         return
#
#     for i in range(start, N + 1):
#         sequence.append(i)
#         backtrack(N, M, sequence, i)
#         sequence.pop()
#
#
# backtrack(N, M, [], 1)
from collections import deque

N = int(input())
numbers = deque(list(map(int, input().split())))
symbols = list(map(int, input().split()))

max_answer = -1_000_000_000
min_answer = 1_000_000_000


def backtrack(numbers, symbols, value):
    global max_answer, min_answer

    if len(numbers) == 0:
        max_answer = max(max_answer, value)
        min_answer = min(min_answer, value)
        return

    for i in range(4):
        if symbols[i] == 0:
            continue

        temp = numbers[0]
        numbers.popleft()
        symbols[i] -= 1

        if i == 0:
            backtrack(numbers, symbols, value + temp)
        elif i == 1:
            backtrack(numbers, symbols, value - temp)
        elif i == 2:
            backtrack(numbers, symbols, value * temp)
        elif i == 3:
            backtrack(numbers, symbols, int(value / temp))

        numbers.appendleft(temp)
        symbols[i] += 1


initial_value = numbers.popleft()
backtrack(numbers, symbols, initial_value)

print(max_answer)
print(min_answer)