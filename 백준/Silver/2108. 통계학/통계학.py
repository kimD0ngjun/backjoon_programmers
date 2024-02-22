import sys
from collections import defaultdict

# 입력 함수
def s_input():
    return sys.stdin.readline().strip()

# 입력 처리
count = int(s_input())
nums = []
frequency_map = defaultdict(int)

for _ in range(count):
    num = int(s_input())
    nums.append(num)
    frequency_map[num] += 1

sorted_nums = sorted(nums)
sorted_frequency = sorted(frequency_map, key=lambda x: (-frequency_map[x], x))

## 산술평균
average = round(sum(sorted_nums) / count)

## 중간값
median = sorted_nums[count // 2]

## 최빈값(조건부 처리)
min_frequency = sorted_frequency[0]
next_frequency = sorted_frequency[1] if len(sorted_frequency) > 1 else None

m_f_num = min_frequency

if next_frequency is None or frequency_map[min_frequency] != frequency_map[next_frequency]:
    m_f_num = min_frequency
else:
    m_f_num = next_frequency

## 범위
range_num = max(nums) - min(nums)

print(average)
print(median)
print(m_f_num)
print(range_num)
