# for number in range(3):
#     print("Attempt")
# print("\n")

# for number in range(3):
#     print("Attempt", number)
# print("\n")

# for x in range(3):
#     print("Attempt", x + 1)
# print("\n")

# for x in range(3):
#     print("Attempt", x + 1, (x+1) * ".")
# print("\n")

# for x in range(1,4,2):
#     print("Attempt", x, x * ".")
# print("\n")

# success = True
# for x in range(3):
#     print("Attempt")
#     if success:
#         print("Successful")
#         break
#     else:
#         print("Not successful. Try again!")
# success = False
# for x in range(3):
#     print("Attempt")
#     if success:
#         print("Successful")
#         break
# else:
#     print("Not successful. Try again!")

# for x in range(3):
#     for y in range (3):
#         print(f"These are the numbers, ({x}, {y})")

# count = 0
# for number in range(1,11):
#     if number % 2 == 0:
#         count +=1
#         print(number)
# print(f"There are {count} even numbers.")

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}. You're welcome 💖")
# greet("Asi", "Ebeheakey")
# greet("Korkor", "Ebeheakey")

# age = 32
# age +=1

# print(age)

# zeros = [0] * 10
# letters = ["a", "b", "c"]
# combined = zeros + letters
# print(combined)
# numbers = list(range(21))
# print(numbers)
# chars = list('Hello World')
# print(chars)

# numbers = list(range(20))
# print(numbers[::2])


# letters = ['a','b','c']
# for x in enumerate(letters):
#     print(x)

items = [
    ('Product1', "GHc10", '50kg'),
    ('Product2', "GHc9", '45kg'),
    ('Product3', "GHc12", '55kg')
    ]

# items.sort(key=lambda item:item[2])

# print(items)
# print(f"These are the prices and sizes available...")

# x = map(lambda item: item[1:3], items)
# for item in x:
#    print(item)

# print(f"These are the prices available...")
# prices = [item[1] for item in items]
# print(prices) 

# values = {x*2 for x in range(6)}
# print(*values)

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)

# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("You didn't enter a valid age.")
# print("Execution continues.")

# n = 55
# number_of_tries = 3
# guess = int(input("Enter an integer from 1 to 99: "))
# while True:
#     if guess < n:
#         print ("Guess is low")
#         number_of_tries = number_of_tries - 1
#         guess = int(input("Enter an integer from 1 to 99: "))
#         if number_of_tries == 0:
#             print('Game over!')
#             break
#     elif guess > n:
#         print ("Guess is high")
#         number_of_tries = number_of_tries - 1
#         guess = int(input("Enter an integer from 1 to 99: "))
#         if number_of_tries == 0:
#             print('Game over!')
#             break
#     else:
#         print ("You guessed it right!😊")
#         break

count = 0
for number in range(1, 15):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'There are {count} even numbers.')

