def print_inverted_pyramid_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

n = int(input())
print_inverted_pyramid_pattern(n)
