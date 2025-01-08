def sum_two_on2_complexity(nums, target):
    """
    Uses brute force by using a nested loop which results in O(n^2) time.
    """
    for index_1 in range(len(nums)):
        for index_2 in range(index_1 + 1, len(nums)):
            if nums[index_2] == target - nums[index_1]:
                return [index_1, index_2]
    return []


def sum_two_on_complexity(nums, target):
    """
    To reduce time complexity to O(n) a hashmap is used for lookup.
    """
    hash_dict = {}
    for index in range(len(nums)):
        hash_dict[nums[index]] = index
    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in hash_dict and hash_dict[complement] != index:
            return [index, hash_dict[complement]]
    return []


print(f'O(n2) complexity: {sum_two_on2_complexity([1, 2, 3, 4, 5], 3)}')
print(f'Returns a empty list if no solution is found: {sum_two_on2_complexity([1, 2, 3, 4, 5], 10)}')
print(f'O(n) complexity:{sum_two_on_complexity([12, 36, 13, 41, 23], 25)}')
