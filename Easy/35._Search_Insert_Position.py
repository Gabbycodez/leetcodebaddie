class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        U - 
            Input: sorted array of different integers, target value
            Output: index of target
            Edge Cases: if target were to be none then return none

        P -     set left = 0
                set right = length of nums - 1

                while left <= right:
                    calculate mid

                    if nums[mid] equals target:
                        return mid

                    else if nums[mid] is less than target:
                        move left to mid + 1

                    else:
                        move right to mid - 1

                return left
        I - 

        '''
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left