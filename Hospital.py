import datetime

# function to get date and the time which we add to our files
def getdate():
    # to get date and time
    return datetime.datetime.now()

# function to ask user to pick name of patient they want
def selectname():
    name = {1: "Melisa", 2: "Mike"}
    b = {1: "patient medicine", 2: "patient diagnosis"}

    for key, value in name.items():
        # taking input of name
        print("Press", key, "for", value, "\n", end="")

    n = int(input("type here.."))

    if n > 2:
        print("error select 1 or 2")
        exit()
    else:
        return n

# function to allow the user to either log into the system or to retrieve data
def select_file_action():
    a = {1: "Log", 2: "Retrieve"}

    for key, value in a.items():
        # taking input of function that user wants to
        # do (either log or retrieve)
        print("Press", key, "for", value, "\n", end="")

    x = int(input("type here.."))

    if x > 2:
        print("error select 1 or 2")
        exit()
    else:
        return x

# function to select the action to be taken for the patient picked
def select_task():
    b = {1: "patient medicine", 2: "patient diagnosis"}

    for key, value in b.items():
        # ask user to choose between food
        # and exercise
        print("Press", key, "for", value, "\n", end="")

    y = int(input("type here.."))

    if y > 2:
        print("error select 1 or 2")
        exit()
    else:
        return y

# function to add to information or retrieve data for patient picked
def action(n, x, y):
    # condition no 1
    if n == 1 and x == 1 and y == 1:
        value = input("type here\n")

        with open("Melisa medicine.txt", "a") as Melisamedicine:

            # printing date and time
            Melisamedicine.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully added to the patient hospital files")

    # condition no 2
    elif n == 1 and x == 1 and y == 2:
        value = input("type here\n")

        # printing date and time
        with open("Melisa diagonosis.txt", "a") as Melisadiagnosis:

            # printing date and time
            Melisadiagnosis.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully added to patient files")

    # condition 3
    elif n == 2 and x == 1 and y == 1:
        value = input("type here\n")

        # printing date and time
        with open("Mike medicine.txt", "a") as Mikemedicine:

            # printing date and time
            Mikemedicine.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully added to patient files")

    # condition 4
    elif n == 2 and x == 1 and y == 2:
        value = input("type here\n")

        # printing date and time
        with open("Mike diagnosis.txt", "a") as Mikediagnosis:

            # printing date and time
            Mikediagnosis.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully added to patient files")

    # condition 5
    elif n == 1 and x == 2 and y == 1:

        # printing date and time
        with open("Melisa medicine.txt", "r") as Melisamedicine:
            a = Melisamedicine.read()
            print(a)

    # condition no 6
    elif n == 1 and x == 2 and y == 2:

        # printing date and time
        with open("Melisa diagonosis.txt", "r") as Melisadiagnosis:
            a = Melisadiagnosis.read()
            print(a)

    # condition no 7
    elif n == 2 and x == 2 and y == 1:

        # printing date and time
        with open("Mike medicine.txt", "r") as Mikemedicine:
            a = Mikemedicine.read()
            print(a)

    # condition no 8
    elif n == 2 and x == 2 and y == 2:

        # printing date and time
        with open("Mike exercise.txt", "r") as Mikediagnosis:
            a = Mikediagnosis.read()
            print(a)

# function to allow access into hospital system
def log():
    Password = input("Please enter the hospital password : ")
    while True:

        if Password == "1234":
            print("Access granted, welcome to the hospital management system")
        else:
            print("Password is incorrect, try again")
        break

# we call a;; our functions

l = log()
n = selectname()
x = select_file_action()
y = select_task()
action(n, x, y)

