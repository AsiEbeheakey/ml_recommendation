magicians = ['david', 'james', 'veriana']
for magician in magicians:
    print(f"Hello, {magician.title()}")
    print(f"{magician.title()}, that was an interesting trick!")
    print(f"I can't wait for the next one, {magician.title()}.\n")
print("Thank you for a great show!.\n")
pets = ['cat', 'dog', 'fish']
for pet in pets:
    print(f"I have a {pet.title()} as a pet")
    print(f"I love my {pet}!.\n")

for value in range(1,6):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2, 15, 2))
print(even_numbers)

players = ['jet', 'fii', 'kool', 'del']
print(players[0:3])
print(players[:3])
print(players[-3:])
print("These are the players on my team:")
for player in players:
    print(player.title())
players.append('mimi')
print(players)
