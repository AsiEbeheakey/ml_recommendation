'''
Generate a password
How long should the password be?
How many characters?
Should it have both uppercase and lowercase?
Should it have numbers and special characters?
'''
import string
import random

def randompasswordgen(size=10, chars=string.ascii_uppercase + 
                      string.ascii_lowercase+string.digits+string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))
print(randompasswordgen().upper())