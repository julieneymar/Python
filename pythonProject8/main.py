# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from builtins import range


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def tony():

    n = int(input("entrer le nonbre d'étudiant:"))
    while (n > 100):
        print("error, le nombre maximal d'étudiant est 100")
        n = int(input("entrer le nonbre d'étudiant:"))
        continue
    i=1
    while (i <=n):
        print("# INFORMATION DE L'ETUDIANT:", str(i))
        N = input(" entrez le nom et prénom de l'étudiant :")
        note1 = float(input("entrez la note 1 de la matiere 1:"))
        while (note1 > 20):
            print("erroe")
            note1 = float(input("entrez la note 1 de la matiere 1:"))
            continue
        note2 = float(input("entrez la note 2 de la matiere 1:"))
        while (note2 > 20):
            print("erroe")
            note2 = float(input("entrez la note 2 de la matiere 1:"))
            continue
        note3 = float(input("entrez la note 1 de la matiere 2:"))
        while (note3 > 20):
            print("erroe")
            note3 = float(input("entrez la note 1 de la matiere 2:"))
            continue
        note4 = float(input("entrez la note 2 de la matiere 2:"))
        while (note4 > 20):
            print("erroe")
            note4 = float(input("entrez la note 2 de la matiere 2:"))
            continue
        note5 = float(input("entrez la note 1 de la matiere 3:"))
        while (note5 > 20):
            print("erroe")
            note5 = float(input("entrez la note 1 de la matiere 3:"))
            continue
        note6 = float(input("entrez la note 2 de la matiere 3:"))
        while (note6 > 20):
            print("erroe")
            note6 = float(input("entrez la note 2 de la matiere 3:"))
            continue
        note7 = float(input("entrez la note 1 de la matiere 4:"))
        while (note7 > 20):
            print("erroe")
            note7 = float(input("entrez la note 1 de la matiere 4:"))
            continue
        note8 = float(input("entrez la note 2 de la matiere 4:"))
        while (note8 > 20):
            print("erroe")
            note8 = float(input("entrez la note 2 de la matiere 4:"))
            continue
        note9 = float(input("entrez la note 1 de la matiere 5:"))
        while (note9 > 20):
            print("erroe")
            note9 = float(input("entrez la note 1 de la matiere 5:"))
            continue
        note10 = float(input("entrez la note 2 de la matiere 5:"))
        while (note10 > 20):
            print("erroe")
            note10 = float(input("entrez la note 2 de la matiere 5:"))
            continue
        moy=((((note1+note2)/2)+((note3+note4)/2)+((note5+note6)/2)+((note7+note8)/2)+((note9+note10)/2))/5)
        print("la moyenne est:",(moy))
        if (moy >= 17):
            print("Mention: Excéllent")
        elif (moy >= 14):
            print("Mention: Bien")
        elif (moy >= 12):
            print("Mention: assez bien")
        elif (moy >= 10):
            print("Moyenne: Passable")
        else:
            print("Mention: Insufisant")

            i = i + 1

            myfill = open("schoolbase.txt", "w+" )

            Mat1=((note1 + note2)/2)
            Mat2=((note3 + note4)/2)
            Mat3=((note5+note6)/2)
            Mat4=((note7+note8)/2)
            Mat5=((note9+note10)/2)
            myfill.write("\nMoyMat1:"+ str(Mat1))
            myfill.write("\nMoyMat2:"+ str(Mat2))
            myfill.write("\nMoyMat3:"+ str(Mat3))
            myfill.write("\nMoyMat4:"+ str(Mat4))
            myfill.write("\nMoyMat5:"+ str(Mat5))
            myfill.write("\nMoyenne general:" + str(moy))

            if (moy >= 17):
                print("Mention: Excéllent")
            elif (moy >= 14):
                print("Mention: Bien")
            elif (moy >= 12):
                print("Mention: assez bien")
            elif (moy >= 10):
                print("Moyenne: Passable")
            else:
                print("Mention: Insufisant")
                Mat1 = ((note1 + note2) / 2)
                Mat2 = ((note3 + note4) / 2)
                Mat3 = ((note5 + note6) / 2)
                Mat4 = ((note7 + note8) / 2)
                Mat5 = ((note9 + note10) / 2)


print(tony())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
