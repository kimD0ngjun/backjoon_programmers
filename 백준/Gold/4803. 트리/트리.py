class Union_Find:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])

        return self.parent[x]

    def union_root(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        # 합치기 전에 이미 같은 루트다 == 이미 같은 연결 성분이다
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

case = 1
answers = []

while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    uf = Union_Find(N + 1)
    cycle = [False] * (N + 1) # 각 연결 요소마다 사이클 판별 확인

    for _ in range(M):
        # 간선이 제시된 순서대로 노드들을 연결해나가본다
        a, b = map(int, input().split())
        root_a = uf.find_root(a)
        root_b = uf.find_root(b)

        if root_a == root_b: # 이미 사이클이 형성된 상태
            cycle[root_a] = True
        else: # 아니라면 하나의 연결 성분으로 합침
            uf.union_root(root_a, root_b)
            new_root = uf.find_root(root_a)
            # 만약 두 연결 성분들 중 하나라도 사이클이 생기는 경우 반영
            cycle[new_root] = cycle[root_a] or cycle[root_b]

    roots = set()
    for i in range(1, N + 1):
        root = uf.find_root(i)

        # 사이클이 아니면서 루트의 지위를 유지하고 있는 애들만
        if not cycle[root]:
            roots.add(root)

    if len(roots) == 0:
        answers.append(f"Case {case}: No trees.")
    elif len(roots) == 1:
        answers.append(f"Case {case}: There is one tree.")
    else: # 2개 이상의 트리들로 구성된 집합 그래프
        answers.append(f"Case {case}: A forest of {len(roots)} trees.")

    case += 1

print(*answers, sep="\n")