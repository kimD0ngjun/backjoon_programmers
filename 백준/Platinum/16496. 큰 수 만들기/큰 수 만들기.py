N = int(input())
nums = list(map(str, input().split()))

compare = []
for num in nums:
    extended_str = num * 10
    compare.append((num, extended_str))

sorted_list = sorted(compare, key=lambda x: x[1], reverse=True)
combined_string = ''.join([item[0] for item in sorted_list])

if combined_string[0] == '0':
    combined_string = "0"

print(combined_string)