class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #Lets a hashmap:
        #to count the frequencies

        s_hash = {}
        for letter in s:
            if letter in s_hash:
                s_hash[letter] += 1
            else:
                s_hash[letter] = 1
        #we can count how many numbers are in it by checking if it is in t 
        for i in t:
            if i not in s_hash:
                return i 
            
            s_hash[i] -= 1

            if s_hash[i] < 0:
               return i
End
ENd