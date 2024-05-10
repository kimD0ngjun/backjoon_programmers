class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strs = []
        nums = []

        # 문자 로그와 숫자 로그 나누기
        for log in logs:
            splited = log.split(maxsplit=1)

            if splited[1][0].isdigit():
                nums.append(splited)
            else:
                strs.append(splited)

        # 사전 순으로 재정렬
        # 아니 숫자는 상대적인 배열이면 걍 그대로 놔두라는 거네...?
        sorted_strs = sorted(strs, key=lambda s: (s[1], s[0]))

        print(sorted_strs)
        print(nums)

        result = [' '.join(inner_list) for inner_list in sorted_strs + nums]

        return result