def game():
    cmd = input('Welcome! What do you need?')
    cmd = cmd.lower()
    if cmd == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
        cmd = input()
        cmd = cmd.lower()
        if cmd == 'start':
            print('Car has started!')
        elif cmd == 'stop':
            print('Car has stopped!')
        elif cmd == 'quit':
            print('Goodbye!')
        else:
            print('I do not understand.')
            print('''
            Please, type a correct command.
            start - to start the car
            stop - to stop the car
            quit - to exit
            ''')
            def ask_help():
                cmd = input()
                cmd = cmd.lower()
                if cmd == 'start':
                    print('Car has started!')
                elif cmd == 'stop':
                    print('Car has stopped!')
                elif cmd == 'quit':
                    print('Goodbye!')
                else:
                    print('I do not understand.')
                    print('''
                                        Please, type a correct command.
                                        start - to start the car
                                        stop - to stop the car
                                        quit - to exit
                                        ''')
                    ask_help()
            ask_help()


    else:
        print('I do not understand')
        game()

game()