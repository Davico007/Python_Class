# to find the highest number in a list

numbers = [2,11,7,5,9,6]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)