N, M = map(int, input().split())
mylist = sorted(list(map(int, input().split())))
answer= []

def dfs(n, n_list):
    if n == M: #종료
        answer.append((n_list[:]))
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n + 1, n_list + [mylist[i]])
            visited[i] = 0

visited = [0]*N # 방문 처리용

dfs(0, [])

for mylist in answer:
    print(*mylist)