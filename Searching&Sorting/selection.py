'''
Select minimums and swap
Best,Worst,Average case time complexity - O(n^2)
'''
arr = [6,2,5,1,4,3]
n = len(arr)
for i in range(n):
    mini = i
    for j in range(i+1,n):
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
print(arr)