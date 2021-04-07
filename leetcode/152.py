class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     max_ending_here = min_ending_here = max_all = nums[0]
    #     for i in range(1, len(nums)):
    #         temp = max_ending_here
    #         max_ending_here = max(nums[i], max_ending_here * nums[i], min_ending_here * nums[i])
    #         min_ending_here = min(nums[i], temp * nums[i], min_ending_here * nums[i])
    #         max_all = max(max_all, max_ending_here)
    #     return max_all
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_product = nums[0]
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            max_product = max(product, max_product)
            if product == 0:
                product = 1
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product = product * nums[i]
            max_product = max(max_product, product)
            if product == 0:
                product = 1
        return max_product
