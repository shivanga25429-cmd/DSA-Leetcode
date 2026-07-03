class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to start the result list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Continue as long as there are nodes to process or a carry remains
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if the list has ended
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = v1 + v2 + carry
            carry = total // 10
            
            # Create a new node with the single digit result
            curr.next = ListNode(total % 10)
            
            # Move pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next