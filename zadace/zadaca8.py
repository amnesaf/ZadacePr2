def pozdrav(ime):
    print("Pozdrav", ime + "!")


dobrodošla = lambda ime: print("Dobrodošla", ime + "!")

def treca(funkcija):
    funkcija("Amnesa")


treca(pozdrav)
treca(dobrodošla)




