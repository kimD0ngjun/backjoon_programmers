index = int(input())

# 초기값 및 결과 설정
value = 666

# brute force
# 범위를 강제 한정
while index != 0:
    str_value = str(value)

    if "666" in str_value:
        index -= 1

    value += 1

# if문 조건 거치든 안 거치든 무조건 +1
# 그래서 -1하고 출력
print(value - 1)

# index = int(input())
# 
# # 초기값 및 결과 설정
# count = 0
# value = 666
# 
# # brute force
# while count is not index:
#     str_value = str(value)
# 
#     if "666" in str_value:
#         count += 1
# 
#     value += 1
# 
# print(value - 1)
