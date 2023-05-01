# num_tries = 3
# password = 'funfilled'

# while True:
#     user_input = input('Please enter your password: ')
#     if user_input == password:
#         print('Access granted!')
#         break
#     elif user_input != password:
#         print('Access denied! Try again.')
#         num_tries = num_tries - 1
#         print(num_tries)
#         if num_tries == 0:
#             print('Device locked. Try again in 30 minutes!')
#             break

# number = 73
# number_of_tries = 3
# while True:
#     user_input = input('Please enter a number between 0 and : ')
#     if user_input) < number:
#         number_of_tries = number_of_tries - 1
#         print("Number is low!")
#         if number_of_tries == 0:
#             print("Device temporarily locked!")
#             break
#     elif int(user_input) > number:
#         number_of_tries = number_of_tries - 1
#         print("Number is high!")
#         if number_of_tries == 0:
#             print("Device temporarily locked!")
#             break
#     else:
#         print("You're correct!!")
#         break

number = 73
number_of_tries = 3

while number == 73:
    user_input = input('Guess a number between 0 and 100: ')
    if int(user_input) < number:
        print("Number is low!")
        number_of_tries = number_of_tries - 1
        if number_of_tries == 1:
            print("You have one last try!")
        if number_of_tries == 0:
            print("Game over!")
            break
    elif int(user_input) > number:
        print("Number is high!")
        number_of_tries = number_of_tries - 1
        if number_of_tries == 1:
            print("You have one last try!")
        if number_of_tries == 0:
            print("Game over!")
            break
    else:
        print("You are correct😁!!")
        break
