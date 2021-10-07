"""
Update this module docstring with your own details
Name:YuhuiHua
Date started:2021.10.7
"""
menu="""Menu:
L - List all albums
A - Add new album
M - Mark an album as completed
Q - Quit"""
def listout():
def add():
def mark():
def mainmenu():
    print(menu)
    choice = input(">>>").upper()
    while choice!="Q"or"4":
        if choice=="L"or"1":
            listout()
        elif choice=="A"or"2":
            add()
        elif choice=="M"or"3":
            mark()
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>>").upper()
    print("{}albums saved to albums.csv".format())
def main():
    print("Album Tracker 1.1 - by Yuhui Hua")
    mainmenu()
main()
