import random
a = sorted([random.randint(1, 20) for _ in range(random.randint(8, 20))])
print(f"Randomly Generated List: {a}")
print(f"Even Numbers: {[even for even in a if even % 2 == 0]}")
print(f"Odd Numbers: {[odd for odd in a if odd % 2 != 0]}")