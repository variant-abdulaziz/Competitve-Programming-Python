# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        temp = result_head = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
        
        
        while list1:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
        while list2:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                
        return result_head.next