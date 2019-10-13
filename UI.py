import tkinter
from tkinter import *
from info import *
from signUpAcc import *

testDict = {"username": "test username",
            "datecreated": "October 12, 2019",
            "timeleft": "30 Days"}


class cc:

    def __init__(self):
        self.cc = ""
        self.zip = ""
        self.cvc = ""
        self.exp = ""

    def ccTester(self, Entry, Label, Button, c):
        if cardNumber(str(Entry.get())):
            Entry.pack_forget()
            Label.pack_forget()
            Button.pack_forget()
            self.cc = str(Entry.get())
            self.getCVC(c)
        else:
            Label.configure(text="Wrong Credit Card")

    def cvcTester(self, Entry, Label, Button, c):
        if cvc(str(Entry.get())):
            Entry.pack_forget()
            Label.pack_forget()
            Button.pack_forget()
            self.cc = str(Entry.get())
            self.getZip(c)
        else:
            Label.configure(text="Wrong CVC")

    def zipTester(self, Entry, Label, Button, c):
        if zip(str(Entry.get())):
            Entry.pack_forget()
            Label.pack_forget()
            Button.pack_forget()
            self.cc = str(Entry.get())
            self.getExp(c)
        else:
            Label.configure(text="Wrong Zip Code")

    def expTester(self, Entry, Label, Button, c):
        if cardExpiration(str(Entry.get())):
            Entry.pack_forget()
            Label.pack_forget()
            Button.pack_forget()
            self.cc = str(Entry.get())
            self.buildInterface(c)
        else:
            Label.configure(text="Wrong Expiration Date")

    def getCC(self):
        c = tkinter.Tk()
        ccEntry = Entry(c)
        ccEntry.pack()
        ccLabel = Label(c, text="Enter Your Credit Card")
        ccLabel.pack()


        ccButton = Button(c, text="OK", command=lambda: self.ccTester(ccEntry,ccLabel, ccButton, c))
        ccButton.pack()

        c.mainloop()

    def getCVC(self, c):
        cvcEntry = Entry(c)
        cvcEntry.pack()
        cvcLabel = Label(c, text="Enter Your CVC")
        cvcLabel.pack()

        cvcButton = Button(c, text="OK", command=lambda: self.cvcTester(cvcEntry, cvcLabel, cvcButton, c))
        cvcButton.pack()



    def getZip(self, c):
        zipEntry = Entry(c)
        zipEntry.pack()
        zipLabel = Label(c, text="Enter Your Zip Code")
        zipLabel.pack()

        zipButton = Button(c, text="OK", command=lambda: self.zipTester(zipEntry, zipLabel, zipButton, c))
        zipButton.pack()

    def getExp(self, c):
        expEntry = Entry(c)
        expEntry.pack()
        expLabel = Label(c, text="Enter Your Expiration")
        expLabel.pack()

        expButton = Button(c, text="OK", command=lambda: self.expTester(expEntry, expLabel, expButton, c))
        expButton.pack()

    def buildInterface(self, c):
        c.destroy()
        print("wat")
        main = interface(self.cc,self.cvc,self.zip,self.exp)
        main.buildInterface()


class interface:

    def __init__(self, cc, cvc, zip, exp):
        m = tkinter.Tk()
        m.title("Free Hulu")
        m.geometry("1000x700")

        userFrame = Frame(m, relief="sunken", borderwidth=5, padx=3, pady=3)

        self.cc = cc
        self.cvc = cvc
        self.zip = zip
        self.exp = exp

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
        usernameLabel.pack(side="top", pady=12)

        dateCreated = accountDict["datecreated"]
        dateLabel = Label(dateCreatedFrame, text=dateCreated)
        dateLabel.pack(side="top", pady=12)

        timeLeft = accountDict["timeleft"]
        timeLabel = Label(timeLeftFrame, text=timeLeft)
        timeLabel.pack(side="top", pady=12)

        deleteButton = Button(self.delFrame, text="Delete Account", bg="red", fg="black",command=lambda: self.deleteAccount(usernameLabel,dateLabel,timeLabel,deleteButton))
        deleteButton.pack(side="top", pady=1)

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

        buttonFrame = Frame(m)
        createButton = tkinter.Button(buttonFrame, text="Create New Account", command=lambda: self.addAccount(testDict))
        createButton.pack(side="top")
        buttonFrame.pack(fill="x")

        m.mainloop()


if __name__ == '__main__':
    test = cc()
    test.getCC()
