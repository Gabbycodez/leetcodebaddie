class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        What is the input? two strings
What am I trying to find? I am trying to find if both strings are anagrams
Do duplicates matter? They do 
Do I need ordering? I do not 
Which data structure fits best?
Hashmap
What is my time complexity target? o(n)
'''
        # we will be doing a frequency hash map
        # we can check if s = anagram | t = nagaram - if there are the same amount of letters in the both
        # anagram
        # nagaram
        if len(s) != len(t):
            return False

        s_hash = {}
        
        for i in s: 
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1  

        for letter in t:
            if letter not in s_hash:
                return False
            if letter in s_hash:
                s_hash[letter] -= 1

                if s_hash[letter] < 0:
                    return False
        return True
End