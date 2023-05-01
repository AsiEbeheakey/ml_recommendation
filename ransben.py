num_tries = 3
password = "tree"

while True:
    user_input_password = input("Please enter a password: ")
    if user_input_password == password:
        print("Access granted")
        break
    elif user_input_password != password:
        print("Password is wrong. Try again.")
        num_tries = num_tries - 1
        print(num_tries)
        if num_tries == 0:
            print("Device permanently locked. Try again in 24 hours")
            break

inhouse_topping = 'mushrooms'

user_input = input('What topping would you want? ')

if user_input != inhouse_topping:
    print("That topping is not available pleasee!!!")
elif user_input == inhouse_topping:
    print('A moment please!')
