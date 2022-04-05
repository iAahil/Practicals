"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if 90 <= score <= 100:
    print("Your score is Excellent!")
elif 50 <= score < 90:
    print("Your score is Passable")
elif 50 > score >= 0:
    print("Your score is Bad")
else:
    print("Your score is Invalid")


