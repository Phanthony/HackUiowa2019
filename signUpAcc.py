#this script opens up a webdriver and signs up for hulu account
from selenium import webdriver
import pyautogui, time, os
from selenium.webdriver.common.keys import Keys

def signUpAcc():
    #opens up web browser and selects plan
    dirpath = os.getcwd()
    dirpath+= "\\resources\\chromedriver.exe"
    driver = webdriver.Chrome(dirpath)
    driver.get("https://www.hulu.com/welcome")
    pyautogui.leftClick()
    time.sleep(2)
    signUpBottom = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/button')
    signUpBottom.click()
    time.sleep(3)
    selectButton = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/form/div/div/div[2]/section/div/div[1]/div[1]/div/div/div[2]/button")
    selectButton.click()
    time.sleep(2)
    month = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/form/div[2]/div[4]/div[2]/div[2]")
    month.send_keys("march")

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

