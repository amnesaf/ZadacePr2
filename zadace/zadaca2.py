def ocjena(bodovi):
    if bodovi<50:
        return "Nedovoljan"
    elif bodovi<65:
        return "Dovoljan"
    elif bodovi<80:
        return "Dobar"
    elif bodovi<90:
        return "Vrlodobar"
    else:
        return "Izvrstan"

from csv import reader
datoteka=open("rezultati.csv","r")
csv_reader=reader(datoteka)
rezultati=list(map(tuple, csv_reader))

novi_rezultati=[]
for ime, prezime, bodovi in rezultati:
    novi_rezultati.append((prezime,ime,bodovi))

novi_rezultati.sort()
rezultati_ocjena=[]
for student in novi_rezultati:
    rjecnik={}
    rjecnik["prezime"]=student[0]
    rjecnik["ime"]=student[1]
    rjecnik["ocjena"]=ocjena(int(student[2]))
    rezultati_ocjena.append(rjecnik)

rezultati_ocjena2=[]
for student in rezultati_ocjena:
    rezultati_ocjena2.append((student["prezime"],student["ime"],student["ocjena"]))

print(rezultati_ocjena2)
