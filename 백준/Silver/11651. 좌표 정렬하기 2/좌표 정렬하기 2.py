"""
https://www.acmicpc.net/problem/11651
"""

# 입력 처리
N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

# print(arr)

# 병합 정렬 클래스
class Merge_sort:
    def __init__(self, array):
        self.array = array
        self.temp = [0] * len(array)  # 임시 배열

    def merge_sort(self):
        self.sort(0, len(self.array) - 1)
        return self.array

    def sort(self, low_index, high_index):
        if low_index == high_index:
            return

        middle_index = (high_index + low_index) // 2

        self.sort(low_index, middle_index)
        self.sort(middle_index + 1, high_index)
        self.merge(low_index, middle_index, high_index)

    def merge(self, low_index, middle_index, high_index):
        temp_index = 0
        left_pointer = low_index
        right_pointer = middle_index + 1

        while left_pointer <= middle_index and right_pointer <= high_index:
            # y를 기준으로 정렬하고 y가 같으면 x를 기준으로 정렬
            if (self.array[left_pointer][1] < self.array[right_pointer][1] or
                    (self.array[left_pointer][1] == self.array[right_pointer][1] and
                     self.array[left_pointer][0] <= self.array[right_pointer][0])):
                self.temp[temp_index] = self.array[left_pointer]
                temp_index += 1
                left_pointer += 1

            else:
                self.temp[temp_index] = self.array[right_pointer]
                temp_index += 1
                right_pointer += 1

        while left_pointer <= middle_index:
            self.temp[temp_index] = self.array[left_pointer]
            temp_index += 1
            left_pointer += 1

        while right_pointer <= high_index:
            self.temp[temp_index] = self.array[right_pointer]
            temp_index += 1
            right_pointer += 1

        for i in range(temp_index):
            self.array[low_index + i] = self.temp[i]

# 연산
merge_sorter = Merge_sort(arr)
sorted_arr = merge_sorter.merge_sort()

# 출력
for x, y in sorted_arr:
    print(x, y)