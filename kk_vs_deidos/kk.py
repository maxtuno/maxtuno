import bisect

class _Num:
    def __init__(self, value, index):
        self.value = value
        self.i = index

    def __lt__(self, other):
        return self.value < other.value

# This implements the Karmarkar-Karp heuristic for partitioning a set
# in two, i.e. into two disjoint subsets s.t. their sums are
# approximately equal.  It produces only one result, in O(N*log N)
# time.  A remarkable property is that it loves large sets:  in
# general, the more numbers you feed it, the better it does.

class Partition:
    def __init__(self, nums):
        self.nums = nums
        sorted = [_Num(nums[i], i) for i in range(len(nums))]
        sorted.sort()
        self.sorted = sorted

    def run(self):
        sorted = self.sorted[:]
        N = len(sorted)
        connections = [[] for i in range(N)]

        while len(sorted) > 1:
            bigger  = sorted.pop()
            smaller = sorted.pop()

            # Force these into different sets, by "drawing a
            # line" connecting them.
            i, j = bigger.i, smaller.i
            connections[i].append(j)
            connections[j].append(i)

            diff = bigger.value - smaller.value
            assert diff >= 0
            bisect.insort(sorted, _Num(diff, i))

        # Now sorted contains only 1 element x, and x.value is
        # the difference between the subsets' sums.

        # Theorem:  The connections matrix represents a spanning tree
        # on the set of index nodes, and any tree can be 2-colored.
        # 2-color this one (with "colors" 0 and 1).

        index2color = [None] * N

        def color(i, c):
            if index2color[i] is not None:
                assert index2color[i] == c
                return
            index2color[i] = c
            for j in connections[i]:
                color(j, 1-c)

        color(0, 0)

        # Partition the indices by their colors.
        subsets = [[], []]
        for i in range(N):
            subsets[index2color[i]].append(i)

        return subsets

if __name__ == '__main__':

    import sys

    # implementation from
    # https://mail.python.org/pipermail/tutor/2001-August/008098.html

    x = []

    # modified by maxtuno
    with open(sys.argv[1], 'r') as data:
        ds = data.readlines()
        for d in ds[1:]:
            x.append(int(d))

    x.sort()
    x.reverse()
    # end

    p = Partition(x)
    s, t = p.run()
    sum1 = 0
    sum2 = 0
    for i in s:
        sum1 += x[i]
    for i in t:
        sum2 += x[i]
    print("Set 1 sum", repr(sum1))
    print("Set 2 sum", repr(sum2))
    print("difference", repr(abs(sum1 - sum2)))
