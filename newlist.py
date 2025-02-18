matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# matrix[0][1] = 20
# print(matrix[0][1])

# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5,8,3,12,7,7,7,3,3,7,3,5,8,5,8,12,5]
# numbers.append(20)
# numbers.insert(4,9)
# numbers.remove(8)
# numbers.clear()
# numbers.pop()
# print(numbers.index(7))
# print(7 in numbers)
#
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers1 = numbers
# print(numbers1)

# to remove duplicate numbers in a list
numbers = [5,8,3,12,7,7,7,3,3,7,3,5,8,5,8,12,5]
for number in numbers:
    if numbers.count(number) > 1:
        place = numbers.index(number)
        item = number
        def repeat_fun(times,f,*args):
            for i in range(times):
                f(*args)
        def do():
            numbers.remove(item)
        repeat_fun(numbers.count(number), do)

        numbers.insert(place,item)
print(numbers)