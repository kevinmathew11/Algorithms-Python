# 287

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

    How can we prove that at least one duplicate number must exist in nums? 
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?
'''


class Solution1:
    def findDuplicate(self, nums) -> int:
        '''
        Simple Application of Piegon Hole Principle.

        TC: O(nlogN)
        SPC: O(1) or O(n)

        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


# a=Solution1()
# print(a.findDuplicate(nums=[1,2,4,5,7,4]))


class Solution2:
    def __str__(self):
        return("I am an solution2 object")

    def findDuplicate(self, nums) -> int:
        '''
        For linear TC: we can use sets for constant look up time. 

        '''
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)


#a = Solution2()
# print(a.findDuplicate(nums=[1,2,4,5,7,4]))


class Solution3:
    '''
    Idea is to reduce the number to a Linked list -2

    TO DO:

    '''


class Solution4:
    '''
    basic math: 
    #https://leetcode.com/problems/find-the-duplicate-number/discuss/923929/PythonBasic-Math-or-Unique-method-or-Time-%3AO(n)-Space-O(1)
    '''

    def findDuplicate(self, nums) -> int:
        unique = len(set(nums)) - 1
        n=len(nums)
        try:
            return int(( sum(nums)-sum(set(nums)))/(n-unique-1))
        except:
            return "division by zero or no duplicate "  #write cases to handle these differently
nums=[1,2,3,4,5,6]
print(Solution4().findDuplicate(nums))