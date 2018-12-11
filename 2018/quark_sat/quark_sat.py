"""
copyright (b) 2012-2018 Oscar Riveros. all rights reserved. oscar.riveros@peqnp.science

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def exist_conflict(trail):
    for cls in cnf:
        if set(-lit for lit in cls) < set(trail):
            return False
    return True


def backtrack(trail):
    while trail:
        lit = trail.pop()
        if lit not in taboo:
            taboo.append(-lit)
            trail.append(-lit)
            return True
        else:
            taboo.remove(lit)
    return False


def dpll():
    trail = []
    while True:
        if not exist_conflict(trail):
            if not trail:
                return []
            else:
                if not backtrack(trail):
                    return []
        else:
            if len(trail) == n:
                return trail
            else:
                trail.append(variables.difference(map(abs, trail)).pop())


def save_sat(model):
    with open(sys.argv[1][:sys.argv[1].index('.')] + '.mod', 'w') as mod_file:
        print('SAT', file=mod_file)
        print(' '.join(list(map(str, sorted(model, key=abs)))) + ' 0', file=mod_file)


if __name__ == '__main__':

    import sys

    n, m, cnf = 0, 0, []
    with open(sys.argv[1], 'r') as cnf_file:
        lines = cnf_file.readlines()
        for line in filter(lambda x: not x.startswith('c'), lines):
            if line.startswith('0') or line.startswith('%'):
                break
            if line.startswith('p cnf'):
                n, m = list(map(int, line[6:].split(' ')))
            else:
                cnf.append(list(map(int, line.rstrip('\n')[:-2].split(' '))))

    variables, taboo = set(range(1, n + 1)), []

    mod = dpll()

    if mod:
        print('SAT')
        save_sat(mod)
    else:
        print('UNSAT')
