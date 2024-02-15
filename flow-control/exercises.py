# def even_or_odd(number):
#     if number % 2 == 0:
#         print ('even')
#     else:
#         print('odd')

# def all_caps(string):
#     if len(string) > 10:
#         return string.upper()
#     else:
#         return string

def number_range(number):
    if number >= 0 and number <= 50:
        print(f'{number} is between 0 and 50')
    elif number >= 51 and number <= 100:
        print(f'{number} is between 51 and 100')
    elif number > 100:
        print(f'{number} is greater than 100')
    else:
        print(f'{number} is less than 0')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)

    


