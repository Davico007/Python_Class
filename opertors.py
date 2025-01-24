weight = float(input('What is your weight?'))
unit = input(f'(L)lbs or (K)kgs ?')
if unit.upper() == 'L':
    print(f'You weigh {weight * 0.45} kg')
elif unit.upper() == 'K':
    print(f'You weigh {weight / 0.45} lbs')
else:
    print('You entered the wrong unit, start again!')