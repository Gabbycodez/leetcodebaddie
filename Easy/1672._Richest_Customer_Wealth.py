class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        '''
        U - input: a matrix called accounts
        output: integer that is the max wealth 

        P - 
        We check each accounts[i][i] to and add the sum of it to a list then compare it to the last recorded max and see if that is the new max
        curr_sum = 0
        max_sum = 0
        for c in accounts:
            for m in accounts[c]:
                curr_sum += m
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 0

        I - 
        '''
        curr_sum = 0
        max_sum = 0
        for c in accounts:
            for m in c:
                curr_sum += m
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 0
        return max_sum
End