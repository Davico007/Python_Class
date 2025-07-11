from playsound import playsound
from mutagen.mp3 import MP3
import time
import miniaudio

zero ="./audio-numbers/0.mp3"
one ="./audio-numbers/1.mp3"
two ="./audio-numbers/2.mp3"
three ="./audio-numbers/3.mp3"
four ="./audio-numbers/4.mp3"
five ="./audio-numbers/5.mp3"
six = "./audio-numbers/6.mp3"
seven = "./audio-numbers/7.mp3"
eight = "./audio-numbers/8.mp3"
nine = "./audio-numbers/9.mp3"
error = "./audio-numbers/error-126627.mp3"

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

sound_mapping= {
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    '0': zero
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
        sound = []
        for character in digits:

            # output += digits_mapping.get(character, '!') + ' '
            sound.append(sound_mapping.get(character, error))
        # print(f"Result: {output}")
        # print(sound)
        for x in sound:
            # playsound(x)
            file = x
            audio = MP3(file)
            length = audio.info.length
            stream = miniaudio.stream_file(file)

            with miniaudio.PlaybackDevice() as device:
                device.start(stream)
                print('playing')
                time.sleep(length)
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
                sound = []
                for x in range(iteration):

                    word = input(f'Word {multiple}: ').lower()
                    folder.append(word)
                    multiple += 1
                    # print(folder)
                for word in folder:
                    display += words_mapping.get(word, '!')
                print(f'Result: {display}')
                for num in display:
                    sound.append(sound_mapping.get(num, error))
                for x in sound:
                    playsound(x)
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