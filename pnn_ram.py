from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import operator

arr = []
berkas = open ("data_train_PNN.txt","r")
data = berkas.readlines()

for line in data:
    arr.append(line.strip().split('\t'))

sorting = sorted(arr,key=operator.itemgetter(3))

#Inisialisasi Kelas dan visualisasi
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
def visualisasi():
    #konversi data string ke integer
    for i in range(0,150):
        p = list(map(float,sorting[i]))
        x = p[3]

        # Masukkan data ke kelas nol
        if x == 0.0:
            p.remove(x)
            cnol.append(p)
            x0.append(np.array(cnol[i][0]))
            y0.append(np.array(cnol[i][1]))
            z0.append(np.array(cnol[i][2]))
        # Masukkan data ke kelas Satu
        elif x == 1.0:
            p.remove(x)
            csatu.append(p)
            for j in range(len(csatu)):
                x1.append(csatu[j][0])
                y1.append(csatu[j][1])
                z1.append(csatu[j][2])
        # Masukkan data ke kelas Dua
        else:
            p.remove(x)
            cdua.append(p)
            for k in range(len(cdua)):
                x2.append(cdua[k][0])
                y2.append(cdua[k][1])
                z2.append(cdua[k][2])
    berkas.close()

    graf = plt.figure()
    data = graf.add_subplot(111, projection='3d')
    data.set_xlabel('Attr 1')
    data.set_ylabel('Attr 2')
    data.set_zlabel('Attr 3')
    data.scatter(x0, y0, z0, c='r', marker='o')
    data.scatter(x1, y1, z1, c='g', marker='*')
    data.scatter(x2, y2, z2, c='b', marker='^')
    plt.show()

input('Masukkan angka')
visualisasi()





