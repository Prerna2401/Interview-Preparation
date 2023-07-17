m = int(input('Enter no. of rows: '))
n = int(input('Enter no. of columns: '))
mat = [[int(input()) for x in range(n)]for y in range(m)]
zeros = []
print(mat)
for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            zeros.append(j)
for i in range(m):
    if 0 in mat[i]:
        for j in range(n):
            mat[i][j] = 0
    else:
        for k in range(len(zeros)):
            mat[i][k] = 0
print(mat)