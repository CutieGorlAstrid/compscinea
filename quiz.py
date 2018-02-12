from tkinter import *
from webbrowser import open as show
loginactive = False
# loginactive is False so that the login prompt will keep prompting the user if an incorrect username and/or password is entered.
answer = None
qnum = 1
userfile = open("users.csv","r")

root = Tk()

# This is the login prompt.
while loginactive != True:
    print("Enter your username")
    username = input(">>> ")
    print("Enter your password")
    password = input(">>> ")
    import csv
    
  # The following code block searches the rows in the CSV file.
    with userfile as f:
        reader = csv.reader(f)
        for num, row in enumerate(reader):
            if username in row[0]:
                loginactive = True
                realanswer = "*"
              # realanswer equals to * so that answer will not equal realanswer, preventing the quiz ending too early.

def chooseMaths():
    choice = 'm'
    root.destroy()
  # root.destroy() closes the Tk window, so the user doesn't have to do it manually.
def chooseComputerScience():
    choice = 'c'
    root.destroy()

w = Label(root, text="Welcome to the quiz. \nYou can get a question wrong up to three times - at three, you will fail and have to retry from the start. \nChoose a topic below.")
w.pack()
m = Button(root, text="Maths", command=chooseMaths)
m.pack()
c = Button(root, text="Computer Science", command=chooseComputerScience)
c.pack()

choice = None
root.mainloop()

print("Good luck.\n")

question = open("questions/" + choice + "question" + str(qnum) + ".txt","r")
print(question)
