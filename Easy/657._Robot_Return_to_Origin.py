class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        '''
        U - Input: string that represents the move sequence - valid moves are 'R', 'L', 'U', and 'D'
            output: 
            edge cases: if empty return True, if the moves are lower case return False,
            if any moves are not valid pass it 
        P - I can set each move to be a number
        if R : +=1
        if L : -1
        if U: +=1 
        if D : -1
        example: UD - add 1 the subtract 1 = 0 as long as the end result is zero then we return True
        example : LL - add 1 add 1 = 2 and the result is 2 we return False
        if not moves:
            return False
        
        result = 0 
        for i in moves:
            match i to the case example: U
            add to result 
        if result == 0 :
            return True
        return False
        I - 
        '''

        result_v = 0
        result_h = 0

        for move in moves:
            if move == 'R':
                result_h += 1
            elif move == 'L':
                result_h -= 1
            elif move == 'U':
                result_v += 1
            elif move == 'D':
                result_v -= 1

        return (result_h, result_v) == (0, 0)

End

ENd