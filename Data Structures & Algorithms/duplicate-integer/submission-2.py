class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for value in map.values():
            if value > 1:
                return True
        
        return False