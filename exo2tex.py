import re

def nettoie(nomFichier):
    try :
        f = open(nomFichier,"rt")  # read text
        try :
            texte = f.read()
        finally : # toujours exécuté !
            f.close()
    except FileNotFoundError :
        print("Ce fichier n'a pas été trouvé !")
    except IOError :
        print("Erreur à l'ouverture du fichier")


    # nettoyage du texte

    aEnlever = ['×'     ,'…'  ,' ','–','÷'   ]
    remplace = ['\\times','...',' ','-','\\div']
    texteTmp = ""

    for i in range(len(texte)):
        if texte[i] in aEnlever :
            texteTmp = texteTmp + remplace[aEnlever.index(texte[i])]
        else :
            texteTmp = texteTmp + texte[i]
    texte = texteTmp

    # on supprime les espaces après les signes -
    texteFin=texte.replace('- ','-')
            
    return(texteFin)


def ecrit(nomFichier,chaineAecrire):
    try:
        f = open(nomFichier, 'w')
        f.write(chaineAecrire)
    except IOError:
        print("Problème à l'enregistrement du fichier")
    finally : # toujours exécuté !
        f.close()



def ajouteEnumerate(nomFichier):
    try :
        f = open(nomFichier,"rt")  # read text
        try :
            listLigne = list(f)
        finally : # toujours exécuté !
            f.close()
    except FileNotFoundError :
        print("Ce fichier n'a pas été trouvé !")
    except IOError :
        print("Erreur à l'ouverture du fichier")

    debutItem = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    enumerat = False
    texte = ""
    
    for i in listLigne :
        if i[0]=="a" and i[1]=="." and i[2]==" ":
            enumerat=True
            texte = texte + "\n\\begin{colenumerate}{1} \n\\item " + i[3:]
        elif i[0] in debutItem and i[1]=="." and i[2]==" ":
            enumerat=True
            texte = texte + "\\item " + i[3:]
        elif enumerat == True :
            texte = texte + "\\end{colenumerate} \n \n" + i
            enumerat = False
        else :
            texte = texte + i
        #print(i)
            
            
    return(texte)


def ajouteExercice(nomFichier):
    try :
        f = open(nomFichier,"rt")  # read text
        try :
            listLigne = list(f)
        finally : # toujours exécuté !
            f.close()
    except FileNotFoundError :
        print("Ce fichier n'a pas été trouvé !")
    except IOError :
        print("Erreur à l'ouverture du fichier")

    debutExo = ['0','1','2','3','4','5','6','7','8','9',' ']
    
    texte = ""
    
    for i in listLigne :
        if i[0]==' ' and i[1]=="1" and i[2]==" " and i[3]==" " :
            texte = texte + "\n\\begin{exercice}[]" + i[4:]
        if i[0]==' ' and i[1] in debutExo and i[2] in debutExo and i[3] in debutExo :
            texte = texte + "\\end{exercice}\n\n\\begin{exercice}[]" + i[4:]
        else :
            texte = texte + i
    texte = texte + "\\end{exercice}"
    return(texte)


# Programme principal


fichier = input("Nom du fichier :")

# on enlève les caractères non reconnus
text = nettoie(fichier)
ecrit("fichierPass1",text)

# on ajoute les enumerate
text = ajouteEnumerate("fichierPass1")
ecrit("fichierPass2",text)

# on ajoute les débuts d'exercice
text = ajouteExercice("fichierPass2")
ecrit("fichierPass3.tex",text)




