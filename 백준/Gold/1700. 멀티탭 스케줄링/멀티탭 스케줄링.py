"""
https://www.acmicpc.net/problem/1700
"""
import sys


# 입력
def sys_input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
equipments = list(map(int, sys_input().split()))

"""
1) 최대한 자주, 많이 사용하는 전기기구일수록 최대한 덜 뽑고 계속 멀티탭에 나둬야 이득
2) 다 쓴 (즉, counts의 value가 0이 된다면) 기구들 우선으로 교체하는 것이 이득
3) 각 분기에서 최소 잔여 사용횟수의 전기기구를 뽑는 게 이득
-> 틀림 
2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
.. 이럴 때, 3을 먼저 뽑고 2 1 쓰다가 마지막에 3 쓸 때 암거나 뽑아서 쓰면 딱 2번만에 해결
근데 내 초기 가설에 따르면 최소 잔여횟수를 기준으로 뽑기 때문에 반례 발생

* 즉, 분기마다 최소사용횟수를 기준으로 뽑으면 x
* 새로운 놈이 난입했을 때 
-> 1) 향후 사용횟수가 0이면 걔를 먼저 뽑기 + 2) 아직 사용횟수가 남아있는 놈들이라면...그 분기를 기점으로 가장 나중에 다시 복귀할 놈을 뽑아버리기 
"""

# 연산
change = 0  # 교체 횟수
tab = set()  # 멀티탭

# change 연산
for i in range(K):
    equipment = equipments[i]

    # 이미 멀티탭에 꽂힌 기구면 굳이 볼 필요 x
    if equipment in tab:
        continue

    # 멀티탭 여유가 있는 상황이면 그냥 꽂기
    if len(tab) < N:
        tab.add(equipment)
        continue

    # 멀티탭이 다 꽂혀 있고, 해당 기구를 새로 꽂아야 함
    if equipment not in tab and len(tab) == N:

        later_index = -1  # 가장 나중에 사용할 장비의 인덱스 초기화
        change_equipment = -1  # 뽑을 장비 초기화

        # 멀티탭 순회
        for cur_equipment in tab:
            find = False  # 찾았니?

            # 마지막 인덱스까지 기구 탐색
            for j in range(i + 1, K):
                # 플러그에 꽂힌 기구를 향후 사용예정기구들 중에서 찾음
                if equipments[j] == cur_equipment:
                    find = True  # 찾음!

                    # 그게 현 분기에서 가장 나중 사용 예정이라면 업데이트
                    if j > later_index:
                        later_index = j
                        change_equipment = cur_equipment

                    break

            # 나중 사용 예정인 걸 못 찾았다면 그건 앞으로 사용 안 할 예정
            # 그러니 얘를 뽑는게 이득
            if not find:
                change_equipment = cur_equipment
                break

        # 교체 기구랑 바꾸고 카운팅
        tab.remove(change_equipment)
        tab.add(equipment)
        change += 1


print(change)
