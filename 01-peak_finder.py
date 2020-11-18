'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

MIT 6.006 Introduction to Algorithms, Fall 2011: https://www.youtube.com/watch?v=HtSuA80QTyo


'''

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        https://github.com/kyle8998/LeetCode/blob/master/Python/find-peak-element.py
        https://leetcode.com/problems/find-peak-element/discuss/?currentPage=1&orderBy=hot&query=
        
        """
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]



