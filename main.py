import os
import function
import decorations

#####################- #Main loop -######################################

run = True

decorations.ui()
print("\n\tWITAJ W PROGRAMIE NOTATNIK WOŹNEGO\n")


        #Main loop
while(run):
    decorations.operations()
    option = input("\n\t\t >> Co chcesz zrobic? ")
    
    if(option == '1'):
        os.system('CLS')
        function.display()
    elif(option == '2'):
        os.system('CLS')
        function.add()
    elif (option == '3'):
        os.system('CLS')
        function.delete()
    elif (option == '4'):
        print("Papa! Milego dnia!")
        run = False
    else:
        print("nie ma takiego wyboru!")

