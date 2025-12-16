class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        if nums[0] > nums[-1]:
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if mid + 1 < len(nums):
                    if nums[mid] <= nums[mid - 1] and nums[mid] <= nums[mid +1]: 
                        index = len(nums) - mid
                        break
                else:
                    index = len(nums) - mid
                    break
                if nums[mid] >= nums[0]:
                    start = mid + 1
                else:
                    end = mid - 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            actual = mid - index
            if actual < 0:
                actual += len(nums)
            if nums[actual] == target:
                return actual
            if nums[actual] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1 
