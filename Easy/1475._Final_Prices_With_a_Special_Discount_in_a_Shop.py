class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        '''
        U - 
            Inputs: an array of integers
            Output: an array of integers with the discount applied if its eligible
            Edge Cases: 
            ith item == prices[j] where j is the min index (j > i ) and prices[j] <= prices[i]
            example = prices = [ 8, 4, 6, 2, 3]
            price[0] = 8 since j in this case is 1 which means 1 > 0 then we 8 - 4 = 4 which would make it
            4 <= 4 - [ 4, 4, 6, 2, 3]

            price[1] = 4 since j in this case is would be 3 since 4 > 2 we would then do 4 - 2 which is 2
            and so on 
            i = 0
            j = 1
            answer = []
            I first check to see if price[i] > price[j]
                if so 
                    answer.append(price[i] - price[j])
                    i += 1
                    j = i + 1
                else we add to j to check for the next one
            return answer

            answer = []

FOR each i

    discount = ?

    FOR each j after i

        if condition:

             discount = ?

             stop searching

    append final value
        P - 
        I - 
        '''

        answer = []
        for i in range(len(prices)): #constraint : 1 <= prices.length <= 500
            final_price = prices[i] #just the base price

            for j in range(i + 1, len(prices)): #iterating through the rest of prices
                if prices[j] <= prices[i]: #checking to see if this price of j <= price of i
                    final_price = prices[i] - prices[j] #applies discount if it does
                    break #break loop to go to next price of i  and to append it to the answer array

            answer.append(final_price)

        return answer