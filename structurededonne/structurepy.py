


annee= {"janvier":31, "fevrier" : 28, "mars" : 31, "avril":30, "mai":31, "juin":30,"juillet":31,"août":31,"septembre":30,"octobre":31,"novembre":30,"decembre":31}
for i in annee:
    mois = input("entrez le mois :")
    print(annee[mois])
    if mois == "quitter":
        break
    
   