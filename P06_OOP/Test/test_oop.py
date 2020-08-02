class Cilveks:
    Vards = "Stas"
    Uzvards = "Tarasov"
    Vecums = 10

    def PilnsVards(self):
        print("Pilns vards ir", self.Vards, self.Uzvards)

    def DzimDiena(self):
        self.Vecums = self.Vecums + 1
        print ("Sodien",self.Vards, self.Uzvards, "palika", self.Vecums,"gadu")

a = Cilveks()
a.PilnsVards()
a.DzimDiena()
