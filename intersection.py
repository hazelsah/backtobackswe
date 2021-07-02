class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: list of int
        :type nums2: list of int
        :rtype: list of int
        '''
        s = set()
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                s.add(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1, 2, 3, 4, 5, 6], [5, 6]))
