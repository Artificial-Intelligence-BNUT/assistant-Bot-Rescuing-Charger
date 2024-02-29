import pyttsx3 as pt
import os

def solveProblem(n, grid):

    path = []
    # insert your code here
    output_file = 'output.txt'
    pt.speak('I solved the problem.')

    return path

def main():
    pt.speak('Hello there.')
    pt.speak('Do you want me to solve this problem?')
    answer = input('Yes or No? ')

    if answer.lower() == 'yes':

        # insert your code here
        solveProblem(n, grid)
        pt.speak('Do you want me to open that file or just read from it?')
        ans = input('open or read? ')
        if ans.lower() == 'open':
            pass
            # insert your code here
        elif ans.lower() == 'read':    
            pass
            # insert your code here
        pt.speak(' finished.')    
        
    elif answer.lower() == 'no':
        pass
        # insert your code here
    

if __name__ == "__main__":
    main()
