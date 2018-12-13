if __name__ == '__main__':

    import sys

    solution = list(sys.argv[2])

    with open(sys.argv[1]) as instance:
        items = instance.readlines()
        n = int(items[0])
        del items[0]
        uu, aa, bb = [], [], []
        for i in range(n):
            uu.append(int(items[i]))
            if solution[i] == '1':
                aa.append(int(items[i]))
            else:
                bb.append(int(items[i]))

    print('UNIVERSE : {}\n'.format(uu))
    print('A        : {}\n'.format(aa))
    print('B        : {}\n'.format(bb))
    print('Delta    : {}'.format(abs(sum(aa) - sum(bb))))
