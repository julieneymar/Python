# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Etudiant:
    def __init__(self, nom,note1,note2,note3,note4,note5,note6,note7,note8,note9,note10,moy,mention):
        self.nom=nom
        self.note1=note1
        self.note2=note2
        self.note3=note3
        self.note4=note4
        self.note5=note5
        self.note6=note6
        self.note7=note7
        self.note8=note8
        self.note9=note9
        self.note10=note10
        self.mention=mention

m = Etudiant(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
n = int(input("entrer le nonbre d'étudiant:"))
while (n > 100):
            print("error, le nombre maximal d'étudiant est 100")
            n = int(input("entrer le nonbre d'étudiant:"))
            continue
myfill = open("schoolbase.txt", "w+")

for i in range(1,n+1):

            print("# INFORMATION DE L'ETUDIANT:", str(i))
            m.nom = (input(" entrez le nom et prénom de l'étudiant :",))
            m.note1 = float(input("entrez la note 1 de la matiere 1:"))
            while (m.note1 > 20):
                print("erroe")
                m.note1 = float(input("entrez la note 1 de la matiere 1:"))
                continue
            m.note2 = float(input("entrez la note 2 de la matiere 1:"))
            while (m.note2 > 20):
                print("erroe")
                m.note2 = float(input("entrez la note 2 de la matiere 1:"))
                continue
            m.note3 = float(input("entrez la note 1 de la matiere 2:"))
            while (m.note3 > 20):
                print("erroe")
                note3 = float(input("entrez la note 1 de la matiere 2:"))
                continue
            m.note4 = float(input("entrez la note 2 de la matiere 2:"))
            while (m.note4 > 20):
                print("erroe")
                m.note4 = float(input("entrez la note 2 de la matiere 2:"))
                continue
            m.note5 = float(input("entrez la note 1 de la matiere 3:"))
            while (m.note5 > 20):
                print("erroe")
                m.note5 = float(input("entrez la note 1 de la matiere 3:"))
                continue
            m.note6 = float(input("entrez la note 2 de la matiere 3:"))
            while (m.note6 > 20):
                print("erroe")
                m.note6 = float(input("entrez la note 2 de la matiere 3:"))
                continue
            m.note7 = float(input("entrez la note 1 de la matiere 4:"))
            while (m.note7 > 20):
                print("erroe")
                m.note7 = float(input("entrez la note 1 de la matiere 4:"))
                continue
            m.note8 = float(input("entrez la note 2 de la matiere 4:"))
            while (m.note8 > 20):
                print("erroe")
                m.note8 = float(input("entrez la note 2 de la matiere 4:"))
                continue
            m.note9 = float(input("entrez la note 1 de la matiere 5:"))
            while (m.note9 > 20):
                print("erroe")
                m.note9 = float(input("entrez la note 1 de la matiere 5:"))
                continue
            m.note10 = float(input("entrez la note 2 de la matiere 5:"))
            while (m.note10 > 20):
                print("erroe")
                m.note10 = float(input("entrez la note 2 de la matiere 5:"))
                continue
            m.moy = ((((m.note1 + m.note2) / 2) + ((m.note3 + m.note4) / 2) + ((m.note5 + m.note6) / 2) + ((m.note7 + m.note8) / 2) + (
                        (m.note9 + m.note10) / 2)) / 5)
            print("la moyenne est:", (m.moy))

            if (m.moy >= 17):
                    m.mention = "Excéllent"
                    print("Mention",m.mention)
            elif (m.moy >= 14):
                    m.mention="Mention: Bien"
                    print("Mention",m.mention)
            elif (m.moy >= 12):
                    m.mention=" assez bien"
                    print("Mention:",m.mention)
            elif (m.moy >= 10):
                    m.mention="Passable"
                    print("Mention:", m.mention)
            else:
                    m.mention="Insufisant"
                    print("Mention:",m.mention)




            Mat1 = ((m.note1 + m.note2) / 2)
            Mat2 = ((m.note3 + m.note4) / 2)
            Mat3 = ((m.note5 + m.note6) / 2)
            Mat4 = ((m.note7 + m.note8) / 2)
            Mat5 = ((m.note9 + m.note10) / 2)

            myfill.write("\n\nNom Prenom:" + m.nom)
            myfill.write("\nMoyMat1:" + str(Mat1))
            myfill.write("\nMoyMat2:" + str(Mat2))
            myfill.write("\nMoyMat3:" + str(Mat3))
            myfill.write("\nMoyMat4:" + str(Mat4))
            myfill.write("\nMoyMat5:" + str(Mat5))
            myfill.write("\nMoyenne general:" + str(m.moy))
            myfill.write("\nMention:" + m.mention + "\n")





i = i + 1


















# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
