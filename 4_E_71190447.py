#data
value = [3,20,100,-35,50]
#fungsi 1 dan perulangan 1
def nilai_maksimal (data):
    nilai_terbesar = data[0]

    for nilai in data:
        if nilai > nilai_terbesar :
            nilai_terbesar = nilai
    return nilai_terbesar

#fungsi 2 dan perulangan 2
def nilai_minimal (data):
    nilai_minimal = data [0]

    for nilai in data:
        if nilai < nilai_minimal:
            nilai_minimal = nilai
    return nilai_minimal

print("Nilai terbesar:", nilai_maksimal(value))
print("nilai Terkecil", nilai_minimal(value))