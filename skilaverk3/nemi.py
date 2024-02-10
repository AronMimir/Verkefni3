class Nemi:
    def __init__(self, kennitala, nafn, kyn, simanumer):
        self.kennitala = kennitala
        self.nafn = nafn
        self.kyn = kyn
        self.simanumer = simanumer
    
    def __str__(self):
        return f"Nafn: {self.nafn}, Kennitala: {self.kennitala}, Kyn: {self.kyn}, Simanumer: {self.simanumer}"

class Hermannanemi(Nemi):
    def __init__(self, kennitala, nafn, kyn, simanumer, adstandandi, bekkur, onn):
        super().__init__(kennitala, nafn, kyn, simanumer)
        self.adstandandi = adstandandi
        self.bekkur = bekkur
        self.onn = onn
    
    def __str__(self):
        return super().__str__() + f", Adstandandi: {self.adstandandi}, Bekkur: {self.bekkur}, Onn: {self.onn}"

class Flokkstjorannemi(Nemi):
    def __init__(self, kennitala, nafn, kyn, simanumer, herdeild, her="landher"):
        super().__init__(kennitala, nafn, kyn, simanumer)
        self.herdeild = herdeild
        self.her = her
    
    def __str__(self):
        return super().__str__() + f", Herdeild: {self.herdeild}, Her: {self.her}"

class Foringjanemi(Nemi):
    def __init__(self, kennitala, nafn, kyn, simanumer, stigNams, namslaun, herlan):
        super().__init__(kennitala, nafn, kyn, simanumer)
        self.stigNams = stigNams
        self.namslaun = namslaun
        self.herlan = herlan
    
    def __str__(self):
        return super().__str__() + f", Stig nams: {self.stigNams}, Namslaun: {self.namslaun}, Herlan: {self.herlan}"