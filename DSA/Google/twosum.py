class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            if (c := target - n) in d:
                return [d[c], i]
            d[n] = i



"""
Index (i)   n (nums[i])   Complement (c = target - n)   Is c in d?   Dictionary (d)
-------------------------------------------------------------------------------
   0             2                  7                      No         {2: 0}
   1             7                  2                     Yes         {2: 0, 7: 1}
                                                    🔁 Found match: d[2] = 0
                                                    ✅ Return [0, 1]
"""
