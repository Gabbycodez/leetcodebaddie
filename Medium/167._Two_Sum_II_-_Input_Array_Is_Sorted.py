class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1

        while start < end: # 0 , 3

            total = numbers[start] + numbers[end] # total = 2 + 15

            if total == target: 
                return [start + 1, end + 1]

            elif total < target:#17
                start += 1
            else:
                end -= 1

        return [-1, -1]
End
ENd