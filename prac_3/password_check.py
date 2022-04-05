def main():

    MIN_LENGTH = 4
    password = get_password(MIN_LENGTH)

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(MIN_LENGTH):
    password = input("Enter Password with a minimum of {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Password must be above {} characters".format(MIN_LENGTH))
        password = input("Enter Password with a minimum of {} characters: ".format(MIN_LENGTH))
    return password


main()
