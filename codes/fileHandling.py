def beolvas(utvonal):
    adatok = list()
    with open(utvonal, "r", encoding="utf8") as file:
        for i, sor in enumerate(file):
            if i == 0:
                continue
            egysor = sor.strip().split(",")
            egyadat = [str(egysor[0].strip()), str(egysor[1].strip()), str(egysor[2].strip()), str(egysor[3].strip()), int(egysor[4].strip()), float(egysor[5].strip()), float(egysor[6].strip()), str(egysor[7].strip())]
            adatok.append(egyadat)
    return adatok

def legnagyobb_stadion(ut):
    adatok = beolvas(ut)
    eredmeny = [-1, "nev", "varos"]
    for elem in adatok:
        if elem[4] > eredmeny[0]:
            eredmeny[0] = elem[4]
            eredmeny[1] = elem[3]
            eredmeny[2] = elem[2]
    with open("legnagyobb.txt", "w", encoding="utf8") as file:
        if eredmeny[0] == 0 or len(adatok) == 0:
            file.write("Nincs (Nincs)\n")
        else:
            file.write(eredmeny[1] + " (" + eredmeny[2] + ")\n")

def osszes_arena(ut):
    adatok = beolvas(ut)
    eredmeny = list()
    for elem in adatok:
        if elem[3].endswith("Arena"):
            eredmeny.append([elem[3], elem[2], elem[-1], "True" if elem[4] > 50000 else "False"])
    with open("arena_park.csv", "w", encoding="utf8") as file:
        file.write("Stadium,City,Country,Big\n")
        for elem in eredmeny:
            file.write(elem[0] + "," + elem[1] + "," + elem[2] + "," + elem[3] + "\n")

def osszes_park(ut):
    adatok = beolvas(ut)
    eredmeny = list()
    for elem in adatok:
        if elem[3].endswith("Park"):
            eredmeny.append([elem[3], elem[2], elem[-1], "True" if elem[4] > 20000 else "False"])
    
    with open("arena_park.csv", "a") as file:
        for elem in eredmeny:
            file.write(elem[0] + "," + elem[1] + "," + elem[2] + "," + elem[3] + "\n")
        
def varosok_szama(ut, *args):
    if len(args) == 0:
        raise Exception("Nincs megadva egy orszag sem!")
    varosok = set()
    eredmeny = dict()
    adatok = beolvas(ut)
    for orszag in args:
        for elem in adatok:
            if elem[-1] == orszag:
                varosok.add(elem[2])
        rendvaros = [x for x in varosok]
        rendvaros.sort()
        eredmeny[orszag] = rendvaros
        varosok.clear()

    with open("varosok.txt", "w", encoding="utf8") as file:
        for key, value in eredmeny.items():
            file.write(key + " varosai:\n")
            for elem in value:
                file.write("\t" + elem + "\n")
            file.write("----------\n")
