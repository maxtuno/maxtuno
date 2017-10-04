import copy
import csv
import subprocess
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, points, size):
        self._matrix = np.zeros((size, size))
        self._size = len(points)

        for i, a in enumerate(points):
            for j, b in enumerate(points):
                if self._matrix[i][j] == 0.0:
                    dist = np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
                    self._matrix[i][j] = dist
                    self._matrix[j][i] = dist

    def size(self):
        return self._size

    def get_distance(self, i, j):
        return self._matrix[i][j]

    def mst(self):
        temp_matrix = self._matrix.copy()

        for i in range(self._size):
            for j in range(self._size):
                if i >= j:
                    temp_matrix[i][j] = 0

        return minimum_spanning_tree(temp_matrix).toarray()

    def remove_node(self, i):
        self._matrix = np.delete(self._matrix, i, 1)
        self._matrix = np.delete(self._matrix, i, 0)
        self._size -= 1


def one_tree(graph):
    short_graph = copy.deepcopy(graph)
    short_graph.remove_node(0)

    cost = np.sum(np.sum(short_graph.mst()))

    min_cost = graph.get_distance(0, 1)
    second_min = min_cost

    for j in range(1, graph.size()):
        dist = graph.get_distance(0, j)
        if dist < min_cost:
            second_min = min_cost
            min_cost = dist

    cost += min_cost + second_min

    return cost


def get_lower_bound(file_name):
    uu = []
    with open(file_name) as file:
        i, spam_reader = 0, csv.reader(file, delimiter=' ')
        _ = next(spam_reader)
        for row in spam_reader:
            if '' in row:
                row.remove('')
            _, x, y = map(float, row)
            uu.append([x, y])
            i += 1

    lb = one_tree(Graph(points=uu, size=len(uu)))

    return lb, 3 * lb / 2


if __name__ == '__main__':

    while True:
        ini = 4
        tt, ss, rr = [], [], []
        for size in range(ini, 1000):

            process = subprocess.Popen(['python3', 'gen_tsp.py', str(size), str(2)])
            process.communicate()

            file_name = 'data_{}.txt'.format(size)

            ot, lb = get_lower_bound(file_name)

            process = subprocess.Popen(['./h_pro', file_name, 'tour_{}.txt'.format(size)], stdout=subprocess.PIPE)
            out, err = process.communicate()
            ds = float(out.decode())

            print(ds / lb, ds, lb)

            print(80 * '-')
            print('SIZE : {}'.format(size))

            tt.append(ds)
            ss.append(lb)
            rr.append(ot)

            plt.figure(figsize=(10, 10))
            plt.title('(3 / 2) 1-Tree (RED)\nH Algorithm Tour Length (BLUE)\n1-Tree (GREEN)\nhttp://twitter.com/maxtuno')
            plt.plot(range(ini, ini + len(ss)), ss, 'r-', label='(3/2) 1-Tree')
            plt.plot(range(ini, ini + len(tt)), tt, 'b-', label='H Algorithm')
            plt.plot(range(ini, ini + len(rr)), rr, 'g-', label='1-Tree')
            plt.savefig('graph.png')
            plt.close()
