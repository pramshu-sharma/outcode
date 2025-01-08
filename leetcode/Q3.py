def longest_substring_length(s):
    """
    The sliding window technique is used with left and right pointers.
    """
    char_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_substring_length('ouboibasdasddiioasdasdbbuyyqtt'))

