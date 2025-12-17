class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        if nums[0] > nums[-1]:
            start = 0
            end = len(nums) - 1
            while start <= end:
                pivot = (start + end) // 2
                if pivot + 1 < len(nums):
                    if nums[pivot] <= nums[pivot - 1] and nums[pivot] <= nums[pivot +1]: 
                        break
                else:
                    break
                if nums[pivot] >= nums[0]:
                    start = pivot + 1
                else:
                    end = pivot - 1
            if target >= nums[0]:
                start = 0
                end = pivot
            else:
                start = pivot
                end = len(nums) - 1
        else:
            start = 0
            end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1 
