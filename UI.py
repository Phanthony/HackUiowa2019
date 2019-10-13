import tkinter
from tkinter import *

testDict = {"username": "test username",
            "datecreated": "October 12, 2019",
            "timeleft": "30 Days"}


class interface:

    def __init__(self):
        m = tkinter.Tk()
        m.title("Free Hulu")
        m.geometry("700x500")

        userFrame = Frame(m, relief="sunken", borderwidth=5, padx=3, pady=3)

        self.main = m
        self.delFrame = Frame(userFrame, relief="sunken")
        self.userNameFrame = Frame(userFrame, relief="sunken")
        self.dateCreatedFrame = Frame(userFrame, relief="sunken")
        self.timeLeftFrame = Frame(userFrame, relief="sunken")
        userFrame.pack(fill="both", expand=True)

    def addAccount(self, accountDict):
        userNameFrame = self.userNameFrame
        timeLeftFrame = self.timeLeftFrame
        dateCreatedFrame = self.dateCreatedFrame

        username = accountDict["username"]
        usernameLabel = Label(userNameFrame, text=username)
        usernameLabel.pack(side="top", pady=4.2)

        dateCreated = accountDict["datecreated"]
        dateLabel = Label(dateCreatedFrame, text=dateCreated)
        dateLabel.pack(side="top", pady=4.2)

        timeLeft = accountDict["timeleft"]
        timeLabel = Label(timeLeftFrame, text=timeLeft)
        timeLabel.pack(side="top", pady=4.2)

        deleteButton = Button(self.delFrame, text="Delete Account", bg="red", fg="black",command=lambda: self.deleteAccount(usernameLabel,dateLabel,timeLabel,deleteButton))
        deleteButton.pack(side="top", pady=1.3)

    def deleteAccount(self, userLabel, dateLabel, timeLabel, button):
        userLabel.pack_forget()
        dateLabel.pack_forget()
        timeLabel.pack_forget()
        button.pack_forget()

    def buildInterface(self):
        m = self.main
        delFrame = self.delFrame
        userNameFrame = self.userNameFrame
        timeLeftFrame = self.timeLeftFrame
        dateCreatedFrame = self.dateCreatedFrame

        userNameFrame.pack(fill="both", expand=True, side="left")
        Label(userNameFrame, text="Username").pack()

        dateCreatedFrame.pack(fill="both", expand=True, side="left")
        Label(dateCreatedFrame, text="Date Created").pack()

        timeLeftFrame.pack(fill="both", expand=True, side="left")
        Label(timeLeftFrame, text="Time Left").pack()

        delFrame.pack(fill="both", expand=True, side="left")
        Label(delFrame, text=" ").pack()

        buttonFrame = Frame(m, padx=3, pady=3)
        createButton = tkinter.Button(buttonFrame, text="Create New Account", command= lambda: self.addAccount(testDict))
        createButton.pack(side="top")
        buttonFrame.pack(fill="x")

        m.mainloop()

    def f(self, f):
        print("HELLO")


if __name__ == '__main__':
    main = interface()
    main.buildInterface()
