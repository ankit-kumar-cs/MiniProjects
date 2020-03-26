#namaskar dosto I am ankit bishnoi and this is my first milestone project
#please read the instructions carefully
#definitions of all the functions
def rule():
    print("In the begining of the game you will be asked for your name and your friend's name")
    print("One player can insert only one value at a time")
    print("\n DO NOT EXCEED THE INDEX VALUE")
    print("\nIF YOUR VALUES MATCH IN THE ROW WISE OR COLUMN WISE OR DIAGONALLY THEN YOU ARE THE WINNER")
    print("The interface of the game will be like this:")
    print("!  0  !  1  !  2  !\n!  3  !  4  !  5  !\n!  6  !  7  !  8  !")
    print("Given integers are the Index values you will have to select a value from them")
    print("At every step i will ask you for enter a index number And I request you to Enter that index number that is not used before")
def start_game(a,b):
    rule()
    l=[0,0,0,0,0,0,0,0,0]
    while True:
        i=int(input(f"{a}'s Turn:"))
        if l[i]==0:
            l[i]='X'
        else:
            print("Already Entered Value Cannot Be Updated\n")
            i=int(input(f"{a}'s Turn:"))
            if l[i]==0:
                l[i]='X'
            else:
                print("Already Entered\n")
                break
        print("\n")
        print("!-----------!\n")
        print(f"!  {l[0]}  {l[1]}  {l[2]}  !\n")
        print(f"!  {l[3]}  {l[4]}  {l[5]}  !\n")
        print(f"!  {l[6]}  {l[7]}  {l[8]}  !\n")
        print("!-----------!\n")

        j=int(input(f"{b}'s Turn:"))
        if l[j]==0:
            l[j]='*'
        else:
            print("Already Entered Value Cannot Be Updated\n")
            j=int(input(f"{b}'s Turn:"))
            if l[j]==0:
                l[j]='*'
            else:
                print("Already Entered\n")
                break
        print("\n")
        print("!-----------!\n")
        print(f"!  {l[0]}  {l[1]}  {l[2]}  !\n")
        print(f"!  {l[3]}  {l[4]}  {l[5]}  !\n")
        print(f"!  {l[6]}  {l[7]}  {l[8]}  !\n")
        print("!-----------!\n")
        if l[0]!=0:
            if ((l[0]==l[1] and l[0]==l[2]) or (l[0]==l[3] and l[0]==l[6])):
                if(l[0]=='X'):
                    print(f"\nCongrats {a} You Win")
                    break
                else:
                    print(f"\n Congrats {b} You Win")
                    break
        if l[8]!=0:
            if ((l[8]==l[7] and l[8]==l[6]) or (l[8]==l[5] and l[8]==l[2])):
                if(l[8]=='X'):
                    print(f"\nCongrats {a} You Win")
                    break
                else:
                    print(f"\n Congrats {b} You Win")
                    break
        if l[4]!=0:
            if ((l[4]==l[0] and l[4]==l[8]) or (l[4]==l[5] and l[4]==l[3]) or (l[4]==l[2] and l[4]==l[6]) or (l[4]==l[1] and l[4]==l[7])):
                if(l[4]=='X'):
                    print(f"\nCongrats {a} You Win")
                    break
                else:
                    print(f"\n Congrats {b} You Win")
                    break
        if (l[0]!=0 and l[1]!=0 and l[2]!=0 and l[3]!=0 and l[4]!=0 and l[5]!=0 and l[6]!=0 and l[7]!=0 and l[8]!=0):
            print("\nSorry NO one is the winner Match is Draw")
            break
start_game(input("Enter your name:"),input("Enter your friend's name:"))
