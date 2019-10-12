import tkinter

if __name__ == '__main__':
    print("HELLO")


def buildInterface():
    m = tkinter.Tk("Free Hulu")
    button = tkinter.Button(m, {"bg": "red"})
    m.mainloop()
