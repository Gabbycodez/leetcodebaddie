class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #0 = red ; 1 = white ; 2 = blue

        left = 0
        right = 1
        max_n = 0
        
        #check if index 0 > index 1:
        count = 0


        while count < len(nums) - 1:
            count +=1
            for i in range(0,len(nums)-1):
                if nums[i] > nums[i+1]:
                    max_n = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = max_n     
        #switch it out 