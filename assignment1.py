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
def listout():
    name = []
    author = []
    year = []
    condition = []
    data_file = open("albums.csv","r")
    file_reader = csv.reader(data_file)
    for row in file_reader:
        name.append(row[0])
        author.append(row[1])
        year.append(row[2])
        condition.append(row[3])
    long = len(name)
    for i in range(1,long+1,1):
        if condition[i-1]=="r":
            print("*",end="")
            print("{}.{:<30} by {:<20}({})".format(i,name[i-1],author[i-1],year[i-1]))
        else:
            print(" {}.{:<30} by {:<20}({})".format(i, name[i - 1], author[i - 1], year[i - 1]))
    data_file.close()
def add():
    print(" ")
def mark():
    print(" ")
def mainmenu():
    data_file = open("albums.csv", "r")
    file_reader = csv.reader(data_file)
    albumnumber = []
    for row in file_reader:
        albumnumber.append(row)
    n = len(albumnumber)
    print("{} albums loaded".format(n))
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
    data_file = open("albums.csv", "r")
    file_reader = csv.reader(data_file)
    albumnumber = []
    for row in file_reader:
        albumnumber.append(row)
    n = len(albumnumber)
    print("{}albums saved to albums.csv".format(n))
def main():
    print("Album Tracker 1.1 - by Yuhui Hua")
    mainmenu()
main()
