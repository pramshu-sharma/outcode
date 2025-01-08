def product_except_num(nums):
    """
    Utilizes two arrays: prefix and suffix for calculating the products of
    elements before and after the index.

    Time complexity is O(n) as nested loops are not used.
    """
    length_of_array = len(nums)

    prefix = [1] * length_of_array
    suffix = [1] * length_of_array

    for index in range(1, length_of_array):
        prefix[index] = prefix[index - 1] * nums[index - 1]

    for index in range(length_of_array - 2, -1, -1):
        suffix[index] = suffix[index + 1] * nums[index + 1]

    result = [prefix[index] * suffix[index] for index in range(length_of_array)]

    return result


print(product_except_num([1, 2, 3, 4, 5]))
