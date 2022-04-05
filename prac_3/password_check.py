MIN_LENGTH = 4
password = input("Enter Password with a minimum of {} characters: ". format(MIN_LENGTH))
while len(password) < MIN_LENGTH:
    print("Password must be above {} characters" .format(MIN_LENGTH))
    password = input("Enter Password with a minimum of {} characters: ". format(MIN_LENGTH))

print("*" * len(password))
