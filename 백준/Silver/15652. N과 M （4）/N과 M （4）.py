N, M = map(int, input().split())


def backtrack(N, M, sequence, start):

    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return

    for i in range(start, N + 1):
        sequence.append(i)
        backtrack(N, M, sequence, i)
        sequence.pop()


backtrack(N, M, [], 1)