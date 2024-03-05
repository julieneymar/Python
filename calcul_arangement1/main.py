# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions,

def facto(n):
    if n <= 1:
        return 1
    return n*facto(n-1)
n = int(input("taper n :"))
choix = int(input(" choix ? permutation=1 , arrangement=2 , combination=3:"))
if choix == 1:
  print(facto(n))
elif choix == 2:
    p = int(input("taper p:"))
    print(facto(n)/facto(n-p))
else:
    p = int(input("taper p:"))
    print(facto(n)/facto(n-p)/facto(p))
