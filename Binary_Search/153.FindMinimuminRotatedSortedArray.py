class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start <= end:
            mid = (start + end) // 2
            if mid + 1 < len(nums):
                if nums[mid] <= nums[mid - 1] and nums[mid] <= nums[mid +1]: 
                    return nums[mid]
            else:
                return nums[mid]
            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                end = mid - 1
