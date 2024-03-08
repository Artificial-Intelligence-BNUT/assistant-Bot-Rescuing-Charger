import pyttsx3 as pt
from typing import List

def solveProblem(n, grid: List[str]):

    answer = ""

    for i in range(n):
        if grid[i].find('b') != -1:
            bot_location = {
                "row": i,
                "col": grid[i].find('b')
            }
        if grid[i].find('c') != -1:
            charger_location = {
                "row": i,
                "col": grid[i].find('c')
            }
    
    ver_mov_counts = abs(charger_location['row'] - bot_location['row'])
    hor_mov_counts = abs(charger_location['col'] - bot_location['col'])

    ver_mov = ''
    hor_mov = ''
    if charger_location['row'] > bot_location['row']:
        ver_mov = 'DOWN\n'
    else:
        ver_mov = 'UP\n'
    if charger_location['col'] > bot_location['col']:
        hor_mov = 'RIGHT\n'
    else:
        hor_mov = 'LEFT\n'
    
    for i in range(ver_mov_counts):
        answer += str(ver_mov)
    for i in range(hor_mov_counts):
        answer += str(hor_mov)
    
    pt.speak('I solved the problem.')

    return answer

def main():
    print('Hello there.\nDo you want me to solve this problem?')
    pt.speak('Hello there.')
    pt.speak('Do you want me to solve this problem?')
    answer = input('Continue? y/n ')

    if answer.lower() == 'yes' or answer.lower() == 'y':
        pt.speak('Enter the number of cells on each row as n')
        n = input('Enter the number of cells on each row as n : ')
        while not n.isnumeric():
            pt.speak('Please enter a valid integer number : ')
            n = input('Please enter a valid integer number : ')
        while int(n) < 1:
            pt.speak('The number should be a positive integer greater than zero : ')
            n = input('The number should be a positive integer greater than zero : ')
        n = int(n)
        grid  = []
        for i in range(n):
            pt.speak('Enter the cells of this row : ')
            grid.append(input('Enter the cells of this row : '))
        
        answer = solveProblem(n, grid)
        pt.speak('Do you want me to open that file or just read from it?')
        ans = input('open or read? ')
        if ans.lower() == 'open':
            output_file = open("output.txt", 'w')
            output_file.write(answer)
            output_file.close()
        elif ans.lower() == 'read':    
            print(answer)
            pt.speak(answer)
        pt.speak(' finished.')    
        
    else:
        print('Have a good day.')
        pt.speak('Have a good day')

if __name__ == "__main__":
    main()
