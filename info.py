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

def cardNumber(creditCard):
    if(len(str(creditCard)) != 16 | len(str(creditCard)) != 19):
        print('invalid credit card number')
        return(False)
    return(True)


def cardExpiration(expirationNum):
    if(len(str(expirationNum)) != 4):
        print('invalid format, please retry again')
        return(False)
    return(True)

def cvc(cvcNum):
    if(len(str(cvcNum)) == 3 or len(str(cvcNum)) == 4):
        return(True)

    print('invalid cvc number, try again')
    return(False)


def zip(zipNum):
    if (len(str(zipNum)) != 5):
        print('invalid zipcode, try again')
        return(False)
    return(True)

if __name__ == '__main__':
    cvc()
