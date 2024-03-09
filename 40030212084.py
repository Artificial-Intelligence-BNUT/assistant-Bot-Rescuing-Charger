import pyttsx3

# Read input
with open("map-guide.txt", 'r') as f:
    number = int(f.readline().strip())
    input_map = [list(f.readline().strip()) for _ in range(number)]


def find(N, input_m):
    # Find positions
    robot=[]
    battery=[]
    for i in range(N):
        for j in range(N):
            if input_m[i][j] == 'b':
                robot = (i, j)
            elif input_m[i][j] == 'c':
                battery = (i, j)

    actions = []
    while robot != battery:
        if robot[0] < battery[0]:
            actions.append('DOWN')
            robot = (robot[0] + 1, robot[1])
        elif robot[0] > battery[0]:
            actions.append('UP')
            robot = (robot[0] - 1, robot[1])
        elif robot[1] < battery[1]:
            actions.append('RIGHT')
            robot = (robot[0], robot[1] + 1)
        else:
            actions.append('LEFT')
            robot = (robot[0], robot[1] - 1)

    return actions


action=find(number,input_map)

# Write output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(action))

# Convert text to speech
convert = pyttsx3.init()
convert.say(' '.join(action))
convert.runAndWait()
