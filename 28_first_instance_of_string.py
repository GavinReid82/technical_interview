def strStr(haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        return -1

a = "Gavin"
b = "My name is Gavin"

print(strStr(b, a))


# The in keyword performs a substring search. In the worst case, this involves a scan of the haystack string, leading to 𝑂(𝑛⋅𝑚) complexity
# haystack.find(needle): This operation also searches for needle in haystack, essentially repeating the substring search: 𝑂(𝑛⋅𝑚) complexity
# The in and find operations perform essentially the same work. The overall time complexity is: 𝑂(𝑛⋅𝑚)

# The function does not create additional copies of haystack or needle. No extra data structures are used. Total Space Complexity: 𝑂(1)