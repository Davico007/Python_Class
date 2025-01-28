command = ""
car_started = False
while True:
    command = input("What do you need?").lower()
    if command == "start":
        if car_started:
            print("Car is still on")
        else:
            car_started = True
            print("Car has started.")
    elif command == "stop":
        if not car_started:
            print("Car is still off")
        else:
            car_started = False
            print("Car has stopped.")
    elif command == "help":
        print("""
start - to start car
stop - to stop car
quit - to quit
        """)
    elif command == "quit":
        print("Goodbye!")
        break
    else: print("Sorry! I don't understand.")