#this script opens up a webdriver and signs up for hulu account
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time

def hooverMouse():
    time.sleep(5)
    pyautogui.moveTo(1917, 1754, duration=0.25)
    pyautogui.leftClick()


def signUpAcc():
    driver = webdriver.Chrome('C:\\Users\\Nghia\\PycharmProjects\\HackUiowa2019\\resources\\chromedriver.exe')
    driver.get("https://www.hulu.com/welcome")
    pyautogui.moveTo(2457, 70, duration=0.25)
    pyautogui.leftClick()
    time.sleep(3)
    signUpBottom = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/button')
    signUpBottom.click()
    hooverMouse()
    time.sleep(60)


if __name__ == '__main__':
    signUpAcc()


