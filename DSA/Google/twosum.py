class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            if (c := target - n) in d:
                return [d[c], i]
            d[n] = i
