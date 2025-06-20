class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        total_len = len(merged)
        mid = total_len // 2
        
        if total_len % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0


"""
| Step | Action                                             | Result                                                     |
| ---- | -------------------------------------------------- | ---------------------------------------------------------- |
| 1    | Input arrays                                       | `nums1 = [1, 3]`, `nums2 = [2, 4]`                         |
| 2    | Merge both arrays                                  | `[1, 3] + [2, 4] = [1, 3, 2, 4]`                           |
| 3    | Sort the merged array                              | `sorted([1, 3, 2, 4]) = [1, 2, 3, 4]`                      |
| 4    | Total length of merged array                       | `total_len = 4` (even number)                              |
| 5    | Middle index                                       | `mid = total_len // 2 = 2`                                 |
| 6    | Since total\_len is even, use avg of mid-1 and mid | `median = (merged[1] + merged[2]) / 2 = (2 + 3) / 2 = 2.5` |
"""

"""
| Step | Action                                   | Result                          |
| ---- | ---------------------------------------- | ------------------------------- |
| 1    | Input arrays                             | `nums1 = [1, 2]`, `nums2 = [3]` |
| 2    | Merge both arrays                        | `[1, 2] + [3] = [1, 2, 3]`      |
| 3    | Sort the merged array                    | `sorted([1, 2, 3]) = [1, 2, 3]` |
| 4    | Total length of merged array             | `total_len = 3` (odd number)    |
| 5    | Middle index                             | `mid = total_len // 2 = 1`      |
| 6    | Since length is odd, take middle element | `median = merged[1] = 2`        |
"""
