class Solution:
    def rob(self, nums: List[int]) -> int:
        # exception
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # 처음 집을 고르면 인접 다음 집은 못 고른다
        # 만약 맨 처음의 케이스를 생각하면...
        # nums[0]과 nums[1] 중 최대값을 생각해야 한다
        nums[1] = max(nums[0], nums[1])
        
        # 인덱스 2부터 시작하기
        # nums[i]의 값 : 인덱스 i의 집 재산 훔친 합으로 업데이트
        for i in range(2, len(nums)):
            # 두 칸씩 띄운 값들 합? 혹은 한 칸만 띄운 합?
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])

        return nums[-1]