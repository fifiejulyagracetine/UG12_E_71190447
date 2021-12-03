Awal = int(input("Masukkan awal deret: "))
Akhir= int(input("Masukkan akhir deret: "))
list1 = []

if (Awal + 1) % 2 == 0:
    for i in range (Awal+1, Akhir, 2) :
        if i % 5 == 0 or i % 9 == 0 : continue
        print (i, end = " ")

else:
    for i in range (Awal, Akhir, 2):
        if i % 5 == 0 or i % 9 == 0 : continue
        print (i, end = " ") 