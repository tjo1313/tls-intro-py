# age = int(input("How old are you? "))
# print(f'You are {age} years old.')
# print()

# for future_age in range(10, 50, 10):
#     print(f'In {future_age} years you will be {future_age + age} years old.')

# my_list = [6, 3, 0, 11, 20, 4, 17]

# # for num in my_list:
# #     print(num)

# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# for number in my_list:
#     if number % 2 != 0:
#         print(number)

# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
#     index += 1

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# new_list = []

# for list in my_list:
#     for item in list:
#         if item % 2 == 0:
#             new_list.append('even')
#         elif item % 2 != 0:
#             new_list.append('odd')

# print(new_list)

# def find_integers(things):
#     return [
#         element for element in things
#         if type(element) is int]

# my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)

# integers = find_integers(my_tuple)
# print(integers)

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# result = {name: len(name)
#            for name in my_set
#            if len(name) % 2 != 0}

# print(result)

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
        
    return result

print(factorial(25))



