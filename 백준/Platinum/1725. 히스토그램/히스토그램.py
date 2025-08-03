import sys


def sys_input():
    return sys.stdin.readline().strip()

N = int(sys_input())
histogram = []

for i in range(N):
    histogram.append((i, int(sys_input())))

"""
단순 브루트한 계산은, 구간(n^2) * 구간의 최소 높이 탐색(거의 n) == n^3

최적화를 위해선 중복 탐색을 줄여야 함
중복 계산을 줄이기 위한 요소들을 정리해보자면

(1) 구간
(2) 그 구간 내에서의 최소 높이
(3) 그 구간 내에서의 최소 높이의 갯수

이 3개가 단순 브루트한 계산법의 요소들이고, 저 3개 중에 중복 연산이 발생하므로 줄이자가 핵심...

구간 내에서의 최소 높이 연산에서 중복 연산이 발생하는듯
왜냐면 구간은 독립적이고 절대유일하고, 구간 내에서의 최소 높이 갯수도 결국 구간에 종속되는 독립적이고 절대유일한데,
구간 내에서의 최소 높이는 만약에

4, 4, 4, 5, 6 이렇다면
인덱스 0에서 인덱스 4까지 최소 높이가 4인게

인덱스 1에서 인덱스 4까지도 최소 높이가 4라는 걸 저 0 ~ 4 구간에서 바로 확인이 가능할 것 같은데?
즉, 인덱스 i ~ j 구간의 최소 높이가 정해지면 특정 조건을 충족할 때, 그 내부 부분구간의 최소 높이도 동일할 수 있다. 
그래서 중복 연산 최적화 가능 요소가 구간 내 최소높이 연산이다...

혹시 이 팝 계산 원리가 구간 최소 높이 연산을 줄인다는 게 그 원리인가

1 1 2 3 이런 식의 막대 배치라면

3부터 1까지 인덱스 순으로 팝해서 너비 계산 후 최소높이 곱하기한 게
3부터 0까지 인덱스 순으로 팝해서 너비 계산해서 최소 높이 계산하는 게 당연히 더 넓을 게 자명할 테니 
이 부분에서 중복 연산을 배제하는 최적화가 이뤄진다..?

그럼 스택에 들어갈 건 막대 사이즈(요소)가 아니라 막대 인덱스여야 되나
"""
# 스택은 계단형으로 막대들이 쌓여있음을 보장시킬 것?
stack = []
max_area = 0

for el in histogram:
    idx, height = el

    # 높이 순차를 못지킨 막대가 등장하면 전부 팝하면서 분기마다 직사각형 연산
    # 전체 배치가 순차적이라면 마지막 인덱스를 기준으로 하거나
    if stack and stack[-1][1] > height:
        # 자신과 같거나 낮은 높이까지(어쨌든 구간을 뛰어넘은 계단형 가능)
        while stack and stack[-1][1] > height:
            pop_idx, pop_height = stack.pop()

            if stack:
                # icx가 4이고 팝한 인덱스 값이 2면 너비는 2여야 됨
                # 인덱스 하나가 곧 너비 1 차지, 인덱스 간 계산으로는 너비가 1 부족
                # 만약 인덱스 3 뽑고 인덱스 2 뽑았을 때, 너비는 2임, 근데 현재 pop_idx는 2
                # 4 - 2 - 1 = 1이므로 계산 틀림, pop_idx 다음의 갱신된 꼭대기 기준으로 너비 계산
                width = idx - (stack[-1][0] + 1)
            else:
                # 더 이상 스택이 없다면 stack[-1][0]이 인덱스에러 발생
                # 스택이 없다는 건, 다 비워질 때까지 stack[-1][1] <= height이 아니었다는 셈
                # 즉 pop_icx가 0인 곳까지 도달했으니 (-1 + 1)과 다를 바 없음
                width = idx

            if width * pop_height > max_area:
                max_area = width * pop_height

    stack.append(el)

# 마지막으로 남은 요소들 있는 경우
# 스택에 남는 케이스는 뭐가 있을까
# 일단 모양은 계단형일 수밖에 없다 최후의 계단형
if stack:
    last_idx, last_height = stack.pop()

    max_area = last_height if last_height > max_area else max_area

    while stack:
        last_pop_idx, last_pop_height = stack.pop()

        if stack:
            last_width = last_idx - stack[-1][0]
        else:
            last_width = last_idx + 1

        if last_width * last_pop_height > max_area:
            max_area = last_width * last_pop_height

print(max_area)

"""
30%대 막힘 반례
4
1
1
1
1

-> 결과 3이 나옴 정답은 4일텐데
"""