class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        1. What is the input? An array

2. What am I trying to find? indices of two numbers that add up to the target with is an interger

3. Do duplicates matter? yes because it can't be a duplicate

4. Do I need ordering? no

5. Which data structure fits best? hash map since it can count all of the duplicates so we aren't add duplicates together

6. What is my target time complexity? o(n)
'''
        #make hashmap first
        num_hash = {}
        #create the target sum - to check if it is equal to the target
        # Ex : 9 - 2 = 7 = target_s = target - indices 
        target_s = 0
        # I have to first create a for loop for the nums to be in the hash map and assign there indices
        # then start checking 
        for i, val in enumerate(nums):
            target_s = target - val
            if target_s in num_hash:
                return [num_hash[target_s], i]
            num_hash[val] = i

            

# I will check to see if the target_s is in the hash map and return the current and target_s indices
ENd