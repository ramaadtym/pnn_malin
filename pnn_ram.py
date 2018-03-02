from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def menu():
    print("====MENU=====")
    print("1. Visualisasi Data Training")
    print("2. Keputusan Data Testing")
    n = input("Masukkan Angka")
    n = int(n)

    klasifikasi()
    if n == 1:
        visualisasi(cnol, csatu, cdua)
    elif n == 2:
        smooth(cnol, csatu, cdua)
        # keputusan(jum)


arr = []
arr2 = []
attr = 0
attr2 = 0
with open("data_train_PNN.txt", "r") as berkas:
    data = berkas.readlines()
    for y in data:
        if (attr > 0):
            brs = y.split()
            arr.append([float(brs[0]), float(brs[1]), float(brs[2]), float(brs[3])])
        attr += 1
with open("data_test_PNN.txt", "r") as berkas:
    data = berkas.readlines()
    for y in data:
        if (attr2 > 0):
            brs = y.split()
            arr2.append([float(brs[0]), float(brs[1]), float(brs[2])])
        attr2 += 1
# Inisialisasi array
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
trainT = []
Ttest = []
acc = []

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
    return cnol, csatu, cdua


def visualisasi(cnol, csatu, cdua):
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
    # Masukkan data ke kelas dua
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


def smooth(cnol, csatu, cdua, g):
    # g = 1.4
    dis1 = []
    dis2 = []
    dis3 = []

    # Pencarian Distance
    pjg0 = len(cnol)
    pjg1 = len(csatu)
    pjg2 = len(cdua)
    jum = []

    for i in range(len(arr)):
        findMin = []
        w = 0
        for j in range(len(arr)):
            if (arr[i] != arr[j] and arr[i][3] == arr[j][3]):
                # cari distance pakai Euclidean
                for v in range(0, 3):
                    w = w + pow((float(arr[j][v]) - float(arr[i][v])), 2)
                d = math.sqrt(w)
                # Tampung di array buat cari minimum
                findMin.append(d)
        if (arr[i][3] == 0):
            dis1.append(min(findMin))
        elif (arr[i][3] == 1):
            dis2.append(min(findMin))
        else:
            dis3.append(min(findMin))
        # print(dis1)
    jum.append([float((g * sum(dis1)) / pjg0), float((g * sum(dis2)) / pjg1), float((g * sum(dis3)) / pjg2)])
    return jum


def keputusan(cnol, csatu, cdua, arr, arr2, jum):
    pjg0 = len(cnol)
    pjg1 = len(csatu)
    pjg2 = len(cdua)
    n = [pjg0, pjg1, pjg2]
    benar = 0
    panjang = 0
    for i in range(len(arr2)):
        m = 3
        peluang = [0.0, 0.0, 0.0]
        nilaiexp = [0.0, 0.0, 0.0]
        for k in range(len(cnol)):
            a = 0
            for j in range(0, 3):
                a = a + float(pow((float(arr2[i][j]) - float(cnol[k][j])), 2))
            b = 2 * (pow(jum[0][0], 2))
            form = math.exp(-(a / b))
            nilaiexp[0]+=form
        peluang[0] = form / pow(2 * math.pi, m / 2) * pow(jum[0][0], m) * n[0]
        for k in range(len(csatu)):
            a = 0
            for j in range(0, 3):
                a = a + float(pow((float(arr2[i][j]) - float(csatu[k][j])), 2))
            b = 2 * (pow(jum[0][1], 2))
            form = math.exp(-(a / b))
            nilaiexp[1]+=form
        peluang[1] = form / pow(2 * math.pi, m / 2) * pow(jum[0][1], m) * n[1]
        for k in range(len(cdua)):
            a = 0
            for j in range(0, 3):
                a = a + float(pow((float(arr2[i][j]) - float(cdua[k][j])), 2))
            b = 2 * (pow(jum[0][2], 2))
            form = math.exp(-(a / b))
            nilaiexp[2]+=form
        peluang[2] = form / pow(2 * math.pi, m / 2) * pow(jum[0][2], m) * n[2]
        # output = peluang.index(max(peluang))
        if (peluang.index(max(peluang)) == arr2[i][3]):
            benar += 1
        panjang += 1
        akurasi = benar/panjang
    print("akurasi", akurasi)
    acc.append(akurasi)


def findG(arr, acc,):
    arrg = []
    # Data Training dari data train
    for i in range(30, 150):
        trainT.append(arr[i])
        x = arr[i][3]
        if x == 0.0:
            cnol.append(arr[i])
        elif x == 1.0:
            csatu.append(arr[i])
        else:
            cdua.append(arr[i])

    # Data tes dari data train
    for j in range(0, 30):
        Ttest.append(arr[j])
    g = 0
    for p in range(200):
        g +=np.random.uniform(0,0.02)
        print ("Nilai G = ", g)
        s = smooth(cnol, csatu, cdua, g)
        keputusan(cnol, csatu, cdua, trainT, Ttest, s)
        arrg.append(g)

    plt.plot(arrg,acc)
    plt.xlabel("Konstanta g")
    plt.ylabel("Akurasi")
    plt.show()


# klasifikasi()
# smooth(cnol,csatu,cdua,g)
findG(arr,acc)

# keputusan(cnol,csatu,cdua)
# menu()
