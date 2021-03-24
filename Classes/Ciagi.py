class Ciagi:
    a1 = 0
    rozn = 0
    ile = 0
    wyrazyCiagu = [a1]

    def wyswietlElementy(self):
        print(self.wyrazyCiagu)
    def pobierzElem(self, *n):
        pobraneElementy = []
        for x in n:
            pobraneElementy.append(self.wyrazyCiagu[x-1])
        print(pobraneElementy)
    def pobierzParametry(self, a1, rozn, ile):
        self.a1 = a1
        self.rozn=rozn
        self.ile = ile
    def sumaEl(self):

        suma=0
        for x in self.wyrazyCiagu:
            suma +=x
        print(suma)
    def policzEl(self):
        if self.rozn != 0:
            a1 = self.a1
            for x in range(self.ile):
                an = a1 + self.rozn
                self.wyrazyCiagu.append(an)
                a1 = an