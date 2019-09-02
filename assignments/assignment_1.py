name = input("Enter your name: ")
age = int(input("Enter your age: "))


def my_data():
    """ Prints the data user entered about himself """
    print(name + " " + str(age))


def print_any(a, b):
    """ Prints any data user enters """
    print(str(a) + " " + str(b))


def decades_lived(age):
    """ Calculates how much decades you lived
    
        :age: Enter how old you are
     """
    return age // 10


my_data()
print_any("Pero", 14)
print("I have lived for " + str(decades_lived(age)) + " decades")
