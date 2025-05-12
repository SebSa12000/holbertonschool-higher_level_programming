def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise. If the tuples are of different lengths,
    the shorter one is padded with zeros.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple containing the sum of the elements.
    """
    # Ensure both tuples have at least 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    return a[0] + b[0], a[1] + b[1]
