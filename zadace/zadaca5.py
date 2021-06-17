def parni_neparni(a):
    def parni(a):
        broj=2
        while broj<a:
            yield broj
            broj+=2
    print("Parni brojevi su: ")
    for i in parni(a):
        print(i)

    def neparni(a):
        broj=1
        while broj<a:
            yield broj
            broj+=2
        print("Neparni brojevi su: ")
        for i in neparni(a):
            print(i)
            
parni_neparni(22)
