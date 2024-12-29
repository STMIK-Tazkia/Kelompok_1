#Bagian 1 Soal NO.4

import numpy as np
def soal_matrix():
    
    C = np.array([
        [44, 55, 54, 10],
        [33, 5, 32, 13],
        [21, 7, 21, 11],
        [33, 88, 32, 15]
    ])

    D = np.array([
        [2, 1, 1, 1],
        [2, 1, 0, 2],
        [2, 0, 1, 2],
        [1, 1, 1, 2]
    ])

    result = np.dot(C, D)

    
    print("Matrix C:")
    print(C)
    print("\nMatrix D:")
    print(D)
    print("\nHasil Dari C x D:")
    print(result)

if __name__ == "__main__":
    soal_matrix()
    



#Bagian 2 Soal No.4

A = {33, 47, 50, 18, 22, 6, 4, 3, 23, 14, 41}
B = {41, 12, 56, 21, 31, 53, 15, 6, 40, 22}


irisan = A.intersection(B)


print("Irisan dari himpunan A dan B:", irisan)





#Bagian 3 Soal No.1

A = {109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1}


urutan_a = list(A)


for i in range(len(urutan_a)):
    for j in range(0, len(urutan_a) - i - 1):
        if urutan_a[j] > urutan_a[j + 1]:
            urutan_a[j], urutan_a[j + 1] = urutan_a[j + 1], urutan_a[j]

print("Himpunan A setelah diurutkan:", urutan_a)






#Bagian 3 soal No.2

def cari_nilai(himpunan, x):
    A_list = list(himpunan)  
    for i in range(len(A_list)):
        if A_list[i] == x:
            return i  
    return -1  

x = 300  
indeks = cari_nilai(A, x)


if indeks != -1:
    print(f"Nilai {x} ditemukan pada indeks ke-{indeks}")
else:
    print(f"Nilai {x} tidak ditemukan di himpunan A")


