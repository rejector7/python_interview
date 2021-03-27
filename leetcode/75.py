from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = defaultdict(int)
        for i in nums:
            if i == 0:
                colors[0] += 1
            if i == 1:
                colors[1] += 1
            if i == 2:
                colors[2] += 1

        for i in range(colors[0]):
            nums[i] = 0
        for i in range(colors[0], colors[0] + colors[1]):
            nums[i] = 1
        for i in range(colors[0] + colors[1], len(nums)):
            nums[i] = 2
        return
