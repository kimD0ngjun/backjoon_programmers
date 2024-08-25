P = 'parent'  # 부모 노드
R = 'rank'  # 트리 높이


def init_uf(size):
    return {P: list(range(size)), R: [0] * size}


def find(uf, x):
    if uf[P][x] != x:
        uf[P][x] = find(uf, uf[P][x])

    return uf[P][x]


def union(uf, x, y):
    rootX = find(uf, x)
    rootY = find(uf, y)

    if rootX != rootY:

        if uf[R][rootX] < uf[R][rootY]:
            uf[P][rootX] = rootY
        elif uf[R][rootX] > uf[R][rootY]:
            uf[P][rootY] = rootX
        else:
            uf[P][rootY] = rootX
            uf[R][rootX] += 1


# 입력
N = int(input())
M = int(input())

uf = init_uf(N)

# 연결 정보 기반 합집합 세팅
for i in range(N):
    connections = list(map(int, input().split()))

    for j in range(N):
        if connections[j] == 1:
            union(uf, i, j)

# 여행 계획
travel = list(map(int, input().split()))

temp = True

travel_root = find(uf, travel[0] - 1)  # 인덱스로 변환해주기 위한 -1

for city in travel:
    if find(uf, city - 1) != travel_root:
        temp = False
        break

if temp:
    print("YES")
else:
    print("NO")