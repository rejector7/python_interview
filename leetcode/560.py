class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             if sum == k:
    #                 res += 1
    #     return res
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     sum_list = [0] * (len(nums) + 1)
    #     for i in range(len(nums)):
    #         sum_list[i + 1] = sum_list[i] + nums[i]
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums) + 1):
    #             if sum_list[j] - sum_list[i] == k:
    #                 res += 1
    #     return res
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum_map = {0: 1}    # {upToSum: count}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            res += sum_map.get(sum - k, 0)
            sum_map[sum] = sum_map.get(sum, 0) + 1
        return res