"""
N퀸 문제는, N 길이의 배열 안에 1부터 N까지의 숫자를 중복 없이 배치하는 것과 같다
"""
N = int(input())
row = 0 # [-1 for _ in range(N)] # 열 메모
left = 0 # set() # 오른쪽 아래 대각선 메모
right = 0 # set() # 왼쪽 아래 대각선 메모
count = 0

"""
오른쪽 아래방향 가능한 대각선 가짓수는 (행 - 열) -> 0,1이랑 1,2
왼쪽 아래방향 가능한 대각선 가짓수는 (행 + 열) -> 2,3이랑 3,2

집합 구조의 해시 연산이 n이 커짐에 따라 시간복잡도가 급증
코드 힌트에서는 비트마스킹을 추천하는데, 집합 대신에 흠...

열 중복 검증은 그냥 앞전의 내용에 있는것들과 비교 
대각선 검증은 오른쪽 아래와 왼쪽 아래를 생각해야 되는데 
오른쪽 아래는 행-열 값으로 계산(가능 범위는 -n부터 n까지) 
왼쪽 아래는 행+열 값으로 계산(가능 범위는 0부터 2n까지)
"""
def backtrack(i):
    global count, row, left, right

    if i == N:
        count += 1
        return

    for n in range(N):
        # if n in board:
        #     continue
        # 열 인덱스만큼 시프팅한 값과 &(1의 자릿수가 둘이 다르면 0 아닌 값, 곧 같은 열에 퀸이 있음)
        if (row & (1 << n)) != 0:
            continue

        # if n - i in left or n + i in right:
        #     continue

        """
        왼쪽 아래는 행 + 열 값이 일정(범위가 0부터 2N-2까지)
        오른쪽 아래는 행 - 열 값이 일정 (범위가 -(N-1)부터 N-1까지니까 N-1 더해서 범위 재지정)
        """
        if (left & (1 << i + n)) != 0:
            continue

        if (right & (1 << i - n + (N - 1))) != 0:
            continue

        # board[i] = n
        # left.add(n - i)
        # right.add(n + i)
        """
        합산 처리 ex) 0010 | 0100 == 0110
        """
        row = row | (1 << n)
        left = left | (1 << i + n)
        right = right | (1 << i - n + (N - 1))

        backtrack(i + 1)

        """
        다시 백트랙킹 ex) 0010 & ~0100 == 0010 & 1011 == 0010
        """
        row = row & ~(1 << n)
        left = left & ~(1 << i + n)
        right = right & ~(1 << i - n + (N - 1))
        # board[i] = -1
        # left.remove(n - i)
        # right.remove(n + i)
        
backtrack(0)
print(count)
