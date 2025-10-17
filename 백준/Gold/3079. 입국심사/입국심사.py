N, M = map(int, input().split())

# k번 심사대에서 걸리는 심사 시간: tables[k-1]
tables = [int(input()) for _ in range(N)]

"""
탐색 범위는 1부터(0초는 말이 안되니까..) 심사대 중 가장 오래 걸리는 심사대 시간 * 인원수 -> 이진 탐색
파라메트릭 서치니까 check 함수를 만들어서 분기를 나눠야 하고(그리디 시뮬레이션)
대충 감이 잡힌다
"""

# 독립적인 그리디 시뮬레이션
# 주어진 시간(time) 내로 M명의 인원을 커버할 수 있나?
def check(time) -> bool:
    """
    실제로는 병렬 처리겠지만, 지금은 가능성의 여부 판별이니까 순차적으로 단위 작업(사람) 배치해보며 가능한지 확인해보기

    time : 주어진 시간
    time // table : 한 심사대에서 '주어진 시간' 내에 처리 가능한 사람 수
    time % table : 최대한 처리했고 남은 쉬는 시간 -> 쥐어짜서 다른 사람도 받게 하려면 다음 심사대로 넘겨야 함
    그 다음으로 넘기는 나머지가 곧 time // next_table에 포함하게 됨(파이프 흐름 생각)
    """
    return M <= sum(time // table for table in tables)

min_time = 1
max_time = max(tables) * M
answer = max_time

while min_time <= max_time:
    mid = (max_time + min_time) // 2

    if check(mid):
        answer = mid
        max_time = mid - 1
    else:
        min_time = mid + 1

print(answer)