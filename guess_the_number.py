import sys
import random
sys.stdout.buffer.write(b'Please enter the minimum number, n.\n')
sys.stdout.flush()
n = sys.stdin.buffer.readline()
sys.stdout.buffer.write(b'Please enter the maximum number, m.\n')
sys.stdout.flush()
m = sys.stdin.buffer.readline()

random_number = random.randint(int(n), int(m))

while True:
    sys.stdout.buffer.write(b'Please enter a number between n and m.\n')
    sys.stdout.flush()
    guess = sys.stdin.buffer.readline()
    if random_number == int(guess):
        sys.stdout.buffer.write(b'Congratulations! You guessed correctly.\n')
        sys.stdout.flush()
        break
    else:
        sys.stdout.buffer.write(b'Please try again.\n')
        sys.stdout.flush()
