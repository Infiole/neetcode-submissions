class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            sorted_string = ''.join(sorted(str))
            result[sorted_string].append(str)
        return list(result.values())
