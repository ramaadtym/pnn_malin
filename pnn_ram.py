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
berkas.close()


#Inisialisasi Kelas
cnol = []
csatu = []
cdua = []

x = sorting[0][3]
if x == '0' :
    print("ok")
    cnol.append(sorting[0])
    print(cnol)
# plt.plot(arr[1], arr[2], 'ro')
# plt.axis([0, 3, 0, 3])
# plt.show()

