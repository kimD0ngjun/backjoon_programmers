# 36264 KB, 3184 ms
N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]

"""
memo[i] : 무게 i에서 추구할 수 있는 최대 가치
"""
memo = [0 for _ in range(K+1)]

for w, v in arr:

    # optimization
    if w > K:
        continue

    """
    i로 지정된 무게값에 w를 더할 수 있는지를 확인
    넣을 수 있다는 건, 가치 값 합산이 가능하니까 
    w가 포함되기 전의 무게인 i-w에 저장된 가치인 memo[i-w]에서 v를 더하면 갱신
    즉, memo[i] = memo[i-w] + v
    """
    """
    뭔가 정방향은 가다가(반복문 idx) 유턴하다가(memo[i-w] 참조) 다시 가다가 유턴하다가 이런 느낌인데 
    역방향은 그냥 역방향만으로만 가니까(반복문의 방향과 memo[i-w]의 방향이 같은..?) 중복을 배제할 수 있으려나
    """
    # for i in range(1, K+1):
    for i in range(K, -1, -1):
        if i - w < 0:
            continue

        memo[i] = max(memo[i-w] + v, memo[i]) # 이전 계산값을 i 무게 기준 최대 갱신이 가능한지?

print(memo[K])



# """
# 입력 단계
# """

# cases = []
# count, max_weight = map(int, input().split())  # 주어진 수열
# memo = [0] * (max_weight + 1) # 0부터 max_weight 까지

# # 핵심은 특정 조합이 되냐? 안되냐? 로
# # 특정 조합이 안되면, 특정 조합을 포함하는 애들은 전부 안되는 거
# # 그걸 memoization

# """
# weight	A	B	C	D
# 0	    0	0	0	0
# 1	    0	0	0	0
# 2	    0	0	0	0
# 3	    0	0	6	6
# 4	    0	8	8	8
# 5	    0	0	0	12
# 6	    13	13	13	13
# 7	    0	0	14	14
# """
# # A -> B -> C -> D 순으로 차례대로 넣었을 때
# # 한줄 한줄이 곧 memo의 업데이트 과정
# # 이중 리스트에서의 내부 요소 값들은 산출되는 최대값으로 업데이트가 되어야 함

# for _ in range(count):
#     weight, value = map(int, input().split())

#     # 최적화
#     if weight > max_weight:
#         continue

#     # 최대 무게(가방 제한)에서 역순으로 무게를 줄여보면서(1번줄까지)
#     for i in range(max_weight, 0, -1):
#         # 입력된 무게와 이전에 입력됐던 무게들 합이 최대 무게제한 이하면서
#         # 메모이제이션에 기록된 값이 0이 아니라면(즉, 이전에 이미 탐색됐더라면)
#         if i + weight <= max_weight and memo[i] != 0:
#             # 가치 비교하면서 맥스값 업데이트(즉 A -> B -> C ... 하는 과정의 화살표에 해당하는 부분)
#             memo[i + weight] = max(memo[i + weight], memo[i] + value)

#     # 0번줄에 대한 처리
#     # 현재 무게만을 넣었을 때의 가치를 메모
#     memo[weight] = max(memo[weight], value)

# # 최종 업뎃된 메모들 중 최대값 반환
# print(max(memo))




