class Palack:
    def __init__(self, ital,  max_urtartalom, jelenlegi_urtartalom = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom
    
    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, urtartalom):
        if urtartalom > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        else:
            self._jelenlegi_urtartalom = urtartalom
        if urtartalom == 0:
            self.ital = None

    def suly(self):
        return self.max_urtartalom/35+self._jelenlegi_urtartalom
    
    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."
    
    def __eq__(self, p):
        if not isinstance(p, Palack):
            return False
        return self.ital == p.ital and self.max_urtartalom == p.max_urtartalom and self._jelenlegi_urtartalom == p.jelenlegi_urtartalom

    def __iadd__(self, p):
        if not isinstance(p, Palack):
            return self
        if self.ital is None:
            self.ital = p.ital
        volt = self._jelenlegi_urtartalom
        self.jelenlegi_urtartalom = (self._jelenlegi_urtartalom + p.jelenlegi_urtartalom)
        if self.ital != p.ital:
            if volt != 0 and p.jelenlegi_urtartalom != 0:
                self.ital = "keverek"
            elif volt == 0:
                self.ital = p.ital
        return self

class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom, jelenlegi_urtartalom=1, palackdij=25):
        super().__init__(ital, max_urtartalom, jelenlegi_urtartalom)
        self.palackdij = palackdij

    def __str__(self):
        return "Visszavalthato"+super().__str__()
    
class Rekesz:
    def __init__(self, max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok = []
    
    def suly(self):
        osszsuly=0
        for elem in self.palackok:
            osszsuly+=elem.suly()
        return osszsuly
    
    def uj_palack(self, p):
        if self.max_teherbiras >= self.suly() + p.suly():
            self.palackok.append(p)

    def osszes_penz(self):
        penz=0
        for elem in self.palackok:
            if isinstance(elem, VisszavalthatoPalack):
                penz+=elem.palackdij
        return penz
