def fizz_buzz(num):
    """
    15 is used as the divisor since the lowest common multiple of 3 and 5 is 15.
    """
    result = []
    for index in range(1, num + 1):
        if index % 15 == 0:
            result.append('FizzBuzz')
        elif index % 3 == 0:
            result.append('Fizz')
        elif index % 5 == 0:
            result.append('Buzz')
        else:
            result.append(index)
    return result


print(fizz_buzz(150))
