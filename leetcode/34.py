class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        if nums[low] > target or nums[high] < target:
            return [-1, -1]
        start, end = -1, -1
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] == target:
                high = mid
        if nums[low] == target:
            start = low

        low = 0
        high = len(nums) - 1
        while low < high - 1:
            mid = (high - low) // 2 + low
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] == target:
                low = mid
        if nums[high] == target:
            end = high
        else:
            if nums[low] == target:
                end = low
        return [start, end]
