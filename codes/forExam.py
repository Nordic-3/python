def pincenyitogato(szoveg):
    if not isinstance(szoveg, str) or szoveg == "":
        return dict()
    lista = szoveg.split("-")
    eredmeny = {"Vörösbor": 0, "Fehérbor": 0, "Szóda": 0, "Összérték": 0}
    for i in range(0, len(lista)):
        lista[i] = lista[i].strip().lower()
    for elem in lista:
        if elem == "gábor":
            eredmeny["Vörösbor"] += 12
            eredmeny["Szóda"] += 1
            eredmeny["Összérték"] += 12*4500 + 350
        elif elem == "marci":
            eredmeny["Fehérbor"] += 6
            eredmeny["Összérték"] += 5*3000
        elif elem == "istván":
            eredmeny["Fehérbor"] += 8
            eredmeny["Szóda"] += 2
            eredmeny["Összérték"] += 7*3000 + 2*350
    return eredmeny

class LoLCharacter:

    def __init__(self, nev, tamadas = 10) -> None:
        self.nev = nev
        self._tamadas = tamadas
        self.hp = 100
        self.kepessegek = list()

    @property
    def tamadas(self):
        return self.tamadas
    @tamadas.setter
    def tamadas(self, tam):
        if 100 > tam > 0:
            self._tamadas = tam
        else:
            self._tamadas = 100
    
    def kepesseg_hozzaadas(self, kepesseg):
        if not isinstance(kepesseg, str):
            raise ValueError("Ervenytelen")
        titkosit = ""
        for index, elem in enumerate(kepesseg):
            if index % 3 == 0:
                titkosit += elem
        self.kepessegek.append(titkosit)
    
    def kepesseg_torles(self, torol):
        if not isinstance(torol, str):
            raise ValueError("Ervenytelen")
        titkosit = ""
        for index, elem in enumerate(torol):
            if index % 3 == 0:
                titkosit += elem
        self.kepessegek.remove(titkosit)
    
    def __lt__(self, karakter):
        if not isinstance(karakter, LoLCharacter):
            raise ValueError("Nem LoL karakter")
        return self._tamadas > karakter.tamadas
    def __str__(self):
        return f"A karakter neve: {self.nev}, támadása: {self._tamadas}, HP: {self.hp}, és {len(self.kepessegek)} képessége van."
    def __sub__(self, karakter):
        if not isinstance(karakter, LoLCharacter):
            raise ValueError("Nem karaktert adtal meg!")
        eredmeny = LoLCharacter(karakter.nev, self._tamadas if self._tamadas < karakter.tamadas else karakter.tamadas)
        eredmeny.hp = self.hp if self.hp < karakter.hp else karakter.hp
        for elem in self.kepessegek:
            eredmeny.kepesseg_hozzaadas(elem)
        for elem in karakter.kepessegek:
            eredmeny.kepesseg_hozzaadas(elem)
        return eredmeny
    
print(pincenyitogato("GÁBor- mARci-István-István-Gábor-Marci-Marci-gábor-Gábor-ISTván"))
