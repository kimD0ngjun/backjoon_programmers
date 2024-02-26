class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        left_pointer = 0
        right_pointer = 0
        
        # 포인터를 옮기면서 업데이트된 합과 이전까지의 합을 비교한 최대값 산출?
        updated_sum = nums[0]
        current_sum = 0
        
        while right_pointer < len(nums): 
            # 업데이트(겸 최대값 산출)
            current_sum += nums[right_pointer]
            updated_sum = max(current_sum, updated_sum)
            
            # left_pointer가 움직이는 경우는 언제일까?
            # 일단 right_pointer의 인덱스를 넘으면 안 되겠지?
            # left_pointer가 움직였다는 건 이제까지 더한 값들에서 감산을 해야 되는 경우
            # right_pointer를 옮겨서 최대 합을 업데이트해도 추가로 left_pointer가 움직여야 한다?
            # 그를 통해서 더 최대값을 얻을 수 있다? 감산을 했는데 크기가 커진다?
            # 합이 음수네
            while current_sum < 0 and left_pointer <= right_pointer:
                current_sum -= nums[left_pointer]
                left_pointer += 1
            
            right_pointer += 1
            
        return updated_sum
            
        
        