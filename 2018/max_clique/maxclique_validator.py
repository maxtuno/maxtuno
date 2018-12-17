def load(file_name):
    global mm
    with open(file_name) as msp_file:
        spam_reader = csv.reader(msp_file, delimiter=' ')
        next(spam_reader)
        uu = []
        for row in spam_reader:
            del row[0]
            mm[int(row[0]), int(row[1])] = 1
            mm[int(row[1]), int(row[0])] = 1
            if int(row[0]) not in uu:
                uu.append(int(row[0]))
            if int(row[1]) not in uu:
                uu.append(int(row[1]))
    return uu


if __name__ == '__main__':

    import csv
    import networkx as nx

    mm = {}

    uu = load('data.clq')

    # http://iridia.ulb.ac.be/~fmascia/files/DIMACS/C125.9.clq
    uu = [115, 92, 18, 48, 31, 116, 71, 125, 91, 19, 2, 98, 117, 68, 85, 7, 99, 114, 122, 29, 70, 11, 25, 101, 44, 79, 49, 34, 110, 1, 5, 121, 45, 77]

    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    G = nx.Graph(gg)

    print(G.degree(uu))
