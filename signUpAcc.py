#this script opens up a webdriver and signs up for hulu account
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def signUpAcc():
    driver = webdriver.Chrome('C:\\Users\\Nghia\\OneDrive\\Desktop\\chromeDriver\\chromedriver.exe')
    driver.get("https://www.hulu.com/welcome")
    signUpBottom = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/button')
    signUpBottom.click()

if __name__ == '__main__':
    signUpAcc()


