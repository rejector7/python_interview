class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums) - 1, 0
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end > start else 0

# using stack