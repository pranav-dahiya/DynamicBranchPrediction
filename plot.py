import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

m = np.array([1,2,4])
n = np.array(m)
m, n = np.meshgrid(m, n)

#labels = ["art", "gcc", "go", "hmmer", "libquantum", "mcf", "sjeng", "sphinx3"]
labels = ["BHT", "Correlation", "GAp"]

data = np.loadtxt("comparison.csv", delimiter=",")
'''
data = data.reshape((8,3,3))

fig = plt.figure()
ax = fig.gca(projection='3d')

labels = ["art", "gcc", "go", "hmmer", "libquantum", "mcf", "sjeng", "sphinx3"]
for i, series in enumerate(data):
    surf = ax.plot_surface(m, n, series, alpha=0.8, label=labels[i])
    surf._facecolors2d=surf._facecolors3d
    surf._edgecolors2d=surf._edgecolors3d

ax.set_xlabel("m (in Bits)")
ax.set_ylabel("n (in Bits)")
ax.set_zlabel("Miss Rate")

ax.legend(loc='upper right')

plt.show()
'''
'''
plt.figure()
X = [2**i for i in range(len(data[0]))]
for i, series in enumerate(data):
    plt.plot(X, series, label=labels[i])
plt.xlabel("n (in bits)")
plt.ylabel("Miss Rate")
plt.legend(loc='upper right')
plt.show()
'''

'''
X = data[0]
Y = list()
for i in range(1, len(data)):
    Y.append(data[i])
'''

print(len(data))
plt.figure()
X = [2**i for i in range(9, 9 + len(data[0]))]
for i, series in enumerate(data):
    plt.plot(X, series, label = labels[i])
plt.xlabel("Predictor Size (in bits)")
plt.ylabel("Miss Rate")
plt.legend(loc="upper right")
plt.show()
