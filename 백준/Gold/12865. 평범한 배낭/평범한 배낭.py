"""
입력 단계
"""

cases = []
count, max_weight = map(int, input().split())  # 주어진 수열
memo = [0] * (max_weight + 1) # 0부터 max_weight 까지

# 핵심은 특정 조합이 되냐? 안되냐? 로
# 특정 조합이 안되면, 특정 조합을 포함하는 애들은 전부 안되는 거
# 그걸 memoization

"""
weight	A	B	C	D
0	    0	0	0	0
1	    0	0	0	0
2	    0	0	0	0
3	    0	0	6	6
4	    0	8	8	8
5	    0	0	0	12
6	    13	13	13	13
7	    0	0	14	14
"""
# A -> B -> C -> D 순으로 차례대로 넣었을 때
# 한줄 한줄이 곧 memo의 업데이트 과정
# 이중 리스트에서의 내부 요소 값들은 산출되는 최대값으로 업데이트가 되어야 함

for _ in range(count):
    weight, value = map(int, input().split())

    # 최적화
    if weight > max_weight:
        continue

    # 최대 무게(가방 제한)에서 역순으로 무게를 줄여보면서(1번줄까지)
    for i in range(max_weight, 0, -1):
        # 입력된 무게와 이전에 입력됐던 무게들 합이 최대 무게제한 이하면서
        # 메모이제이션에 기록된 값이 0이 아니라면(즉, 이전에 이미 탐색됐더라면)
        if i + weight <= max_weight and memo[i] != 0:
            # 가치 비교하면서 맥스값 업데이트(즉 A -> B -> C ... 하는 과정의 화살표에 해당하는 부분)
            memo[i + weight] = max(memo[i + weight], memo[i] + value)

    # 0번줄에 대한 처리
    # 현재 무게만을 넣었을 때의 가치를 메모
    memo[weight] = max(memo[weight], value)

# 최종 업뎃된 메모들 중 최대값 반환
print(max(memo))


