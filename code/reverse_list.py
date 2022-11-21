def reverse_list(items: list):
    """
    Return a copy of the list reversed.

    >>> reverse_list(["1", "2", "3"])
    ['3', '2', '1']
    """
    result = []
    for item in items:
        result.insert(0, item)
    return result


print(reverse_list(["1", "2", "3"]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
