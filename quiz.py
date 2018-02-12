from tkinter import *
from webbrowser import open as show
from time import sleep
from itertools import islice
loginactive = False
# loginactive is False so that the login prompt will keep prompting the user if an incorrect username and/or password is entered.
answer = None
qnum = 0
tries = 3

root = Tk()

# This is the login prompt.
while loginactive != True:
    print("Enter your username")
    username = input(">>> ")
    print("Enter your password")
    password = input(">>> ")
    import csv

    print("\nPlease direct your attention to the Tk window.")

    userfile = open("users.csv","r")
    
  # The following code block searches the rows in the CSV file.
    with userfile as f:
        reader = csv.reader(f)
        for num, row in enumerate(reader):
            if username in row[0]:
                if password in row[1]:
                    loginactive = True
                    realanswer = "*"
                  # realanswer equals to * so that answer will not equal realanswer, preventing the quiz ending too early.

choice = 'Nothing yet'

def chooseMaths():
    global choice
    choice = 0
    root.destroy()
  # root.destroy() closes the Tk window, so the user doesn't have to do it manually.
def chooseComputerScience():
    global choice
    choice = 1
    root.destroy()

w = Label(root, text="Welcome to the quiz. \nYou can get a question wrong up to three times - at three, you will fail and have to retry from the start. \nChoose a topic below.")
w.pack()
m = Button(root, text="Maths", command=chooseMaths)
m.pack()
c = Button(root, text="Computer Science", command=chooseComputerScience)
c.pack()

root.mainloop()

print("\nGood luck.\n")

if choice == 0:
    choice = "m"
elif choice == 1:
    choice = "c"
else:
    try:
        exit()
    except SystemExit:
        print()

qnum = 1
while qnum < 4:
    with open(choice + "question" + str(qnum) + ".txt", "r") as q:
        firstline = q.readline()
        print(firstline)
        answer = input(">>> ")
    with open(choice + "question" + str(qnum) + ".txt") as r:
        print(r.readlines()[1:15])
        realanswer = r.readlines()[1:15]
    if any(answer in item for item in realanswer) == True:
        print("\nCorrect. Next question.\n")
        qnum = qnum + 1
    else:
        tries = tries - 1
        if tries == 1:
            tryword = "try"
        else:
            tryword = "tries"
        print("\nIncorrect! You have " + str(tries), tryword + " left!\n")
        if tries < 1:
            show("fail.jpg")
            break
if qnum > 3:
    show("win.jpg")
