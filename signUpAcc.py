#this script opens up a webdriver and signs up for hulu account
from selenium import webdriver
import pyautogui, time, os
from selenium.webdriver.common.keys import Keys


def hooverMouse():
    time.sleep(5)
    pyautogui.moveTo(1917, 1754, duration=0.25)
    pyautogui.leftClick()


def signUpAcc():
    #opens up web browser and selects plan
    dirpath = os.getcwd()
    dirpath+= "\\resources\\chromedriver.exe"
    driver = webdriver.Chrome(dirpath)
    driver.get("https://www.hulu.com/welcome")
    pyautogui.moveTo(2457, 70, duration=0.25)
    pyautogui.leftClick()
    time.sleep(3)
    signUpBottom = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/button')
    signUpBottom.click()
    hooverMouse()

    #moves mouse over to drag the scroll down
    pyautogui.moveTo(3815, 461, duration=0.25)
    pyautogui.scroll(-1000)


    #hoovers over the month button and clicks on it
    pyautogui.moveTo(1390, 616, duration=0.25)
    pyautogui.leftClick()
    pyautogui.moveTo(1612, 1024, duration=0.25)
    pyautogui.leftClick()

    #hoovers over the day button and clicks on it
    pyautogui.moveTo(1907, 610, duration=0.25)
    pyautogui.leftClick()
    pyautogui.moveTo(1883, 1108, duration=0.25)
    pyautogui.leftClick()

    #hoovers over the year button and clicks on it/scroll down
    pyautogui.moveTo(2282, 618, duration=0.25)
    pyautogui.leftClick()
    pyautogui.moveTo(2474, 730, duration=0.25)
    pyautogui.scroll(-750)
    pyautogui.moveTo(2230, 1107, duration=0.25)
    pyautogui.leftClick()

    #hoovers over gender and selects perfer not to say
    pyautogui.moveTo(1805, 894, duration=0.25)
    pyautogui.leftClick()
    pyautogui.moveTo(1577, 1184, duration=0.25)
    pyautogui.leftClick()

    #click continue
    pyautogui.moveTo(1837, 1325, duration=0.25)
    #pyautogui.leftClick()

    time.sleep(10000)




def printPosition():

    #the code below prints the x,y coordinates. Recommended display size is 1920x1080
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionString, end='')
            print('\b' * len(positionString), end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone.')




if __name__ == '__main__':
    signUpAcc()
    #printPosition()

