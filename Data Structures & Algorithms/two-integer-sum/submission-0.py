class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevEmptyMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevEmptyMap:
                return [prevEmptyMap[diff], i]
            prevEmptyMap[val] = i
        return 0