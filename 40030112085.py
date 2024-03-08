import pyttsx3 as pt
import os, sys


def solveProblem(n, grid):
    f = open('output.txt', 'w')
    for i in range(n):
        for j in range(n):
            if grid[i][j].lower() == 'b':
                b = [i, j]
            if grid[i][j].lower() == 'c':
                c = [i, j]

    distance = [c[0] - b[0], c[1] - b[1]]

    if distance[0] < 0:
        for i in range(distance[0], 0):
            f.write('UP\n')
    else:
        for i in range(distance[0]):
            f.write('DOWN\n')

    if distance[1] < 0:
        for i in range(distance[1], 0):
            f.write('LEFT\n')
    else:
        for i in range(distance[1]):
            f.write('RIGHT\n')


def main():
    print('Hello there.')
    pt.speak('Hello there.')
    print('Do you want me to solve this problem?')
    pt.speak('Do you want me to solve this problem?')
    answer = input('Yes or No? ')

    if answer.lower() in ['yes', 'y', 'ye', 'yeah', 'yup', 'yep', 'yea']:
        
        grid = []
        pt.speak('Enter the number of rows and columns: ')
        n = int(input('Enter the number of rows and columns: '))
        for i in range(n):
            pt.speak(f'Enter row number {str(i + 1)}')
            grid.append(list(input(f'Enter row number {str(i + 1)}: ')))
        solveProblem(n, grid)
        
        print('Do you want me to open that file or just read from it?')
        pt.speak('Do you want me to open that file or just read from it?')
        ans = input('Open or Read? ')
        if ans.lower() in ['open', 'o']:
            file = open("output.txt", "r")
            print(file.read())
            
        
        elif ans.lower() in ['read', 'r']:
            file = open("output.txt", "r")
            while True:
                content = file.readline()
                if not content:
                    break
                print(content)
                pt.speak(content)
            file.close()
            
        
        print('Finished!')
        pt.speak(' finished.')

    elif answer.lower() in ['no', 'n', 'nope', 'nah']:
        print('Understandable, have a great day!')
        pt.speak('Understandable, have a great day!')
        


if __name__ == "__main__":
    main()
