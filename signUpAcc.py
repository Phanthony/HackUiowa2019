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
    driver = webdriver.Chrome('C:\\Users\\Nghia\\PycharmProjects\\HackUiowa2019\\resources\\chromedriver.exe')
    driver.get("https://www.hulu.com/welcome")
    pyautogui.moveTo(2457, 70, duration=0.25)
    pyautogui.leftClick()
    time.sleep(3)
    signUpBottom = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/button')
    signUpBottom.click()
    hooverMouse()

    #moves mouse over to drag the scroll down
    pyautogui.scroll(-15, x=3815, y=461)
    #pyautogui.dragTo(3815, 461, 3, button='left')


    #hoovers over the month button and clicks on it
    #pyautogui.moveTo(1457, 1675, duration=0.25)
    #pyautogui.leftClick()
    #pyautogui.moveTo(1492, 2031, duration=0.25)
    #pyautogui.leftClick()

    #hoovers over the day button and clicks on it
    #pyautogui.moveTo(1978, 1681, duration=0.25)
    #pyautogui.leftClick()
    #pyautogui.moveTo(1974, 1439, duration=0.25)
    #pyautogui.leftClick()

    #hoovers over the year button and clicks on it
    #pyautogui.moveTo(2225, 1323, duration=0.25)
    #pyautogui.leftClick()
    #pyautogui.moveTo(2259, 1767, duration=0.25)
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

