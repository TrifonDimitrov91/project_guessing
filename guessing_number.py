
import random as rd
n = 30
number = rd.randint(0,n)
half_number = n // 2
number_of_iteration = 10

hint = {"hint1":False, "hint2":False}

while number_of_iteration > 0:

    user_input = int(input("Enter Integer: "))

    if user_input == number:
        print("\nYou got it right!")
        print(f"Number is {number}")
        print("*"*40)
        break 

    elif number_of_iteration > 5 and number_of_iteration < 9 and hint["hint1"] == False:
        if number <  half_number:
            print(f"\nHint: Number is < {half_number}")
            print("-"*40)
            number_of_iteration -= 1
            hint["hint1"] = True

        else:
            print(f"\nNumber is > {half_number}")
            number_of_iteration -= 1
            print("-"*40)
            hint["hint1"] = True

    elif number_of_iteration == 5 and hint["hint2"] == False:
        if number % 2 == 0:
            print("\nHint: Number is even")
            print("-"*40)
            hint["hint2"] == True

        else:
            print("\nNumber is odd")
            number_of_iteration -=1
            print("-"*40)
            hint["hint2"] == True


    elif number_of_iteration == 1 and number != user_input:
        print("\nGame Over!")
        print("="*40)
        number_of_iteration -= 1

    else:
        print("\nIncorrect")
        number_of_iteration -= 1
        print("_"*40)
        

