class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        ret_list = []
        l, r = 1, k
        list_heap = []
        for i in range(k):
            list_heap.append((nums[i], i))
        heapq.heapify_max(list_heap)
        ret_list.append(list_heap[0][0])
        while r < len(nums):
            heapq.heappush_max(list_heap, (nums[r], r))
            while list_heap[0][1] < l:
                heapq.heappop_max(list_heap)
            ret_list.append(list_heap[0][0])
            l += 1
            r += 1
        return ret_list
            
        