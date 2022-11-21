def my_max(items: list):
    """
    >>> my_max([1, 2, 3])
    3
    """
    return sorted(items)[-1]


print(my_max([1, 2, 3]))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
