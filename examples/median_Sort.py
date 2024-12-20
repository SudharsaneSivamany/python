# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


def findMedianSortedArrays(nums1, nums2) -> None:
    sorted_num = sorted(nums1 + nums2)
    if len(sorted_num) % 2 == 1:
        print(sorted_num[int(len(sorted_num)/2)])       
    else:
        print(float((sorted_num[int(len(sorted_num)/2)] + sorted_num[int(len(sorted_num)/2 - 1)]) / 2))
findMedianSortedArrays([1,3,6,7], [2,4,5,8])