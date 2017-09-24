def delta(xs):
	return sum([abs(xs[i - 1] - xs[i]) for i in range(len(xs))])


if __name__ == '__main__':

    import tour_art as tour

    import matplotlib.pyplot as plt

    xs = [complex(a, b) for a, b in tour.tour]
    ds = delta(xs)

    xs, ys = zip(*tour.tour + [tour.tour[0]])

    plt.figure(figsize=(10, 10))
    plt.axis('off')
    # plt.title('ds : {}'.format(ds))
    plt.plot(xs, ys, 'ro')
    plt.plot(xs, ys, 'k-')
    plt.savefig('art.png')
