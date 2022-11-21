a = 1  # O(1)

a += 1  # O(1)

b = [1, 2, 3]  # O(n)

b[0]  # O(1)


for x in b:  # O(n)
    print(x, end=" ")  # O(1)

min(b)  # O(n)

d = [x + 1 for x in b]  # O(n)
