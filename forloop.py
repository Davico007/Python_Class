# for item in range(1,10,3):
#     print(item)
#

# to find the total price on a cart
# prices = [10,20,30]
# total = 0
# for item in prices:
#     total += item
# print(total)

# to generate a nested list like cordinates
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# to check the index of a number on a list
numbers = [2,5,7,8,9]
ges = input('''
Welcome!
To check if a number is on the list, enter the number:
''')

# old method

# included = bool
#
#
# while ges == '' or not ges.isnumeric():
#     ges = input('Please enter a non-decimal number!:')
# else:
#     guess = int(ges)
#     for item in numbers:
#
#         if guess == item:
#             included = True
#             print(f'Your number ({guess}), is on index {numbers.index(item)}.')
#             break
#         else:
#             included = False
#
#     if not included:
#         print(f'Your number ({guess}), is not on the list!')

# new method

while ges == '' or not ges.isnumeric():
    ges = input('Please enter a non-decimal number!:')
else:
    guess = int(ges)
    # print(guess)
    # print(numbers.index(guess))
    if not guess in numbers:
        print(f'Your number ({guess}), is not on the list!')
    else:
        print(f'Your number ({guess}), is on index {numbers.index(guess)}.')




#    to draw shapes with 'X' based on items on a list
# numbers = [5,2,2,5,2,2,5]
# for item in numbers:
#     output = ''
#     for y in range(item):
#         output += 'X'
#     print(output)
