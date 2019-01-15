# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

from math import pi
i = int(input("Enter the number of decimal places (must be less than 14): "))
h = 0
b = list()
for x in str(pi):
    h += 1
    b.append(x)
    if h == i+2:
        break

h = ''.join(b)
print(h)
