class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(arr)):
            complement = target - arr[i]

            if complement in map:
                return [map[complement], i]

            map[arr[i]] = i