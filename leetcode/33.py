class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # mid = 0
        while low < high - 1:
            mid = (high - low) // 2 + low
            if nums[low] < nums[high]:
                if target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[low] < nums[mid]:
                    if nums[low] <= target <= nums[mid]:
                        high = mid
                    if nums[mid] < target:
                        low = mid + 1
                    if target < nums[low]:
                        low = mid + 1
                else:
                    if nums[mid] <= target <= nums[high]:
                        low = mid
                    if nums[mid] > target:
                        high = mid - 1
                    if target > nums[high]:
                        high = mid - 1
        # print(low, mid, high)
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        else:
            return -1