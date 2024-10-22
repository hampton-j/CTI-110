# CTI 110
# P3LAB1 - Choose your own adventure
# Hampton
# 10/22/24

def main():
    print("Choose Your Own Adventure")
    print("Do you:")
    print("1. Go home")
    print("2. Check out the haunted house")
    choice = int(input())
    if choice == 1:
        go_home()
    elif choice == 2:
        check_out_the_haunted_house()




def check_out_the_haunted_house():
    print("You decide to check out the haunted house")
    print("should you go up the stairs or stay downstairs?")
    print("1. go up the stairs")
    print("2. stay downstairs")
    choice = int(input())
    if choice == 1:
        go_up_the_stairs()
    elif choice == 2:
        stay_downstairs()

def go_up_the_stairs():
    print("If you go up the stairs a man with an axe chases you")
    print("bad ending")

def stay_downstairs():
    print("If you you stay downstairs a vampire appears behind you and delivers a swift end")
    print("very bad ending")


    


def go_home():
    print("You decide to go home")
    print("But should you get some food?")
    print("1. Order Italian")
    print("2. Grab Sushi")
    choice = int(input())
    if choice == 1:
        get_italian()
    elif choice ==2:
        grab_sushi()

def get_italian():
    print("You eat the italian and gain psychic powers!🧙🧙🧙")
    print("good ending")

def grab_sushi():
    print("A demon takes over your body")
    print("Very scary ending")

# start the program 
main()


