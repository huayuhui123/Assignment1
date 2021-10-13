"""
Update this module docstring with your own details
Name:YuhuiHua
Date started:2021.10.7
"""
import csv
menu="""Menu:
L - List all albums
A - Add new album
M - Mark an album as completed
Q - Quit"""
data_file = open("albums.csv","r+")
inform = [line for line in csv.reader(open("albums.csv"))]
def listout():
    name = []
    author = []
    year = []
    condition = []
    for row in inform:
        name.append(row[0])
        author.append(row[1])
        year.append(row[2])
        condition.append(row[3])
    long = len(name)
    require=0
    for i in range(1,long+1,1):
        if condition[i-1]=="r":
            print("*",end="")
            print("{}.{:<30} by {:<20}({})".format(i,name[i-1],author[i-1],year[i-1]))
            require=require+1
        else:
            print(" {}.{:<30} by {:<20}({})".format(i, name[i - 1], author[i - 1], year[i - 1]))
    print("You need to listen to {} albums".format(require))
def add():
    print(" ")
def mark():
    listout()
    print("Enter the number of an album to mark as completed")#
    m=input(">>>")
    while m.isalpha() or inform[int(float(m))-1][3]!="r":
        if m.isalpha() or int(float(m))!=float(m):
            print("Invalid input; enter a valid number")
        elif m<"0" or m=="0":
            print("Number must be > 0")
        elif int(float(m))>len(inform):
            print("Too large!The number must be under {}".format(len(inform)))
        else:
            print("You have already listened to ",(inform[int(float(m))-1][0]))
            break
        m = input(">>>")
    if inform[int(m)-1][3]=='r':
        inform[int(m)-1][3]='c'
        csv.writer(open('albums.csv','w',newline='')).writerow(inform)
        print("You listened to{}".format(inform[int(m)-1][0]))
def mainmenu():
    print("{} albums loaded".format(len(inform)))
    print(menu)
    choice = input(">>>").upper()
    while choice!="Q"and"4":
        if choice=="L"or choice=="1":
            listout()
        elif choice=="A"or choice=="2":
            add()
        elif choice=="M"or choice=="3":
            mark()
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>>").upper()
    print("{}albums saved to albums.csv".format(len(inform)))
def main():
    print("Album Tracker 1.2 - by Yuhui Hua")
    mainmenu()
    data_file.close()
main()
