class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_odd=False
        has_even=False
        for num in nums1:
            if num%2==0:
                has_even=True
            else:
                has_odd=True
        if not (has_odd and has_even):
            return True
        return True