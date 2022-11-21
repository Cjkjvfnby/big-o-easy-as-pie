def min_values(items: list):
    """
    >>> min_values([1, 1, 2, 3])
    2
    """
    result = 0
    for item in items:
        if item == min(items):
            result += 1
    return result


print(min_values([1, 1, 2, 3]))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
