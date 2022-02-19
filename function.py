import decorations
import space

#--------------------------#   Input testing   #-------------------------------#

            
def testing(x):
    if(x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        return True
    else:
        return False



#------------------------------- GENERAL FUNCTION ------------------------------#


                                #   Display notes   #
def display():
    decorations.menu_rooms()
    num = input("zadania z ktorego pokoju chcesz zobaczyc? ")

    if(testing(num)):
        num = int(num)
    else:
        print("Nie ma takiego pokoju!")
        return

    if (num in range(1,len(space.room))):
        print("Pomieszczenie " + str(space.room[num][0].capitalize()) + ": ")
        if(len(space.room[num]) > 1):
            decorations.display_notes(num)
        else:
            print("\n\t<Brak notatek>")
    elif(num == 0):
        for i in range(1, len(space.room)):
            print("--------------\n", (space.room[i][0])+": ")
            if(len(space.room[i]) > 1):
                for y in range(1, len(space.room[i])):
                    print('\t', space.room[i][y])
            else:
                print("\n\t<Brak notatek>")
        print("--------------")
    else:
        print("\nTaki pokoj nie istnieje")
    



                                #   Add notes   #
def add():
    decorations.menu_rooms()
    num_where_add = input("do jakiego pokoju przypisac notatke? ")
    
    if(testing(num_where_add)):
        num_where_add = int(num_where_add)
    else:
        print("Nie ma takiego pokoju!")
        return

    content = input("Podaj tresc notatki: ")
    
    if(num_where_add in range(1,11)):
        space.room[num_where_add].append(content)
    elif(num_where_add == 0):
        for x in range(1, 11):
            space.room[x].append(content)
    else:
        print("Taki pokoj nie istnieje!")



                                #   Delete notes    #
def delete():
    decorations.menu_rooms()
    
    delRoom = input("Z jakiego pokoju usunac notatke? ")
    if(testing(delRoom)):
        delRoom = int(delRoom)
    else:
        print("Nie ma takiego pokoju!")
        return
        

    if (delRoom in range(1, len(space.room))):
        print("Pomieszczenie " + str(space.room[delRoom][0])+'\n')
        if (len(space.room[delRoom]) < 2):
            print("Brak notatek!")
            return
        else:
            print("\t 0 Usun wszystkie")

        decorations.display_notes(delRoom)
        
        num = input("Jaki numer ma notatka do usuniecia? ")
  
        if(testing(num)):
            num = int(num)
        else:
            print("nie ma takiej notatki!")
            return
        
        if (num in range(1,len(space.room[delRoom]))):
            del space.room[delRoom][num]
            print("usunieto pomyslnie ;)")
            
        elif(num == 0):
            certainly = input("Napewno usunac wszystkie notatki? y/n")
            if(certainly == 'y'):
                for index in range(1, len(space.room[delRoom])):
                    del space.room[delRoom][1]
            elif(certainly == 'n'):
                return
            else:
                print("Nie ma takiego wyboru!")
        else:
            print("Nie ma takiego wyboru!")
    elif(delRoom == 0):
        certainly = input("Napewno usunac wszystkie notatki? y/n")
        if(certainly == 'y'):
            for index in range(1, len(space.room)):
                for z in range(1, len(space.room[index])): 
                    del space.room[index][1]
        elif(certainly == 'n'):
            return
        else:
            print("Nie ma takiego wyboru!")
    else:
        print("taki pokoj nie istnieje!")
