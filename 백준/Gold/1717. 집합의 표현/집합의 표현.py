"""
https://www.acmicpc.net/problem/1717
"""

# 유니온파인드
class UnionFind:
    def __init__(self, size):
        # 각 노드의 부모를 자기 자신으로 초기화
        self.parent = list(range(size))
        # 각 트리의 높이를 0으로 초기화(노드 i가 루트인 트리의 높이)
        self.rank = [0] * size

    def find_root(self, x):
        # x가 루트 노드인지 확인
        if self.parent[x] != x:
            # 경로 압축: 부모를 직접 루트로 재귀적 업데이트
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def union_root(self, x, y):
        # x와 y의 루트를 찾는다
        rootX = self.find_root(x)
        rootY = self.find_root(y)

        # 루트가 다르면 서로 다른 트리이므로 합친다
        if rootX != rootY:
            # 유니온 by 랭크를 적용(높이 비교를 통해 더 낮은 높이의 트리에게 붙인다)
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            # 둘다 높이가 같으면 걍 하나를 루트로 지정하고 높이만 1 증가
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# 입력
n, m = map(int, input().split())

# 연산
results = []
uf = UnionFind(n + 1)  # 원소 개수 == n + 1

for _ in range(m):

    i, a, b = map(int, input().split())

    if i == 0:
        uf.union_root(a, b)
    elif i == 1:
        if uf.find_root(a) == uf.find_root(b):
            results.append("YES")
        else:
            results.append("NO")

# 출력
for result in results:
    print(result)


