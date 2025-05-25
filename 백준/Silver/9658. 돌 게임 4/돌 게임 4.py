# 알고리즘 감각 다시 살리기...

"""
번갈아가며 돌을 가져가고 턴이 B
마지막 턴에 남은 돌이 1개이거나 3개이면 A가 이김
즉, 마지막에 돌을 3개나 1개를 남기게 하기 위한 이슈

N의 개수가
1 : 창영 승 * 아무리 뒤져봐도 상근이가 이길 방법이 없음
2(1 + 1) : 상근 승
3(1 + 1 + 1) : 창영 승 * 아무리 뒤져봐도 상근이가 이길 방법이 없음
4(3 + 1) : 상근 승
5(4 + 1) : 상근 승
6(3 + 1 + 1 + 1) : 상근 승
7(4 + 1 + 1 + 1) : 상근 승
...

M개까지 진행되고 현재 상근이 차례일 때,

1) M + 1
2) M + 3
3) M + 4

케이스 비교
"""

N = int(input())
memo = [True] * (N + 5)


def dp():
    memo[1], memo[3] = False, False

    for i in range(5, N + 1):
        if memo[i - 1] and memo[i - 3] and memo[i - 4]:
            memo[i] = False
        else:
            memo[i] = True

    return memo[N]


if dp():
    print('SK')
else:
    print('CY')