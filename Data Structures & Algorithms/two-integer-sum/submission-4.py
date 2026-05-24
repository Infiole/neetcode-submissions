class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            ans = target - num
            try:
                return [i,nums.index(ans, i+1)]
            except ValueError:
                continue
