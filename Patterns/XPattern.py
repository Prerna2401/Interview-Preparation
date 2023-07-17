def print_x_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

n = int(input())
print_x_pattern(n)
