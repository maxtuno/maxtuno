if __name__ == '__main__':
    import random

    d = 32  # bits
    n = 1000  # size

    public_seed = 0  # the public seed for generating the same universe of numbers
    private_seed = 666  # you secret seed for creating a unique target

    random.seed(public_seed)
    universe = [random.randrange(1, 2 ** d) for i in range(n)]

    random.seed(private_seed)
    t = sum(random.sample(universe, k=len(universe) // 2))

    print(public_seed, t)

    with open('{}_{}.txt'.format(public_seed, t), 'w') as data:
        data.write('{}\n{}'.format(len(universe), t))
        for o in universe:
            data.write('\n{}'.format(o))
