def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_list = []
    
    while list1 or list2:
        l1_index = 0
        l2_index = 0
        if list1[l1_index] <= list2[l2_index]:
            merged_list.append(list1[l1_index])
            l1_index += 1
        else:
            merged_list.append(list2[l2_index])
            l2_index += 1
    
    return merged_list
