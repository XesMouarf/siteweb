# -*- coding: utf-8 -*-

def parse():
    db(db.ingredient).delete()
    import os
    filename = os.path.join(request.folder, 'private', 'ciqual.csv')
    f = open(filename,'r')
    for line in f:
        line = line.split(';')
        try:
            kcals=float(line[20].replace(',','.'))
        except Exception, e:
            print e
            kcals = None
        try:
            sodium=float(line[4].replace(',','.'))
        except:
            sodium = None
        try:
            magesium=float(line[5].replace(',','.'))
        except:
            magesium = None
        try:
            phosphore=float(line[6].replace(',','.'))
        except:
            phosphore = None
        try:
            potasium=float(line[7].replace(',','.'))
        except:
            potasium = None
        try:
            calcium=float(line[8].replace(',','.'))
        except:
            calcium= None
        try:
            maganese=float(line[9].replace(',','.'))
        except:
            maganese = None
        try:
            fer=float(line[10].replace(',','.'))
        except:
            fer = None
        try:
            cuivre=float(line[11].replace(',','.'))
        except:
            cuivre = None
        try:
            zinc=float(line[12].replace(',','.'))
        except:
            zinc = None
        try:
            selenium=float(line[13].replace(',','.'))
        except:
            selenium = None
        try:
            iode=float(line[14].replace(',','.'))
        except:
            iode = None
        try:
            proteines=float(line[15].replace(',','.'))
        except:
            proteines = None
        try:
            glucides=float(line[17].replace(',','.'))
        except:
            glucides = None
        try:
            lipides=float(line[27].replace(',','.'))
        except:
            lipides = None
        try:
            amidon=float(line[21].replace(',','.'))
        except:
            amidon = None
        try:
            fibre=float(line[25].replace(',','.'))
        except:
            fibre = None
        try:
            vitamine_d=float(line[47].replace(',','.'))
        except:
            vitamine_d = None
        try:
            vitamine_e=float(line[48].replace(',','.'))
        except:
            vitamine_e = None
        try:
            vitamine_k1=float(line[49].replace(',','.'))
        except:
            vitamine_k1 = None
        try:
            vitamine_k2=float(line[50].replace(',','.'))
        except:
            vitamine_k2 = None
        try:
            vitamine_c=float(line[51].replace(',','.'))
        except:
            vitamine_c = None
        try:
            vitamine_b1=float(line[52].replace(',','.'))
        except:
            vitamine_b1 = None
        try:
            vitamine_b2=float(line[53].replace(',','.'))
        except:
            vitamine_b2 = None
        try:
            vitamine_b3=float(line[54].replace(',','.'))
        except:
            vitamine_b3 = None
        try:
            vitamine_b5=float(line[55].replace(',','.'))
        except:
            vitamine_b5 = None
        try:
            vitamine_b6=float(line[56].replace(',','.'))
        except:
            vitamine_b6 = None
        try:
            vitamine_b12=float(line[57].replace(',','.'))
        except:
            vitamine_b12 = None
        try:
            vitamine_b9=float(line[58].replace(',','.'))
        except:
            vitamine_b9 = None

        db.ingredient.insert(
            name=line[3],
            kcals=kcals,
            sodium=sodium,
            magesium=magesium,
            phosphore=phosphore,
            potasium=potasium,
            calcium=calcium,
            maganese=maganese,
            fer=fer,
            cuivre=cuivre,
            zinc=zinc,
            selenium=selenium,
            iode=iode,
            proteines=proteines,
            glucides=glucides,
            lipides=lipides,
            amidon=amidon,
            fibre=fibre,
            vitamine_d=vitamine_d,
            vitamine_e=vitamine_e,
            vitamine_k1=vitamine_k1,
            vitamine_k2=vitamine_k2,
            vitamine_c=vitamine_c,
            vitamine_b1=vitamine_b1,
            vitamine_b2=vitamine_b2,
            vitamine_b3=vitamine_b3,
            vitamine_b5=vitamine_b5,
            vitamine_b6=vitamine_b6,
            vitamine_b12=vitamine_b12,
            vitamine_b9=vitamine_b9,
            hasmacro=True)
    return dict()