'''
def removeDuplicates(nums]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)'''
# Time O(n2)
# Space O(1)


def removeDuplicates(nums) -> int:
    if not nums:
        return 0
    
    write_index = 1  # Start from the second position
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Check if the current number is different from the previous
                nums[write_index] = nums[i]  # Place the unique element at the write_index
                write_index += 1  # Move the write_index forward
    
    return write_index  # Length of the modified list

# Time O(n)
# Space O(1)

arr = [1, 1, 2, 3, 3]
print(removeDuplicates(arr))