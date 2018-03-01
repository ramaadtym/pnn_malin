from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def menu():
    print("====MENU=====")
    print("1. Visualisasi Data Training")
    print("2. Perhitungan Data Training")
    n = input("Masukkan Angka")
    n = int(n)

    klasifikasi()
    if n == 1:
        visualisasi(cnol,csatu,cdua)
    elif n == 2:
        smooth(cnol,csatu,cdua)
    elif n == 3:
        keputusan(jum)

arr = []
attr = 0
with open ("data_train_PNN.txt","r") as berkas:
    data = berkas.readlines()
    for y in data:
        if(attr > 0):
            brs = y.split()
            arr.append([float(brs[0]),float(brs[1]),float(brs[2]),float(brs[3])])
        attr += 1

#Inisialisasi array
cnol = []
csatu = []
cdua = []
x0 = []
y0 = []
z0 = []
x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []
jum = []

def klasifikasi():
    for i in range(0, 150):
        x = arr[i][3]
        # print(x)
        if x == 0.0:
            cnol.append(arr[i])
        elif x == 1.0:
          csatu.append(arr[i])
        else:
         cdua.append(arr[i])
    return cnol,csatu,cdua

def visualisasi(cnol,csatu,cdua):
    # print(cnol[3])
    for i in range(len(cnol)):
        x0.append(np.array(cnol[i][0]))
        y0.append(np.array(cnol[i][1]))
        z0.append(np.array(cnol[i][2]))
    # Masukkan data ke kelas Satu
    for j in range(len(csatu)):
         x1.append(csatu[j][0])
         y1.append(csatu[j][1])
         z1.append(csatu[j][2])
    #Masukkan data ke kelas dua
    for k in range(len(cdua)):
        x2.append(cdua[k][0])
        y2.append(cdua[k][1])
        z2.append(cdua[k][2])

    berkas.close()

    graf = plt.figure()
    graf.canvas.set_window_title('Visualisasi Data Training')
    data = graf.add_subplot(111, projection='3d')
    data.set_xlabel('Attr 1')
    data.set_ylabel('Attr 2')
    data.set_zlabel('Attr 3')
    data.scatter(x0, y0, z0, c='r', marker='o')
    data.scatter(x1, y1, z1, c='g', marker='*')
    data.scatter(x2, y2, z2, c='b', marker='^')
    plt.show()


def smooth(cnol,csatu,cdua):
    g = 1
    dis1 = []
    dis2 = []
    dis3 = []

    #Pencarian Distance
    pjg0 = len(cnol)
    pjg1 = len(csatu)
    pjg2 = len(cdua)

    for i in range(len(arr)):
        findMin = []
        w = 0
        for j in range(len(arr)):
            if (arr[i] != arr[j] and arr[i][3] == arr[j][3]):
                #cari distance pakai Euclidean
                for v in range(0,3):
                    w = w + pow((float(arr[j][v]) - float(arr[i][v])), 2)
                d = math.sqrt(w)
                #Tampung di array buat cari minimum
                findMin.append(d)
        if (arr[i][3] == 1) :
            dis1.append(min(findMin))
        elif (arr[i][3] == 2) :
            dis2.append(min(findMin))
        else :
            dis3.append(min(findMin))
        jum.append([float((g * sum(dis1)) / pjg0), float((g * sum(dis2)) / pjg1), float((g * sum(dis3)) / pjg2)])

        return jum

def keputusan(jum):
    arr2 = []
    attr2 = 0
    with open("data_test_PNN.txt", "r") as berkas:
        data = berkas.readlines()
        for y in data:
            if (attr2 > 0):
                brs = y.split()
                arr2.append([float(brs[0]), float(brs[1]), float(brs[2])])
            attr2 += 1



# menu()
klasifikasi()
smooth(cnol,csatu,cdua)

keputusan(jum)

