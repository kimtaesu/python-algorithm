data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[mid:]
        right_half = list[:mid]

        mergeSort(left_half)
        mergeSort(right_half)

        k = 0
        left = 0
        right = 0

        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                list[k] = left_half[left]
                left += 1
            else:
                list[k] = right_half[right]
                right += 1
            k += 1

        while left < len(left_half):
            list[k] = left_half[left]
            left += 1
            k += 1

        while right < len(right_half):
            list[k] = right_half[right]
            right += 1
            k += 1

mergeSort(data)

print(data)
