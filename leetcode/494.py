class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        pre_map = {nums[0]: 1, -nums[0]: 1}
        if nums[0] == 0:
            pre_map = {0: 2}
        s_map = {}
        for i in range(1, len(nums)):
            s_map = {}
            for s in list(pre_map.keys()):
                s_map[s + nums[i]] = pre_map.get(s) + s_map.get(s + nums[i], 0)
                s_map[s - nums[i]] = pre_map.get(s) + s_map.get(s - nums[i], 0)
            pre_map = s_map
        return pre_map.get(S, 0)


