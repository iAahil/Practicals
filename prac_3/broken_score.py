"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():

    score = float(input("Enter score: "))
    return_result(score)
    print(return_result(score))


def return_result(score):
    if 90 <= score <= 100:
        return "Your score is excellent"
    elif 50 <= score < 90:
        return "Your score is passable"
    elif 50 > score >= 0:
        return "Your score is bad"
    else:
        return "Your score is invalid"

main()

print(random.randint(0,100))

