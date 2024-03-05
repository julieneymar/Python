# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import random
n=random.randint(0,100)
vies = 10
print("j'ai choin un nombre au hasard,essayer de le deviner!")
while(vies > 0):
    var = int(input("Choisissez un nombre:"))
    if(var < n):
         print("c'est plus !")
    elif(var > n):
         print("c'est moins !")
    else:
        print("bravo ! tu as gagné !!")
        break
    vies -= 1
    print("vies :", vies)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
