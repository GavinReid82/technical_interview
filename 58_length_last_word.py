def lengthOfLastWord(s: str) -> int:
    s_clean = s.strip().split(" ")
    return len(s_clean[-1])

# Overall Time Complexity: O(n)+O(n)+O(m)=O(n). strip/split/len. The dominant term is O(n), where n is the length of the string.

# s_clean: The split() method creates a list of words, which requires additional space proportional to the number of words and their combined lengths.
# Overall Space Complexity: O(n)