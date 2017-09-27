def delta(xs):
    return sum([abs(xs[i - 1] - xs[i]) for i in range(len(xs))])


if __name__ == '__main__':

    import tour as tour

    import matplotlib.pyplot as plt

    xs = [complex(a, b) for a, b in tour.tour]
    ds = delta(xs)

    xs, ys = zip(*tour.tour + [tour.tour[0]])

    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.title('http://twitter.com/maxtuno\nnº cityes : {}\n  tour : {}'.format(len(tour.tour), ds))
    plt.plot(xs, ys, 'ro-', alpha=0.4)
    plt.savefig('tsp.png')
