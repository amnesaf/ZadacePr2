import random
def random_ocjena():
    return random.randint(1,5)

studenti=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

ukupni_broj=len(studenti)

broj_studenata={}

for ime in studenti:
    broj_studenata[ime]=0

for ime in studenti:
    if ime in broj_studenata:
        broj_studenata[ime]+=1
    else:
        broj_studenata[ime]=1

imena_studenata=[]
kljucevi=broj_studenata.keys()
for ime in kljucevi:
    imena_studenata.append(ime)

ocjene={}
jedinice=0
dvice=0
trice=0
cetvrtice=0
petice=0
pozitivne=0

for ime in imena_studenata:
    for i in range(broj_studenata[ime]):
        ocjene[ime+str(i+1)]=random_ocjena()
        if ocjene[ime+str(i+1)]>1:
            pozitivne+=1
        if ocjene[ime+str(i+1)]==1:
            jedinice+=1
        elif ocjene[ime+str(i+1)]==2:
            dvice+=1
        elif ocjene[ime+str(i+1)]==3:
            trice+=1
        elif ocjene[ime+str(i+1)]==4:
            cetvrtice+=1
        else:
            petice+=1

imena_i_ocjene=ocjene.items()
for student, ocjena in imena_i_ocjene:
    print(student, ":", ocjena)

print("Jedinica ima: ", jedinice)
print("Dvica ima: ", dvice)
print("Trica ima: ", trice)
print("Cetvrtica ima: ", cetvrtice)
print("Petica ima: ", petice)
print("Prolaznost je: ", round((pozitivne/ukupni_broj)*100,2),"%")
                  
        
