name = input('What is your name?')
birth_year = int(input('Birth year: '))
print(type(birth_year))
age = 2025- birth_year
print(type(age))
print(age)
greet = '''
Hey there!
How was your trip?

Your team.
'''
print(greet)
msg = f'{name} is {age} years old'
print(msg)
print(msg.replace('David', 'Adeoluwa'))
print('Adeoluwa' in msg)