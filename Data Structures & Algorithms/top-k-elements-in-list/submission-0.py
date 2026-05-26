from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] +=1
        
        result = []

        for i in range(k):
            max_key = max(count, key=count.get)
            result.append(max_key)
            count.pop(max_key)

        return result
