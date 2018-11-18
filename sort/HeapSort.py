data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def heap_sort(a):
    def siftdown(a, i, size):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l <= size - 1 and a[l] > a[i]:
            largest = l
        if r <= size - 1 and a[r] > a[largest]:
            largest = r
        if largest != i:
            swap(a, i, largest)
            siftdown(a, largest, size)

    def heapify(a, size):
        p = (size // 2) - 1
        while p >= 0:
            siftdown(a, p, size)
            p -= 1

    size = len(a)
    heapify(a, size)
    end = size - 1
    while end > 0:
        swap(a, 0, end)
        siftdown(a, 0, end)
        end -= 1


heap_sort(data)
print(data)
