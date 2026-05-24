class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key_store = []
        for num in nums:
            if num in key_store:
                return True
            key_store.append(num)
        return False