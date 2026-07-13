class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #count letters by using a dictionary
        m_dict = {}
        for val in magazine:
            if val not in m_dict:
                m_dict[val] = 1
            else:
                m_dict[val] +=1
        for i in ransomNote:
            if i not in m_dict or m_dict[i] == 0:
                return False
            m_dict[i] -=1
        return True



        
        ENd