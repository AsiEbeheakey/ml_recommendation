# I have a list of party guests below
party_guests = ['kofi', 'ama', 'kweku']


# Using List Indexing and slicing take each item and apply a an action called title() which will change their first letters to caps
'''
The title method .title()  does not change the list it only does a temporary action to it and returns the result but doesnt permanently change the content of the list.
Also the title can take a string with two names eg 'kofi nimako" and it will change the kofi to Kofi and nimako to Nimako.
'''
print(party_guests[0].title(), party_guests[1].title(), party_guests[2].title())


# I Want you to take the list and add a new guest to it called Ransben
party_guests.append("ransben")


# Now show me the content of my party guests
print(party_guests)



'''
We can also use a for loop to loop over the items and apply a function or action to them like below.
'''
# for item in party_guests:
#     print(item.title())

party_guests.append('asi')
print(party_guests)
print(party_guests[0].title(), party_guests[4].title(), party_guests[3].title())
party_guests.insert(0, 'korkor')
print(party_guests)
print(f'You are welcome to my party, {party_guests[0].title()}!')
party_guests.pop()
print(party_guests.pop(2))
party_guests.sort()
print(party_guests)


user_input = int(input("Give me a number: "))

if user_input % 2 == 1:
    print("Number is odd!")

else:
    print("Number is even!")


correct_guess_number = 73
number_of_tries = 5

while True:
    user_input = int(input("Guess a number between 0 and 100? "))
    if user_input == correct_guess_number:
        print("You are right!")
        break
    elif user_input <= correct_guess_number:
            print("Your number is low")
            number_of_tries = number_of_tries - 1
            print(f"You have {number_of_tries} tries left. Try again!!!")
            if number_of_tries == 0:
                print("You are out of tries!!!")
                break
    elif user_input >= correct_guess_number:
            print("Your number is high")
            number_of_tries = number_of_tries - 1
            print(f"You have {number_of_tries} tries left. Try again!!!")
            if number_of_tries == 0:
                print("You are out of tries!!!")
                break
    break

cars = ["Mazda", "Audi", "Toyota", "Ford", "Mercedes Benz"]

for car in cars:
    print(car)

print("\n")

for car in cars:
    if car[0] == "M":
        print(car)

print("\n")

for car in cars:
    if car[0:2] in "Mer":
        print(car)


