Number = int(input("Input a Number: "))
Divisor = int(input("Input a Divisor: "))

if (Number % 4) == 0:
    print(f"Your number ({Number}) is divisible by 4")
    print(f"Your number ({Number}) is Even")
elif (Number % 2) == 0:
    print(f"Your number ({Number}) is Even")
else:
    print(f"Your number ({Number}) is Odd")

if (Number % Divisor) == 0:
    print(f"Your Number ({Number}) is divisible by your divisor ({Divisor})")
else:
    print(f"Your Number ({Number}) is not divisible by your divisor ({Divisor})")