"""
Author - Oscar Riveros http://www.peqnp.science
This Particular Code is in Public Domain
Generate Random Instances Of Mixed Integer Programmin for http://lpsolve.sourceforge.net/5.5/ 
(can convert with lp_solve on mps see help)
"""

if __name__ == '__main__':
    import sys
    import numpy

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    matrix = numpy.random.randint(-n, m, size=(n, m))# + numpy.random.logistic(size=(n, m))
    aa = numpy.random.randint(-n ** 2, n, size=(n,))# + numpy.random.sample(size=(n,))
    bb = numpy.random.randint(-n, n ** 2, size=(n,))# + numpy.random.sample(size=(n,))
    cc = numpy.random.randint(-n ** 2, m ** 2, size=(m,))# + numpy.random.normal(size=(m,))
    bounds = [(numpy.random.randint(-n // 2, 0), numpy.random.randint(1, n // 2)) for _ in range(m)]

    numpy.savetxt('data/data.matrix', matrix, fmt='%Lf')
    numpy.savetxt('data/data.a', aa, fmt='%Lf')
    numpy.savetxt('data/data.b', bb, fmt='%Lf')
    numpy.savetxt('data/data.c', cc, fmt='%Lf')
    numpy.savetxt('data/data.bounds', bounds, fmt='%i')

    print('min: ' + ' '.join('{} * x{}'.format(c, x) for x, c in enumerate(cc)) + ';')
    for e, row in enumerate(matrix):
        print('{} <= '.format(aa[e]) + ' '.join('{} x{}'.format(c, x) for x, c in enumerate(row)) + ' <= {}'.format(bb[e]) + ';')

    for i, (y, x) in enumerate(bounds):
        print('x{} <= {};'.format(i, x))
        print('x{} >= {};'.format(i, y))
    for i in range(len(bounds)):
        print('int x{};'.format(i))

