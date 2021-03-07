def rec_linear_sum(items):
    assert hasattr(items, "__getitem__"), "parameter [items] must be iterable"
    assert len(items), "parameter [items] must be of a non-zero length"
    if len(items) < 2:
        return items[0]
    return items[0] + rec_linear_sum(items[1:])



print(rec_linear_sum([1, 2, 3]))