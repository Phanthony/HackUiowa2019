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
    print(len(str(creditCard)))


def cardExpiration(expirationNum):
    if(len(str(expirationNum)) != 4):
        print('invalid format, please retry again')
    print(len(str(expirationNum)))

def cvc(cvcNum):
    print(len(str(cvcNum)))
    if(len(str(cvcNum)) != 3 | len(str(cvcNum)) != 4):
        print('invalid cvc number, try again')
    print(len(str(cvcNum)))


def zip(zipNum):
    if (len(str(zipNum)) != 5):
        print('invalid zipcode, try again')
    print(len(str(zipNum)))
if __name__ == '__main__':
    cvc()
