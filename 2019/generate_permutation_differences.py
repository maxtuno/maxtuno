# If anyone wants to generate some instance of the problem of "Permutation Reconstruction from Differences" here is a very simple script, you can put in the comments or something similar.
# https://twitter.com/maxtuno/status/1081191522450792448
if __name__ == '__main__':
    import sys
    import random

    n = int(sys.argv[1])

    x = list(range(1, n + 1))

    random.shuffle(x)

    y = [abs(x[i + 1] - x[i]) for i in range(n - 1)]

    for i in range(n - 1):
        print(y[i])
