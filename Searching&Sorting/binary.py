arr = [2, 4, 6, 1, 3, 5]
arr.sort()

def binarySearch(arr, start, end, ele):
    if start <= end:
        mid = (start + end) // 2
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            return binarySearch(arr, start, mid - 1, ele)
        else:
            return binarySearch(arr, mid + 1, end, ele)
    else:
        return -1  # Element not found

srch = int(input('Enter search element: '))
result = binarySearch(arr, 0, len(arr) - 1, srch)

if result != -1:
    print('Element found at index:', result)
else:
    print('Element not found!')
