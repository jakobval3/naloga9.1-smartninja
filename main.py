print("This is a unit converter,it converts kilometers to miles.")

while True:
    km = input("Please enter your number of kilometers here:")

    km = km.replace(",", ".")

    miles = float(km) * 0.62

    print("{0} kilometers is {1} miles.".format(km,miles))

    question= input("Would you like to convert again? (yes/no)")

    if question.lower() != "yes":
        print("Okay, goodbye.")
        break


