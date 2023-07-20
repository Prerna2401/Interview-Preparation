arr = [int(i) for i in input().split()]
n = len(arr)
temp = [0 for i in range(n+2)]
for i in range(n):
    if arr[i] != 0:
        temp[arr[i]] += 1
for i in range(n):
    if temp[i] == 0:
        ans = i
print(ans)

#Alternate Solution
#summ = sum(arr)
#check = (n+1)*(n+2)//2
#print(check-summ)