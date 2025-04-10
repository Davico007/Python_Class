num_of_sequence = int(input('How many sequence do you want? '))

def generate_fibonacci(amount):
    fib = [0,1]
    for n in range(num_of_sequence - 2):
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

print(genarate_fibonacci(num_of_sequence))
