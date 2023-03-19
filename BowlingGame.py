
import re
#this is used to create a global array for the functions to modify/read score
#First dim in array stores score and turkey if scored
#Second dim in array stores sum of first dim
frameScore =[
    [[10,8,2],[2]],     #Frame 1 
    [[5,5,10],[0]],     #Frame 2 
    [[0,0,0],[0]],     #Frame 3 
    [[0,2,0],[0]],     #Frame 4 
    [[0,2,3],[0]],     #Frame 5 
    [[0,0,0],[0]],     #Frame 6 
    [[0,0,0],[0]],     #Frame 7 
    [[0,0,0],[0]],     #Frame 8 
    [[0,0,0],[0]],     #Frame 9 
    [[0,0,0],[0]]     #Frame 10 
    ]
def TallyFrame():
    #Based off the frame passed/selected from the user loop back and update frames
    #loop through each array index and tally them independantly
    for eachFrame in range(len(frameScore)):
        frameScore[eachFrame][1] = sum(frameScore[eachFrame][0])

def clearFrames():
     #This is to clear all values from frameScore.
    #Iterate through each part of the array and set them to 0
    #This is coded using a for loop incase the number of frames changes
    for eachFrame in range(len(frameScore)):
        frameScore[eachFrame][0] = [0,0,0]
            #Call TallyFrame to clear out our sums immediately
    else:
        TallyFrame()

def scoreUpdate(score, frame):
    #This function handles when ever we want to update part of our array/Frame card
    frameScore[frame][0] = score
    #TallyFrame useage is stored here mainly as a way to insure we have finished
    #performing our calculations before passing the package off
    TallyFrame()


def goalie(pin1, pin2, pin3, frame):
    pinset =[pin1,pin2,pin3]
    print(pinset)
    for eachPin in range(len(pinset)):
        try:
            print( (re.search('[xX/]', pinset[eachPin])))
            #try to find a match, regex wont search ints and will fail
            nonNum = (re.search('[xX/]', pinset[eachPin]))
            #use regex return to figure out if it was a strike or spare entered
            if (nonNum.group() == '/'):
                print("Converting / to spare!")
                #Find the pin value for the associated frame
                #calculate the missing difference in frame value 
                spareValue = 10 - pinset[eachPin-1]
                print('spare calculated')
                pinset[eachPin] = spareValue
            if (pinset[eachPin] == 'x' or pinset[eachPin] == 'X'):
                print("Strike Detected!")
                pinset[eachPin] = 10 
                print(pinset)  
        except:

            print("No matches to convert")
            if (pinset[eachPin]>10):
                raise Exception("Illegal Score")

    print(pinset)
    #Check to see if some how the turkey shot was used illegally 
    if(pinset[2]>0 and (sum(pinset)-pinset[2])<10):
        raise Exception("Illegal Score")
    else:
        scoreUpdate(pinset, frame)

