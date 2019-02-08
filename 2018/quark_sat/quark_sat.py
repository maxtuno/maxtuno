"""
copyright (c) 2012-2018 Oscar Riveros. all rights reserved. oscar.riveros@peqnp.science

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


import sys


def apply_decide():
    assert_literal(select_literal())


def assert_literal(lit):
    trail.append(lit)


def literals_to_variables(lts):
    return map(abs, lts)


def invert_literal(lit):
    return -lit


def invert_clause(cls):
    return set([invert_literal(lit) for lit in cls])


def select_literal():
    return variables.difference(literals_to_variables(trail)).pop()


def no_exist_conflict():
    for cls in cnf:
        if invert_clause(cls) < set(trail):
            return True
    return False


def apply_backtrack():
    while trail:
        lit = trail.pop()
        if lit not in taboo:
            taboo.append(invert_literal(lit))
            assert_literal(invert_literal(lit))
            return True
        else:
            taboo.remove(lit)
    return False


def dpll():
    while True:
        if no_exist_conflict():
            if not trail:
                return False
            else:
                if not apply_backtrack():
                    return False
        else:
            if len(trail) == n:
                return True
            else:
                apply_decide()


def validate():
    for cls in cnf:
        sat = False
        for lit in cls:
            sat |= lit in trail
            if sat:
                break
        if not sat:
            return False
    return True


def save_sat():
    if validate():
        with open(sys.argv[1][:sys.argv[1].index('.')] + '.model', 'w') as model:
            print('SAT', file=model)
            print(' '.join(list(map(str, sorted(trail, key=abs)))) + ' 0', file=model)


if __name__ == '__main__':
    n, m, cnf = 0, 0, []
    with open(sys.argv[1], 'r') as cnf_file:
        lines = cnf_file.readlines()
        for line in filter(lambda x: not x.startswith('c'), lines):
            if line.startswith('p cnf'):
                n, m = list(map(int, line[6:].split(' ')))
            else:
                cnf.append(list(map(int, line.rstrip('\n')[:-2].split(' '))))

    variables, trail, taboo = set(range(1, n + 1)), [], []

    if dpll():
        print('SAT')
        save_sat()
    else:
        print('UNSAT')
