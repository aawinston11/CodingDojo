import random

def tosses(times):
    print "Starting the program..."
    heads = 0
    tails = 0
    for i in range(1,times+1):
        toss_result=""
        toss = random.randint(1,2)
        if toss == 1:
            heads += 1
            toss_result = "head"
        else:
            tails += 1
            toss_result = "tail"
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + toss_result + "! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "Ending the program, thank you!"
tosses(50)