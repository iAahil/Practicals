"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    it will occur when an input is anything other than an integer
2. When will a ZeroDivisionError occur?
    it will occur when the denominator is a zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    yes by adding an error checking loop
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
