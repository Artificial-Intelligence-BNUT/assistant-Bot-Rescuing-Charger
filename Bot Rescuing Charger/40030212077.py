import pyttsx3 as pt

def solveProblem(n, grid):

    path = []

    # پیدا کردن موقعیت های دو کاراکتر مورد نظر ما
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "b":
                bx = j
                by = i
            elif grid[i][j] == "c":
                cx = j
                cy = i
    
    # مقایسه فاصله عمودی دو کاراکتر
    while by<cy:
        by+=1
        path.append("DOWN")
    while by>cy:
        by-=1
        path.append("UP")
    # مقایسه فاصله افقی دو کاراکتر
    while bx<cx:
        bx+=1
        path.append("RIGHT")
    while bx>cx:
        bx-=1
        path.append("LEFT")

    pt.speak('I\'ve solved the problem.')

    return path

def main():
    pt.speak('Hello there.')
    pt.speak('Do you want me to solve this problem?')
    answer = input('Yes or No? ')

    if answer.lower() == 'yes':
        
        # باز کردن فایل ورودی
        pt.speak('please enter the name of text file which has the input informations')
        inFile = open(input("(Enter \"input\") ")+".txt" , "r")
        N = int(inFile.readline().strip())
        grid = [list(inFile.readline().strip()) for i in range(N)]

        # فراخوانی تابع برای حل مسئله        
        result = solveProblem(N, grid)

        # ذخیره نتیجه در فایل output
        outFile = open("output.txt", "w")
        for k in result:
            outFile.write(k+"\n")
        outFile.close()
        
        # مشاهده فایل نتیجه در ترمینال
        pt.speak('would you like to see the output?')
        ans = input('Yes or No? ')
        if ans.lower() == 'yes':
            savedOutput = open("output.txt" , "r")
            data = savedOutput.read()
            data_into_list = data.replace('\n', ' ')
            print(data_into_list) 
        elif ans.lower() == 'no':    
            pt.speak("as you wish")

        pt.speak('finished.')    
        print("End")
        
    elif answer.lower() == 'no':
        pt.speak("am i a joke to you?")
        print("End")

if __name__ == "__main__":
    main()