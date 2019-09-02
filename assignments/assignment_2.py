name_list = []


def print_name_list():
    if len(name_list) < 1:
        print("-" * 15 + " LIST IS EMPTY " + "-" * 15)
        return
    print("-" * 15 + " NAME LIST " + "-" * 15)
    for name in name_list:
        if len(name) > 5 and ("n" in name or "N" in name):
            print(name + ": " + str(len(name)))
    print("-" * 41)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def add_name_to_list():
    name_list.append(input("Enter a name: "))


def empty_name_list():
    while len(name_list) > 0:
        name_list.pop()


waiting_for_input = True


while waiting_for_input:
    print("Please choose")
    print("1: Add a name")
    print("2: List names")
    print("3: Empty the list")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        add_name_to_list()
    elif user_choice == "2":
        print_name_list()
    elif user_choice == "3":
        empty_name_list()
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Wrong input, please pick a value from the list!")
else:
    print("Aborting...")
