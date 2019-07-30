class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p, q = m - 1, n - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[p + q + 1] = nums1[p]
                p = p - 1
            else:
                nums1[p + q + 1] = nums2[q]
                q = q - 1
        nums1[:q + 1] = nums2[:q + 1]

# 题目说明不要return ，直接将nums1的元素进行更改