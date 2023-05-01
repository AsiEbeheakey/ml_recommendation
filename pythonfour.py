# dictionary = {
#     "wood": "wawa",
#     "description": ["apotracheal","diffuse porous", "tyloses"],
#     "uses":["furniture", "flooring", "moulding"]
# }

# # dictionary["colour"] ="white"

# dictionary['colour'] = ['white','yellowish']

# # print(dictionary)

# print(f"{dictionary['description'][2].title()} resemble water bubbles.")
# print('\n')

# print(f"{dictionary['wood'].title()} is used as {dictionary['uses'][1]} material.")

# for x in dictionary['uses']:
#     print(x)
   
#     print(f"{dictionary['wood'].title()} can be used as {x}.")

person={
    'first_name':'Asi',
    'last_name':'Ebeheakey',
    'age':30,
    'city':['Accra', 'Sefwi Wiawso']
}

'''
# We want to print a sentence that says the ff:
# Asi Ebeheakey is 30 and she stays in both Accra and Sefwi

# print(f"{person['first_name']} likes bananas.")
# for x in person['city']:
#     print(f"{person['first_name']} stays in {x}.")

#Add an empty space #''# which will separate first_name from last_name after printing.
'''

fullname = person['first_name'] + ' ' + person['last_name']
age = person["age"]
#Convert dictionary list to actual list as in 'city': ['Accra', 'Sefwi Wiawso'] is a dictionary list. 
#By defining #city = list(person['city'])#, it has been converted to an actual list which can be indexed. 
city = list(person["city"])
Accra = city[0]
sefwi = city[1]

print(f"{fullname} is {age} and she stays in both {Accra} and {sefwi}")