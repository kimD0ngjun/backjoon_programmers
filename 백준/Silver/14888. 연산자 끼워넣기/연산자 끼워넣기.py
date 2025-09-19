import sys

N = int(input())
sequence = list(map(int, input().split()))
operator = list(map(int, input().split()))

min_value = sys.maxsize
max_value = - sys.maxsize

def backtrack(value, idx, pl, mi, mu, di):
    global min_value, max_value

    if pl + mi + mu + di == 0:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    if pl > 0:
        value += sequence[idx]
        backtrack(value, idx + 1, pl - 1, mi, mu, di)
        value -= sequence[idx]

    if mi > 0:
        value -= sequence[idx]
        backtrack(value, idx + 1, pl, mi - 1, mu, di)
        value += sequence[idx]

    if mu > 0:
        value *= sequence[idx]
        backtrack(value, idx + 1, pl, mi, mu - 1, di)
        value = int(value / sequence[idx])

    if di > 0:
        value /= sequence[idx]
        backtrack(int(value), idx + 1, pl, mi, mu, di - 1)
        value *= sequence[idx]

backtrack(sequence[0], 1, operator[0], operator[1], operator[2], operator[3])

print(max_value)
print(min_value)