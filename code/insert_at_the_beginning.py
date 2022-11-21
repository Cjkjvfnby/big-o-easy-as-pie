def reverse_list(items: list):
    """
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
