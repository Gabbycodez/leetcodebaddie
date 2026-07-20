# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #head = Node(1)
        #have to have three pointers as if we change current.next we could lose the rest of the list
        #current = 1
        #prev = none
        


        prev = None
        curr = head
        
        while curr:
            #Save next node
            next_node = curr.next
            #Reverse current pointer
            curr.next = prev
            #Move previous forward
            prev = curr
            #Move current forward
            curr = next_node
        return prev
End

ENd