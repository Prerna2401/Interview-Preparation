def print_hollow_square_pattern(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

n = int(input())
print_hollow_square_pattern(n)
