def largestNumber(nums):
    # 스트링화한 숫자와 늘인 숫자 이중 리스트
    compare = []

    for num in nums:
        str_num = str(num)  # 숫자를 문자열로 변환

        extended_str = str_num * 10  # 반복
        compare.append([str_num, extended_str])

    # 두 숫자를 비교할 때는, 두 숫자를 연결한 경우의 크기를 비교하여 정렬
    # 숫자의 사전순 배치를 생각하기
    sorted_list = sorted(compare, key=lambda x: x[1], reverse=True)
    combined_string = ''.join([item[0] for item in sorted_list])

    # exception
    if combined_string[0] == '0':
        return "0"

    return combined_string


K, chance = map(int, input().split())
num_list = []

# 중복 배치가 가능한 회수
# K를 빼는 건, 적어도 하나의 자연수들이 배치되어야 하므로
count = chance - K

# print(K)
# print(chance)

for _ in range(K):
    num_list.append(int(input()))

# 당연히 추가로 붙는 숫자는 최댓값일 것
max_num = max(num_list)

for _ in range(count):
    num_list.append(max_num)

print(largestNumber(num_list))