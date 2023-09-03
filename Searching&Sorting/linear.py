arr = [3,6,8,2,4,7,1]
n = len(arr)
ele = int(input('Enter search element: '))
for i in range(n):
    if arr[i] == ele:
        print('Search element ',ele,' found at index ',i)
        break
    else:
        continue
if ele not in arr:
    print('Element not found!')