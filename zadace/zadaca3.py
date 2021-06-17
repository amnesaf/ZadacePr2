import re
zamjena="^a.*[0-5].*f$"
razmak="\s"
while 1:
    string=input("Unesite string: ")
    result=re.search(zamjena,string)
    result2=re.search(razmak,string)
    if result and result2:
        break
    else:
        print("Nema podudaranja")

print("Izvršeno podudaranje")
