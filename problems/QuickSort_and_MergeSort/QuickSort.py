def stepByStep(l1):
    quicksort(l1, 0, len(l1) - 1)

    # print(l1)


def quicksort(list, start, end):
    if end <= start:
        return
    print(l1)
    pivot = partition(list, start, end)

    quicksort(list, start, pivot - 1)
    quicksort(list, pivot + 1, end)


def partition(list, start, end):
    pivot = list[end]
    i = start - 1
    for j in range(start, end):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    i += 1
    list[i], list[end] = list[end], list[i]

    return i


# l1 = [8, 2, 5, 3, 9, 4, 7, 6, 1]
l1 = [8, 2, 4, 7, 1, 3, 9, 6, 5]
stepByStep(l1)
