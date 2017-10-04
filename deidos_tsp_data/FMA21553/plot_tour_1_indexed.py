def delta(xs):
    return sum([abs(xs[i - 1] - xs[i]) for i in range(len(xs))])


if __name__ == '__main__':
    import sys
    import csv

    import matplotlib.pyplot as plt

    uu, xy = [], {}
    with open(sys.argv[1]) as file:
        spam_reader = csv.reader(file, delimiter=' ')
        [n] = map(int, next(spam_reader))
        for row in spam_reader:
            _, x, y = map(float, [r for r in row if r != ''])
            uu += [complex(x, y)]

    tour = []

    with open(sys.argv[2]) as data:
        exec('tour = [' + ','.join(data.readlines()).replace(' ', ',') + ']')

    xy = [uu[i - 1] for i in tour]

    ds = delta(xy)

    xs, ys = zip(*[(a.real, a.imag) for a in xy + [xy[0]]])

    plt.figure(figsize=(40, 40))
    plt.axis('off')
    plt.title('Concorde\nhttp://twitter.com/maxtuno\nTour Length (Standard Euclidean with Floats) = {}'.format(delta(xy)))
    plt.gca().invert_yaxis()
    plt.plot(xs, ys, 'ko', alpha=0.5)
    plt.plot(xs, ys, 'k-', alpha=0.5)
    plt.savefig(sys.argv[2] + '.png', origin='lower')
