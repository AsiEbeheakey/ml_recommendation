wishlist = [['ransbern', 'jesse', 'kofi'], ['waakye', 'jollof', 'banku'], '0266466868']
attendee = wishlist[0][0]
food = wishlist [1][2]
phone_number = wishlist[2]
print(f"{attendee.title()} prefers {food}. You can reach him on {phone_number}.")
dimensions = (200,50)
print ('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

print("\n")

buffet = ['rice', 'banku', 'plantain', 'beans']
for dish in buffet:
    print(f"{dish.title()} is available")

print("\n")

for dish in buffet:
    if dish == 'rice':
        print(dish.upper())
    else:
        print(dish.title())