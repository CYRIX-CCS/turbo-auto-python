import time, sys
indent = 0
indentIncreasing = True #Whether indentation is increasing or not.

try:
    while True: #The main program loop.
        print('' *indent, end = '')
        print("**********")
        time.sleep(1) #sleep for  1 second

        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                #Change direction
                indentIncreasing = False
        else:
            #Decreasing the number of spaces:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = Tr