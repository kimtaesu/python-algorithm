data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def quick_sort(x, start, end):
    if start < end:
        pivot = partition(x, start, end)
        quick_sort(x, start, pivot - 1)
        quick_sort(x, start + 1, end)
    return x


def partition(x, start, end):
    pivot = end
    left = start
    wall = start

    while left < pivot:
        if x[left] < x[pivot]:
            swap(x, left, wall)
            wall += 1
        left += 1

    swap(x, wall, pivot)

    pivot = wall
    return pivot


quick_sort(data, 0, len(data) - 1)
print(data)
