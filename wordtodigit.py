digits_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

words_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
is_digit = bool
print('Welcome! What would you like?')
multiple= 1
while True:
    command = input('Digits to Words(D/d) or Words to Digits(W/w) or Exit(X/x): ').lower()
    if command == 'd':
        is_digit = True
        print("You have selected Digits to Words.")
        digits = input('Phone: ')
        output = ''
        for character in digits:
            output += digits_mapping.get(character, '!') + ' '
        print(f"Result: {output}")
    elif command == 'w':
        is_digit = False
        print("You have selected Words to Digits.")
        cmd = input("Enter the number of words do you wish to turn to digits or 'done' to exit: ")
        command = cmd.lower()
        folder = []

        while True:
            if command == '':
                cmd = input("Enter the number of words do you wish to turn to digits or 'done' to exit: ")
                command = cmd.lower()
            elif command.isnumeric():
                print(f'You wish to transcribe {cmd} word(s) to digit(s)')

                # totally unnecessary function
                # def repeat_add(times, f):
                #     for i in range(times):
                #         f()
                # def do():
                #
                #     word = input(f'Word {multiple}: ').lower()
                #     folder.append(word)
                #     print(f'Result: {folder}')
                #     display = ''
                #     for word in folder:
                #         display += words_mapping.get(word, '!')
                #     print(display)

                iteration = int(cmd)
                display = ''
                for x in range(iteration):

                    word = input(f'Word {multiple}: ').lower()
                    folder.append(word)
                    multiple += 1
                    # print(folder)
                for word in folder:
                    display += words_mapping.get(word, '!')
                print(f'Result: {display}')
                multiple = 1
                # repeat_add(iteration, do)
                break
            elif command == 'done':
                print('Goodbye!')
                break
            else:
                cmd = input("Enter the number of words do you wish to turn to digits or 'done' to exit: ")
                command = cmd.lower()
    elif command == 'x':
        print('Goodbye!')
        break