from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    msg1=str(input("➥✪➣Add password Devi : "))
    
    print("\033[1;37;40m")

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()
    
    
    
    
    
def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()
    print("\033[1;32;40m", end = "")
    print ("\n[[ ࿇D3VI-1NS1D3࿇ ]]\n")
    e = datetime.datetime.now()
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    
os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")
print('===========================================================')
print('===========================================================')
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
emailx=str(input("➥✪➣Enter Gmail : "))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
pwx =str(input("➥✪➣P4SSW0RD  : "))
print("\033[1;37;40m")

aclass()

print("\033[1;33;40m", end = "")
msg4=str(input("➥✪➣P0ST 1D  : "))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
xxx= str(input(' Enter your name : '))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
xx= str(input('Enter hantername  : '))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
msg5=str(input("➥✪➣Enter File Abuse: "))
print("\033[1;37;40m")
f=open(msg5, 'r')

lines = f.readlines()

f.close()

print("\033[1;33;40m", end = "")
msg6= int(input("➥✪➣Put Time  : "))
print("\033[1;37;40m")

os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")
print('===========================================================')
print("[-[ ✪✿✪✿✪ TH3 T00L  CR34T3D BY D3VI INSIDE ✪✿✪✿✪ ]-]")
print('===========================================================')
print("\033[1;37;40m")

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(xxx+ ' ' +line + ' '+xx)

            print('Comm3nt G0n3 - ', xxx+ ' ' +line + ' '+xx)

            count += 1

            if count % 10 == 0:

                sleep(1)

                

                

                