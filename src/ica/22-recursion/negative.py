def count_negatives(lst):
    if len(lst) == 0:
        return 0

    if lst[0] < 0:
        return 1 + count_negatives(lst[1:])
    else:
        return count_negatives(lst[1:])


