N, r, c = map(int, input().split())

"""
00 01 02 03
10 11 12 13
20 ....

divide : N(2^N) -> N-1(2^(N-1) 길이인 4개의 서브 구역)
4개 구역 중 어디에 있는가?
재귀적으로 너비가 2^N-1보다 크거나 같으면 오른쪽, 작다면 왼쪽
재귀적으로 높이가 2^N-1보다 크거나 같으면 아래쪽, 작다면 윗쪽

N > 1
'왼 위'의 가장 큰 순서 : 2**(2N-2) - 1.  '오른 위'의 가장 큰 순서 : 2**(2N-1) - 1
x, y : (2**(N-1) - 1, 2**(N-1) - 1)  x, y : (2**(N-1) - 1, 2**N - 1) 
'왼 아래'의 가장 큰 순서 : 3*2**(2N-2) - 1.  '오른 아래'의 가장 큰 순서 : 2**(2N) - 1
x, y : (2**N - 1, 2**(N-1) - 1)          x, y : (2**N - 1, 2**N - 1) 

조건문 4개 분기로 나눠서 하나의 재귀 자식만 호출

---

현재(N)의 배열 내에서 가장 큰 값은 2**(2N) - 1
r, c가 인덱스 범위 중 어디에 속하냐에 따라 해당 서브 배열로 들어간다
그때의 파라미터는 N-1, 해당 서브 배열의 가장 큰 순서값
인덱스도 줄어드는 범위만큼 서브배열 방향에 따라 해당 좌표값을 절삭하면 될듯
"""

def recur(n, x, y, value):
    # extraordinary case
    if n == 1:
        if x == 0 and y == 0:
            return value - 3
        elif x == 0 and y == 1:
            return value - 2
        elif x == 1 and y == 0:
            return value - 1
        elif x == 1 and y == 1:
            return value

    # 1번째 서브 배열
    if 0 <= x < 2**(n-1) and 0 <= y < 2**(n-1):
        return recur(n - 1, x, y, value - 3 * 2**(2*(n-1)))
    # 2번째 서브 배열
    elif 0 <= x < 2**(n-1) and 2**(n-1) <= y < 2**n:
        return recur(n - 1, x, y - 2**(n-1), value - 2 * 2**(2*(n-1)))
    # 3번째 서브 배열
    elif 2**(n-1) <= x < 2**n and 0 <= y < 2**(n-1):
        return recur(n - 1, x - 2**(n-1), y, value - 2**(2*(n-1)))
    # 4번째 서브 배열
    elif 2**(n-1) <= x < 2**n and 2**(n-1) <= y < 2**n:
        return recur(n - 1, x - 2**(n-1), y - 2**(n-1), value)

print(recur(N, r, c, 2**(2*N) - 1))