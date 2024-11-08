import sys

N, M = map(int, input().split())

homes = []
chickens = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            homes.append((i, j))
        elif line[j] == 2:
            chickens.append((i, j))

"""
치킨 거리: 집으로부터 주변 치킨집들 중 거리가 가장 가까운 곳
"""

result = sys.maxsize


def cal_distances(chickens, homes):
    distances = 0

    for home in homes:
        h1, h2 = home
        distance = sys.maxsize

        for chicken in chickens:
            c1, c2 = chicken
            distance = min(distance, abs(c1 - h1) + abs(c2 - h2))

        distances += distance

    return distances


def backtrack(start, sequence):

    global result

    if len(sequence) == M:
        # print("----------")
        # print(sequence)
        distance = cal_distances(sequence, homes)
        result = min(result, distance)
        # print("치킨 거리: " + str(distance))
        # print("----------")
        return

    for i in range(start, len(chickens)):
        if chickens[i] not in sequence:
            sequence.append(chickens[i])
            backtrack(i + 1, sequence)
            sequence.pop()


backtrack(0, [])
print(result)