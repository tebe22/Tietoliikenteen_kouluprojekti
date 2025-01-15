import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualisoi_data(data, keskipisteet):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='blue', label='Datapisteet')
    ax.scatter(keskipisteet[:, 0], keskipisteet[:, 1], keskipisteet[:, 2], c='red', marker='x', label='Keskipisteet')

    ax.set_xlabel('X-akseli')
    ax.set_ylabel('Y-akseli')
    ax.set_zlabel('Z-akseli')
    plt.legend()
    plt.show()