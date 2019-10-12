from bs4 import BeautifulSoup
import urllib3
from pip._vendor.distlib.compat import raw_input


def email():
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://10minutemail.com/10MinuteMail/index.html')
    soup = BeautifulSoup(r.data, 'html.parser')
    email = (soup.find_all('input')[2]['value'])
    print(email)



def password():
    password = 'Davenport563!'

def name():
    firstName = 'Tony Stark'

def cardNumber():
    creditCard = int(raw_input("Enter your credit card number : "))
    theNumber = []
    theNumber.append(creditCard)
    creditCardNumber = theNumber[0]
    lengthOfNum = len(str(creditCardNumber))
    if(lengthOfNum != 16 | lengthOfNum != 19):
        print('invalid credit card number')
        cardNumber()
    print(creditCardNumber)


def cardExpiration():
    expirationNum = int(raw_input("Enter expiration number in MMYY format :"))
    theNumber = []
    theNumber.append(expirationNum)
    numbers = theNumber[0]
    lengthOfNum = len(str(numbers))
    if(lengthOfNum != 4):
        print('invalid format, please retry again')
        cardExpiration()
    print(numbers)

def cvc():
    cvcNum = int(raw_input("Enter the cvc number :"))
    theNumber = []
    theNumber.append(cvcNum)
    numbers = theNumber[0]
    lengthOfNum = len(str(numbers))
    if(lengthOfNum != 3 | lengthOfNum != 4):
        print('invalid cvc number, try again')
        cvc()
    print(numbers)


def zip():
    zipNum = int(raw_input("Enter zipcode :"))
    theNumber = []
    theNumber.append(zipNum)
    numbers = theNumber[0]
    lengthOfNum = len(str(numbers))
    if (lengthOfNum != 5):
        print('invalid zipcode, try again')
        zip()
    print(zip)

if __name__ == '__main__':
    cardExpiration()
