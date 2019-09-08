from array import *
def inv(p):
    return not p
def diz(p,q):
    return p|q
def kon(p,q):
    return p&q
def imp(p,q):
    return (not p)&q
def ecv(p,q):
    return p==q
def peremen():
    print("Введите кол-во переменных в выражении:")
    peremen = input()
    return peremen
def boolInput(a):
    inp = input()
    if str(inp) == "1":
        a.append(True)
    elif str(inp) == "0":
        a.append(False)
    else:
        print("Вы ввели значение переменной неверное, вводите либо '1', либо '0'")
        boolInput(a)
def decision(num1, num2, sing, a):
    b = []
    if sing == "diz":
        for i in range(len(a[num1])):
            b.append(diz(a[num1][i], a[num2][i]))
        a.append(b)
    if sing == "kon":
        for i in range(len(a[num1])):
            b.append(kon(a[num1][i], a[num2][i]))
        a.append(b)
    if sing == "imp":
        for i in range(len(a[num1])):
            b.append(imp(a[num1][i], a[num2][i]))
        a.append(b)
    if sing == "ecv":
        for i in range(len(a[num1])):
            b.append(ecv(a[num1][i], a[num2][i]))
        a.append(b)
    print("Номер переменной для этого действия " + str(len(a) - 1))
    print("------")
def decision1(num, sing, a):
    b = []
    if sing == "diz":
        for i in range(len(a[num])):
            b.append(diz(a[num][i], a[num][i]))
        a.append(b)
    if sing == "kon":
        for i in range(len(a[num])):
            b.append(kon(a[num][i], a[num][i]))
        a.append(b)
    if sing == "imp":
        for i in range(len(a[num])):
            b.append(imp(a[num][i], a[num][i]))
        a.append(b)
    if sing == "ecv":
        for i in range(len(a[num])):
            b.append(ecv(a[num][i], a[num][i]))
        a.append(b)
    if sing == "inv":
        for i in range(len(a[num])):
            b.append(inv(a[num][i]))
        a.append(b)
    print("Номер переменной для этого действия " + str(len(a) - 1))
    print("------")
def inputValue():
    print("Введите знак между переменными:")
    znak = input()
    if znak == "diz" or znak == "kon" or znak == "imp" or znak == "ecv":
        return znak
    else:
        print("Вы ввели знак неверно, повторите попытку.")
        return inputValue()


def outputPicture(a):
    s = ""
    for i in range(len(a)):
        for k in range(len(a[i])):
            s = s+str(a[i][k])
        print(str(i) + ": " + s)
        s = ""


a = []
peremen = int(peremen())
if peremen == 1:
    a = [1,0]
elif peremen == 2:
    a = [[0,0,1,1],[0,1,0,1]]
elif peremen == 3:
    a = [[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1], [0,1,0,1,0,1,0,1]]
elif peremen == 4:
    a = [[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1], [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]]
elif peremen == 5:
    a = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1], [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1], [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]]
print(a)
print("Введите кол-во действий в уравнении:")
N=int(input())
for i in range(N):
    print("Данные для действия номер " + str(i))
    print("Сколько переменых используется для этого действия?")
    per = int(input())
    if per == 1:
        print("Введите номер переменной:")
        value = int(input())
        print("Введите название лог. операции:")
        sing = inputValue()
        decision1(value,sing,a)
    if per == 2:
        print("Введите номер переменной один:")
        num1 = int(input())
        print("Введите номер переменной два:")
        num2 = int(input())
        sing = inputValue()
        decision(num1, num2, sing, a)
outputPicture(a)
