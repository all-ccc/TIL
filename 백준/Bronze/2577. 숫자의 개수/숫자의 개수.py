a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for n in range(10):
    counts = result.count(str(n))
    print(counts)