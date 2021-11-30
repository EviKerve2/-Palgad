from random import *
inimised=["Pillipets", "Zemlyakov", "Vinogradova", "Komarova", "Kerve", "Illing"]
palgad=[2500, 2300, 2000, 1900, 1700, 1500, 1300, 500]

def sisesta_andmed(i,p): #Добавить в список новых три фамилии
    N=3
    for n in range(N):
        a=input("Введите фамилию нового работника: ")
        i.append(a)
        palk=randint(100,10000) #Вводит рандомную зарплату новому работнику
        p.append(palk)
    return i,p

def andmed_ekranile(i,p): #выводит на экран список имен и зарплат
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #удаляет человека из списка
    nimi=input("Введите имя для удаления из списка: ")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,". ",i[e],"-", p[e])
        jaar=int(input("Порядковый номер: "))
        i.pop(abi_list[jaar-1])
        p.pop(abi_list[jaar-1])
        andmed_ekranile(i,p)
    return i,p
        
def top3(i,p,v): #три самых высоких зарплаты
    if v==1:
        p.sort()
        p.reverse()
        i.sort()
        i.reverse()
        for h in range (0,len(p),1):
            if h>=3:
                break
            print(p[h])
            print(i[h])
    elif v==2:
        p.sort()
        i.sort()
        for j in range(0,len(p),1):
            if j>=3:
                break
            print(p[j])
            print(i[j])

def keskmine_kustutamine(i,p): #удаляет все зарплаты ниже средней
    summa=0
    new_list5=[]
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Средняя зарплата составляет - ", summa, " все зарплаты ниже этой цифры будут удалены!")
    w=0
    while w<len(p):
        if p[w]<summa:
            del p[w]
        else:
            w+=1
    print("В списке зарплат остались зарплаты выше средней: ",p)


def name_search1(i,p):
    nimi=input("Введите имя работника: ")
    n=i.count(nimi)
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                print(t,". ",i[e]," - ",p[e] )

while 1:
    print("a - ввод данных: \ne - вывод на экран: \nk - удаление зарплат ниже средней.\nz - топ три. \nu - поиск зарплат по имени.")
    valik=input()
    if valik.lower()=="a":
        inimised,palgad=sisesta_andmed(inimised,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimised, palgad)
    elif valik.lower()=="k":
        inimised,palgad=kustutamine(inimised, palgad)
    elif valik.lower()=="z":
        top3(inimised,palgad, int(input("1 - топ трех самых богатых, 2 - топ трех самых бедных.")))
    elif valik.lower()=="u":
        name_search1(inimised, palgad)
    else:
        break
