# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    op = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            op.next = list1
            list1 = list1.next
        else:
            op.next = list2
            list2 = list2.next
        op = op.next
    op.next = list1 if list1 else list2
    return dummy.next

'''
Initialization:

Create a dummy node that acts as the head of the merged list.
Use a pointer (op) to keep track of the current node in the merged list.

Merging:

Compare the values of the nodes in list1 and list2.
Append the smaller value to the merged list and move the respective pointer (list1 or list2) forward.

Remaining Nodes:

If one of the lists is exhausted, append the remaining nodes of the other list to the merged list.

Return:

The merged list starts from dummy.next.'''