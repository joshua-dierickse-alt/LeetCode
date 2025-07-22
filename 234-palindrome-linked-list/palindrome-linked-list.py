# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Palindrome Linked List
        
        head_val = head
        head_list = []
        while head_val is not None:
            head_list.append(head_val.val)
            head_val = head_val.next
        
        inverted_head = head_list[::-1]
        
        if (head_list == inverted_head):
            return(True)
        else:
            return(False)