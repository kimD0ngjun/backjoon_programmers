"""
문제 예시 설명이 많이 이상한데... 1초에 트럭은 1대만 움직일 수 있음
움직인다는 것은 다리에 오르는 데에 1초, 다리 내에서 한 칸 이동하는 데에 1초, 다리에서 내려가는 데에 1초 소요
"""
from collections import deque


# truck_weights 리스트 주어진 순서대로 큐에 들어감
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    wait = deque(truck_weights)
    time = 0

    """
    분기에 다리가 비는 상황은 없다. 처음(이미 앞에서 처리) 마지막 시간 전까지 다리에는 최소 1대의 트럭이 존재한다
    1. 무게 조건이 만족돼서 혹은 대기 트럭이 없어서, 더 이상 트럭 추가 없이 다리 내에서 트럭들이 움직이는 경우(time += bridge_length - len(bridge))
    2. 무게 조건 범위 내에서, 다리에서 트럭이 내림과 동시에 바로 직후의 트럭들이 무게를 만족할 때까지 오르는 경우(time += 트럭 갯수)
    3. 무게 현황이 유지돼야 하는 경우에도(이 경우는 다리에 있는 트럭은 2개 이상), 다리 끝에 도달한 선순위 트럭이 다리에서 벗어나는 경우(time += 1)
    
    1번의 케이스는 분기 내에서 2번과 3번 조건을 뚫은 경우다 -> 얘를 최적화시킬 방법 없으려나...
    """
    while wait or bridge:
        time += 1

        # 3번
        # 다리 맨 앞의 트럭이 마지막 지점에 도달했는지?(1초에 다리 1칸씩 이동)
        if bridge and time - bridge[0][1] >= bridge_length:
            # 도달했으면 가차없이 뺀다
            bridge.popleft()
            # 뺀 거랑 동시에 다리 뒷편에서 트럭이 진입 가능한지 2번 검증이 필요

        # 2번
        # 현재 다리 위 무게 + 추가되는 트럭 무게 조건 만족 시 트럭 진입시킴
        if wait and sum(truck_weight for truck_weight, _ in bridge) + wait[0] <= weight:
            # (트럭의 무게, 트럭의 진입 시점)
            bridge.append((wait.popleft(), time))

    return time