# Write Python code to print the seventh number of range(0, 25, 3)

# my_range = range(0, 25, 3)
# print(my_range[6])

# Use slicing to write Python code to print a 6-character substring of 'Launch
# School' that begins with the first c.

# string = 'Launch School'
# print(string[4:10])

# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple 
# should be in reverse order from the original. It should also exclude the 
# first and last members of the original. Result should be (4, 3, 2).

# my_tuple = (1, 2, 3, 4, 5)
# my_list = list(my_tuple)
# my_list.reverse()

# result = tuple(my_list[1:4])
# print(result)

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet'
# }

# print(pets['Dog'])
# print(pets.get('Lizard'))
# print(pets.get('Lizard', '<silence>'))

# Write Python code to replace all the : characters in the string below with +.

# info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"

# print(info.replace(':', '+'))

# Explain why the code below prints different values on lines 3 and 4.

# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))
# print(text.rfind('f', 21, 35))

# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12]
# ]

# stuff[1][3] = 606
# print(stuff)

# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             },
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             },
#         },
#     },
# }
# print(cats['Pete']['Cocoa']['enjoys'])

# numbers1 = [1, 3, 5, 7, 9, 11]
# numbers2 = []
# numbers3 = [2, 4, 6, 8]
# numbers4 = ['1', '3', '5']
# numbers5 = ['1', 3.0, '5']

# print(3 in numbers1)
# print(3 in numbers2)
# print(3 in numbers3)
# print(3 in numbers4)
# print(3 in numbers5)

# Write some code that combines the sequences into a list of tuples. Each tuple 
# should contain one member of each sequence. Print the final result so you can 
# see all the values, which should look like this:

# my_str = 'abc'
# my_list = ['Alpha', 'Bravo', 'Charlie']
# my_tuple = (None, True, False)
# my_range = range(10, 60, 10)

# zipped_iterables = zip(my_str, my_list, my_tuple, my_range)
# print(tuple(zipped_iterables))

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)