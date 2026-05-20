class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #define our variables
        slow, fast = head, head  #both pointers start at the head

        while fast and fast.next: #check if fast don't equal to none and fast next value don't equal to none
            slow = slow.next #iterates once
            fast = fast.next.next #iterates twice

            if slow == fast:
                break # stop once they equal
        else:
            return None
        
        start = head

        while start != fast:
            start = start.next
            fast = fast.next
        return start