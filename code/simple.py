a = 1  # O(1)

a += 1  # O(1)

b = [1, 2, 3]  # O(n)

b[0]  # O(1)


c = [1, 2, 3]  # O(n)

for x in c:  # O(n)
    print(x, end=" ")  # O(1)

min(c)  # O(n)

d = [x + 1 for x in c]  # O(1)
