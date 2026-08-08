from bisect import bisect_left

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        top = 0
        bottom = 0

        top_length = 0
        bottom_length = 0

        for i in range(len(nums1)):
            num_top = nums1[i]
            num_bottom = nums2[i]

            if num_top < num_bottom:
                num_top, num_bottom = num_bottom, num_top

            if num_bottom >= top:
                top = num_bottom
                bottom = num_bottom
                top_length += 1
                bottom_length += 1
            elif num_top < bottom:
                top = num_bottom
                bottom = num_bottom
                top_length = 1
                bottom_length = 1
            elif top > num_top and num_bottom >= bottom:
                top = num_bottom
                bottom = num_bottom
                top_length = 1
                bottom_length += 1
            elif num_top >= top and num_bottom >= bottom:
                top = num_top
                bottom = num_bottom
                top_length += 1
                bottom_length += 1
            elif num_top >= top and num_bottom < bottom:
                top = num_top
                bottom = num_bottom
                top_length = max(top_length, bottom_length) + 1
                bottom_length = 1
            else:
                top = num_bottom
                bottom = num_top
                top_length = 1
                bottom_length += 1
                top, bottom = bottom, top
                top_length, bottom_length = bottom_length, top_length

            result = max(result, top_length, bottom_length) 

        return result
