import math
number = int(input("Input Number Here: "))
print(sorted(set([item for element in range(1, int(math.sqrt(number)) + 1) if (number % element) == 0 for item in [element, number // element]])))