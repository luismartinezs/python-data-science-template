def perimeter(length, width=None):
    if width is None:
        width = length
    return 2 * (length + width)
