numbers = []
for i in range(5):
    number = int(input("Enter Number: "))
    numbers.append(number)
average = sum(numbers) / len(numbers)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the number is {}".format(average))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
