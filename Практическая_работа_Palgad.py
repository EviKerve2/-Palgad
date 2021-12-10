from random import *
inimised=["Pillipets", "Zemlyakov", "Vinogradova", "Komarova", "Kerve", "Illing"]
palgad=[2500, 2300, 2000, 1900, 1700, 1500]

def sisesta_andmed(i,p): #Добавить в список новых три фамилии
    N=3
    for n in range(N): #Ставит рандомному работнику рандомную зарплату
        a=input("Введите фамилию нового работника: ") #просит ввести
        i.append(a) #Добавляет элемент в конец списка 
        palk=randint(100,10000) #Вводит рандомную зарплату новому работнику
        p.append(palk) #Добавляет элемент в конец списка 
    return i,p 

def andmed_ekranile(i,p): #выводит на экран список имен и зарплат
    N=len(i) #Возвращает число
    for n in range(N): #Ставит рандомному работнику рандомную зарплату
        print(i[n],"-",p[n])

def kustutamine(i,p): #удаляет человека из списка
    nimi=input("Введите имя для удаления из списка: ") #просит ввести
    n=i.count(nimi) #Возвращает количество элементов со значением nimi
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)): #Ставит рандомное возвращение числа
            if i[e]==nimi: 
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,". ",i[e],"-", p[e])
        jaar=int(input("Порядковый номер: ")) #просит ввести
        i.pop(abi_list[jaar-1]) #Удаляет i-ый элемент и возвращает его
        p.pop(abi_list[jaar-1]) #Удаляет i-ый элемент и возвращает его
        andmed_ekranile(i,p)
    return i,p
        
def top3(i,p,v): #три самых высоких зарплаты
    if v==1:
        p.sort() #Сортирует список 
        p.reverse() #Разворачивает список 
        i.sort() #Сортирует список 
        i.reverse() #Разворачивает список 
        for h in range (0,len(p),1):
            if h>=3:
                break
            print(p[h])
            print(i[h])
    elif v==2:
        p.sort() #Сортирует список 
        i.sort() #Сортирует список 
        for j in range(0,len(p),1):
            if j>=3:
                break
            print(p[j])
            print(i[j])

def keskmine_kustutamine(i,p): #удаляет все зарплаты ниже средней
    summa=0
    new_list5=[] #Делает новый список
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Средняя зарплата составляет - ", summa, " все зарплаты ниже этой цифры будут удалены!")
    w=0 #w припавнивается к нулю
    while w<len(p):
        if p[w]<summa:
            del p[w] #Если последовательность инструкций, возвращающает значение w, то он удаляет зарплаты ниже средней
        else:
            w+=1
    print("В списке зарплат остались зарплаты выше средней: ",p) #Если нет, то он выводит экран эту надпись


def name_search1(i,p):
    nimi=input("Введите имя работника: ") #просит ввести 
    n=i.count(nimi) #Возвращает количество элементов со значением nimi
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                print(t,". ",i[e]," - ",p[e] )

while 1:
    print("\na - ввести новых работников: \ne - показать на экран список работников: \nk - удалить работников у которых зарплата ниже средней.\nz - топ три богатых/бедных работников. \nu - поиск зарплат по имени и фамилии.")
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
