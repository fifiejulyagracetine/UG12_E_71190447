masukkan_nilai = int(input("Masukkan Angka : "))

for i in range(masukkan_nilai):
    print(" "*(masukkan_nilai-i)+" *"*(i+1))

for j in range(masukkan_nilai):
    print(" "*(j+2)+" *"*(masukkan_nilai-1-j)) 