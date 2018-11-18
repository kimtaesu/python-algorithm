## 퀵 셀렉션 (Quick Selection) 파이썬으로 구현
# 퀵 셀렉션은 리스트를 정렬하지 않고 K번째로 큰 수를 알고 싶을 때 쓰는 방법이다.
#
# 전체적인 솔루션은 퀵 정렬과 매우 유사하다, 피벗을 하나 골라서 값을 비교하면서, 피벗보다 작은 리스트, 피벗 보다 큰 리스트로 나눈다.
#
# k번째 숫자가 속해있는 리스트만 가지고 다시 재귀적으로 반복한다.
#
# median 값을 찾을 때도 활용 가능.
#
# 평균 시간복잡도는 O(n)



def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def quick_selection(arr, kth):
    pivot = arr[(len(arr) + 1) // 2 - 1]
    left, mid, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            mid.append(arr[i])

    if kth < len(left):
        print("left: ", kth, len(left))
        return quick_selection(left, kth)
    elif kth < len(left) + len(mid):
        print("mid: ", kth, len(left), len(mid))
        return mid[0]
    else:
        print("right: ", kth, len(left), len(mid))
        return quick_selection(right, kth - len(left) - len(mid))


data = [15, 111, 1, 77, 3, 7, 8]
print(quick_selection(data, 4))
