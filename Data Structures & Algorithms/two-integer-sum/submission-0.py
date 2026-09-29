class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, e in enumerate(nums):
            if (target - e) in nums_dict:
                return [nums_dict.get(target - e), i]
            nums_dict[e] = i
        return [0,0]

        