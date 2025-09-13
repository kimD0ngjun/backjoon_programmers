N = int(input())
sequence = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

answers = []

# 에라토스테네스
# 최대 합이라 해도 2000을 넘지 않으니 밀러 라빈은 오버엔지니어링일듯
is_prime = [True] * 2001
is_prime[0] = is_prime[1] = False

for i in range(2, int(2000**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 2001, i):
            is_prime[j] = False

"""
백트랙킹 후, 정답 재정렬은 시간초과(3퍼에서 터짐)
백트랙킹 자체가 문제의 해결 수단이 아닌 것 같음
"""
# # dfs 백트랙킹
# # 첫 번째 요소와 나머지 놈들 전부 더하며 소수 판별 후, 맞다면 백트랙킹 시도
# # 2개씩 짝지어서 선택해야 되니까 rest를 item으로 채워가지 않고 그냥 rest 내에서 2개씩 선택?
# def dfs(remaining):
#     # 전부 소수 쌍 생성에 성공한 경우
#     if len(remaining) == 0:
#         return True
#
#     first = remaining[0]
#     for i in range(1, len(remaining)):
#         second = remaining[i]
#
#         # 두 쌍의 합이 소수다?
#         if is_prime[first + second]:
#             next_remaining = remaining[1:i] + remaining[i + 1:]
#             if dfs(next_remaining):
#                 return True
#
#     return False
#
# for i in range(1, N):
#     pair = sequence[0] + sequence[i]
#
#     if not is_prime[pair]:
#         continue
#
#     rest = sequence[1:i] + sequence[i + 1:]
#     if dfs(rest):
#         answers.append(sequence[i])

"""
얘 덕에 이분 매칭을 공부하네...
"""
# 이분 매칭용 그래프 생성하기
for i in range(N):
    for j in range(i + 1, N):
        if is_prime[sequence[i] + sequence[j]]:
            graph[i].append(j)
            graph[j].append(i)

# print(graph)
def dfs(node):
    # 첫 번째 요소도 제외
    if visited[node] or node == 0:
        return False
    visited[node] = True

    for adj in graph[node]:
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = node
            return True

    return False

for el_idx in graph[0]:
    match = [-1] * N
    match[el_idx] = 0 # 인접 인덱스를 첫 번째 인덱스로 매핑
    count = 1 # 매핑 카운트

    for i in range(1, N):
        visited = [False] * N
        if dfs(i): count += 1

    if count == N:
        answers.append(sequence[el_idx])

if not answers:
    print(-1)
else:
    print(*sorted(answers))