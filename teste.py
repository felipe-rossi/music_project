import numpy

matriz = numpy.zeros((10, 10))

for i in range(0, 10):
    for j in range(0, 10):
        matriz[i][j] = i + j

print(matriz)