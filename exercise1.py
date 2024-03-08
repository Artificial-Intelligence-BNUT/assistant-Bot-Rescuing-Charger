import pyttsx3 as pt
import random

def solveProblem(n):
    
    rows, cols = (n, n)
    arr = [[] for _ in range(rows)]
    for i in range(cols):
        arr[i] = ['-' for _ in range(cols)]

    bot_y, bot_x = (0, 0)
    battery_y, battery_x = (0, 0)
    while (bot_x == battery_x and bot_y == battery_y):
        bot_y = random.randint(0, n - 1)
        bot_x = random.randint(0, n - 1)
        battery_y = random.randint(0, n - 1)
        battery_x = random.randint(0, n - 1)

    arr[bot_y][bot_x] = 'b'
    arr[battery_y][battery_x] = 'c'

    print("The Battery and the Robot are placed in the Matrix like This: ")
    for i in range(rows):
        print(arr[i])

    y = battery_y - bot_y
    x = battery_x - bot_x

    f = open("output.txt", "x")
    f.close()
    f = open("output.txt", "w")

    if (y < 0):
        for t in range(-1 * y):
            print("Up")
            f.write("Up")
    else:
        for t in range(y):
            print("Down")
            f.write("Down")

    if (x < 0):
        for t in range(-1 * x):
            print("Left")
            f.write("Left")
    else:
        for t in range(x):
            print("Right")
            f.write("Right")

    pt.speak('I solved the problem.')


def main():
    pt.speak('Hello there.')
    pt.speak('Do you want me to solve this problem?')
    answer = input('Yes or No? ')

    if answer.lower() == 'yes':

        pt.speak('Please enter the square web size')
        n = int(input('Please enter the square web size: '))
        solveProblem(n)
        pt.speak('Do you want me to open that file or just read from it?')
        ans = input('open or read? ')
        if ans.lower() == 'open':
            pass
            f = open("output.txt", "r")

        elif ans.lower() == 'read':
            pass
            f = open("output.txt", "r")
            print(f.read())
            
        pt.speak(' finished.')

    elif answer.lower() == 'no':
        pass
        pt.speak('Maybe we can work together some other time!')
        print("Maybe we can work together some other time!")


if __name__ == "__main__":
    main()
