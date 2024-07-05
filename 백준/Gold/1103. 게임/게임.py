"""
https://www.acmicpc.net/problem/1103
"""
import sys
sys.setrecursionlimit(1_000_000)

# 입력 처리
M, N = map(int, input().split())

maps = []

for _ in range(M):
    row = [int(char) if char != 'H' else -1 for char in input()]
    maps.append(row)

# print(maps)

"""
방문 기록 기억시키면서 만약 방문한 곳 또 방문하게 되면 -1 출력
구멍(-1) 밟으면 그대로 모든 과정 종료

bfs보다는 어느 한 루트 골랐을 때, 무한회귀하는지 운 좋으면 바로 확인 가능한 dfs가 메모리 좀 덜 들지도?
"""

# 방문 기억
visited = [[False] * N for _ in range(M)]
# 최댓값 갱신용 dp
dp = [[0] * N for _ in range(M)]

# 방향 전환용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
loop = False


# 재귀 호출용 dfs 함수
def dfs(x, y, count):
    global answer
    global loop

    # 카운트 최고값 계속 갱신시키기
    answer = max(answer, count)

    for i in range(4):
        # 다음 방향
        next_x = x + maps[x][y] * dx[i]
        next_y = y + maps[x][y] * dy[i]

        # 맵 내부에 있고 해당 다음 경로가 구멍이 아닐 때
        """
        - 재귀호출되는 시점
        이 부분에서 더 재귀호출되는 것을 막는 게 시간 소요를 조금이라도 줄일듯
        현재까지 기록된 카운팅이 dp에서 기억하는 카운팅보다 더 작으면 굳이 재귀호출 반복할 필요 x
        """
        if 0 <= next_x < M and 0 <= next_y < N and maps[next_x][next_y] != -1 and count > dp[next_x][next_y]:

            # 하지만 방문했다면...?
            if visited[next_x][next_y]:
                loop = True
                break

            # 아직 방문도 안 됐다면
            else:
                # dp 최댓값 업데이트
                dp[next_x][next_y] = count

                # 방문 처리
                visited[next_x][next_y] = True
                dfs(next_x, next_y, count + 1)

                # 재귀 호출 후에, 방문 기록을 다시 돌려놔야 다른 재귀호출 서브 함수들이랑 기록 공유 x
                visited[next_x][next_y] = False


# 함수 호출 시작
dfs(0, 0, 1)

if loop:
    print(-1)
else:
    print(answer)