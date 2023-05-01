dictionary= {
    "adam": "first man",
    "God":" Father of creation",
    "created_items":["Trees", "Land", "Sea", "Fish", "Sky"]
}


rightsideditems = dictionary.values()

converteListitems = list(rightsideditems)
converteListitems[2].append("mountain")

print(converteListitems)
# convert2list = list(leftsideditems)
# convert2list[2]


# string data from dictionary
# print(dictionary["adam"].capitalize())

# print(dictionary.values())


# for x in list(dictionary.values())[2]:
#     '''
#     The above code is saying 
#     a. I need you to loop through a dictionary values; which looks like a list
#     b. When you do i want you to explicitly convert it from a dictionary value to a list
#     c. Then i can loop through and print out the values since its now an actual list
#     '''
#     print(x)