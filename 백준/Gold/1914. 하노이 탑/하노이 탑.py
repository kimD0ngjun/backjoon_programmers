N = int(input())
answers = []

# n : 옮길 원판 갯수, fr : 시작 막대, tmp : 임시 막대, to : 도착 막대
def hanoi(n, fr, tmp, to):
    # global count

    if n == 1:
        # count += 1
        # answers.append((fr, to))
        print(fr, to)
    else:
        """
        n이 3일 때,
        1 -> 2, 2 1 0
        1 -> 3, 1 1 1
        2 -> 3, 1 0 2
        1 -> 3, 0 0 3
        """
        hanoi(n - 1, fr, to, tmp) # 목표 막대로 옮기기 위해 임시 막대에 걸리적거리는 n - 1개 임시 안착
        # count += 1
        # answers.append((fr, to)) # 이제 목표 막대로 옮길 수 있게 됨
        print(fr, to)
        hanoi(n - 1, tmp, fr, to) # 임시 막대에 넣어둔 n - 1개 원반들 목표 막대로 옮기기

print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)