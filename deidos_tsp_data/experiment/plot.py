def delta(xs):
    return sum([abs(xs[i - 1] - xs[i]) for i in range(len(xs))])


if __name__ == '__main__':
    import sys 

    import matplotlib.pyplot as plt

    with open(sys.argv[1]) as data:
        exec(data.readline())

    xs = [complex(a, b) for a, b in tour]
    ds = delta(xs)

    xs, ys = zip(*tour + [tour[0]])

    plt.figure(figsize=(20, 20))
    plt.axis('off')
    plt.title('http://twitter.com/maxtuno\nnº cityes : {}\n  tour : {}'.format(len(tour), ds))
    plt.plot(xs, ys, 'ro-', alpha=0.4)
    plt.savefig(sys.argv[1].replace('.py', '.png'))
