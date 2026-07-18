class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #input : any integer
        #output : boolean that let us know if the integer is a palindrome
        #palindrome is something that is the read the same back and forth
        #time complexity - o(1) - I think this because i will have to keep up with numbers which means i would be storing

        #121
        #^ ^ - check if both pointers are the same then continue | if bothe pointers meet then return true
        #-121
        #^  ^ - both pointers not the same return False

        #I would say the key is to catch the difference first
        #convert this to a string to have the len
        x = str(x)
        l = 0
        r = len(x) - 1 

        while l < r :
            if x[l] != x[r]:
                return False
            l+=1
            r-=1
        return True
