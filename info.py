from bs4 import BeautifulSoup
import urllib3


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
if __name__ == '__main__':
    print(email())
