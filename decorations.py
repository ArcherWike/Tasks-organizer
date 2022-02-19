import space
#############- Decoration and display functions -#########################

def ui():
    print("="*50)

def operations():
    ui()
    menu = [
        'zobacz',
        'dodaj',
        'usun',
        'wyjdz'
    ]
    for x, an in enumerate(menu):
        print("\t",x+1 , an)
    ui()

def menu_rooms():
    ui()
    for x, an in enumerate(space.room[0:11]):
        print("\t",x , an[0])
    ui()


def see_menu():
    ui()
    print("|\t\t\tMENU\t\t\t|")
    ui()


def display_notes(index):
    for y in range(1, len(space.room[index])):
        print('\t', y, (space.room[index][y]))
