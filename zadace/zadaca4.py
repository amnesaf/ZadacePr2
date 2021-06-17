import re
ime=input("Unesite ime: ")
prezime=input("Unesite prezime: ")

email="^"+ime+"."+prezime+"@fpmoz.sum.ba$"
eduid="^"+ime[0]+prezime+"([0-9]*)@sum.ba$"

while 1:
    unos1=input("Unesite email: ")
    unos2=input("Unesite eduid: ")
    regex=re.match(email,unos1)
    regex1=re.match(eduid,unos2)
    if regex and regex1:
        break
    else:
        print("Nema podudaranja")

print("Izvršeno podudaranje")
