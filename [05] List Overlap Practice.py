import random
a = sorted([random.randint(1, 20) for _ in range(random.randint(8, 20))])
b = sorted([random.randint(1, 20) for _ in range(random.randint(8, 20))])

print(a)
print(b)

print(sorted(list(set(a) & set(b))))