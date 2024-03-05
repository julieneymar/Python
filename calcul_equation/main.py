# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


aqn = input(" saisissez l'équation:")
def parsing(equ):
    s = equ.split(equ)
    t = float(s[1])
    ss = s[0].split(" ")
    coeff , exp =[],[]
    op=1
    for e in ss:
        if e!='+' and e!='-':
            ee=e.spli("x^")
            if (len(ee) = 1):
                exp.append(0)
                coeff.append(float(e)*op-t)
            else:
                exp.append(int(ee[1]))
                coeff.append(float(ee[0]*op))





