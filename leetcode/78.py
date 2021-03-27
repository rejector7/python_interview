class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        pre_res = self.subsets(nums[0:len(nums) - 1])
        res = []
        for subset in pre_res:
            res.append(subset + [nums[len(nums) - 1]])
        res += pre_res
        return res