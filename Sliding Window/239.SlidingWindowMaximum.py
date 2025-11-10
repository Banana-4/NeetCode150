import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        max_n =(left, nums[left])
        while right < k:
            if max_n[1] < nums[right]:
                max_n =(right, nums[right])
            right += 1
        heap = []
        for i in range(max_n[0], right):
            heapq.heappush(heap, (-nums[i], i))
        result = [-heap[0][0]]
        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            left += 1
            right +=1
            while heap[0][1] < left:
                heapq.heappop(heap) 
            result.append(-heap[0][0])
        return result
