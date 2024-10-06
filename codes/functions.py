def hogolyo_csata(rounds):
    back = dict()
    for item in rounds:
        for key, value in item.items():
            if key not in back.keys:
                back[key] = value
            else:
                szam = value.get('eldobott_hogolyok')
                
    return back

def hogolyo_pontossag(rounds):
    for key, value in rounds.items():
        if value.get('talalt') is None or value.get('eldobott_hogolyok') is None:
            value['pontossag'] = 0  
            rounds[key] = value
        else: 
            value['pontossag'] = value.get('talalt') / value.get('eldobott_hogolyok')
            rounds[key] = value
    return rounds

def hogolyo_piros_lap(rounds):
    back = []
    for key, value in rounds.items():
        if value.get('fejtalalat') is None or value.get('eldobott_hogolyok') is None:
            continue
        if value.get('pontossag') >= 0.7 and value.get('fejtalalat') / value.get('eldobott_hogolyok') >= 0.5:
            back.append(key)
    return back
    