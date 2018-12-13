if __name__ == '__main__':
    import sys
    import random

    seed = int(sys.argv[1])
    k = int(sys.argv[2])
    m = int(sys.argv[3])

    universe = [random.randint(10 ** (k - 1), 10 ** k) for i in range(m)]

    with open('npp_{}_{}_{}.txt'.format(seed, k, m), 'w') as instance:
        print(m, file=instance)
        for item in universe:
            print(item, file=instance)
