import os
import pyttsx3

def found_batry(N,input_array):
    action = []
    robot = None
    battery = None

    for i in range(N):
        for j in range(N):
            if input_array[i][j] == 'b':
                robot = (i, j)
            elif input_array[i][j] == 'c':
                battery = (i, j)

    while robot != battery:
        if robot[0] < battery[0]:
            action.append('DOWN')
            robot = (robot[0]+1, robot[1])
        elif robot[0] > battery[0]:
            action.append('UP')
            robot = (robot[0]-1, robot[1])
        elif robot[1] < battery[1]:
            action.append('RIGHT')
            robot = (robot[0], robot[1]+1)
        else:
            action.append('LEFT')
            robot = (robot[0], robot[1]-1)

    return action



# Getting input from the user
while True:
    N = int(input("Enter a number : "))
    if N > 100:
        print("Number is greater than 100. Please try again.")
        N = int(input("Enter a number : "))
    else:
        break

# Getting map from the user (enter empty line to stop loop)
input_array = []
for x in range(N):
    line = str(input("Enter your map : "))
    input_array.append(line)

  
action = found_batry(N,input_array)

with open('output.txt', 'w') as f:
    f.write('\n'.join(action))
    
e = pyttsx3.init()
e.say(' '.join(action))
e.runAndWait()