    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #U - return True if a number shows up twice 
        #else return False
        #P - Could set where a set doesn't take any duplicates
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False  END
