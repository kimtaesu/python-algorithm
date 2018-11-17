import random

data = [random.randint(1, 100) for _ in range(10)]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def bubbleSort(x):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                swap(x, j, j + 1)
                swapped = True
        print(x, swapped)
    return x


print(bubbleSort(data))

# [85, 5, 27, 87, 75, 10, 26, 91, 35, 94] True
# [5, 27, 85, 75, 10, 26, 87, 35, 91, 94] True
# [5, 27, 75, 10, 26, 85, 35, 87, 91, 94] True
# [5, 27, 10, 26, 75, 35, 85, 87, 91, 94] True
# [5, 10, 26, 27, 35, 75, 85, 87, 91, 94] True
# [5, 10, 26, 27, 35, 75, 85, 87, 91, 94] False
# [5, 10, 26, 27, 35, 75, 85, 87, 91, 94]