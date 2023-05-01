# from collections import Counter
# x = Counter(('geeksforgeeks'))
# for i in x.elements():
#     print(i, end = '')

# from collections import Counter
# a = [12, 12, 18, 28, 9, 0, 3, 7]
# x = Counter(a)
# # print(x)


# # for i in x.keys():
# #     print(i, ':', x[i])

# x_keys = list(x.keys())
# x_values = list(x.values())

# print(x_keys)
# print(x_values)

from collections import Counter
a = ['softlan', 'lenor', 'lenorpods', 'softlan', 'kuschelweish', 'softlan',
 'softlan', 'lenor', 'disinfectant']
x = Counter(a)
print(x)
print(*x)
print('\n')

'''
Please explain "for i in x.key():"to me
'''

for i in x.keys():
    print(i, ':', x[i])
print('\n')