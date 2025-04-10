num_of_sequence = int(input('How many sequence do you want? '))

def fibonacci_sequence(amount):
    fib = [0,1]
    for n in range(num_of_sequence-2):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    return fib

print(fibonacci_sequence(num_of_sequence))