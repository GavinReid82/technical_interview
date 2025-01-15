def removeElement(nums, val) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index, arr[:write_index]

arr = [0,1,1,2,1,4,3,1]
print(removeElement(arr, 1))

'''
Time Complexity:
The loop iterates through the entire list once, so the time complexity is: O(n).

Space Complexity:
The function operates in-place, using only a few extra variables (write_index and i), so the space complexity is: O(1)
'''