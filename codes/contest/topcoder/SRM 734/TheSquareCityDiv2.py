# -*- coding: utf-8 -*-
import collections


class TheSquareCityDiv2:
    def find(self, r, t):
        n = int(round(len(t) ** 0.5))
        moves = []
        for i in range(n):
            for j in range(n):
                t0 = t[i * n + j]
                move = None
                warmest = -(1 << 30)
                for k0 in range(n):
                    for k1 in range(n):
                        dist = abs(k0 - i) + abs(k1 - j)
                        k = k0 * n + k1
                        if (dist <= r) and t[k] > warmest:
                            warmest = t[k]
                            move = k
                moves.append(move)

        states = [i * n + j for i in range(n) for j in range(n)]
        while True:
            changed = False
            next_states = []
            for s in states:
                ns = moves[s]
                if s != ns:
                    changed = True
                next_states.append(ns)
            if not changed:
                break
            states = next_states

        ra = len(set(states))
        group = collections.Counter()
        for s in states:
            group[s] += 1
        rb = group.most_common(1)[0][1]
        return ra, rb


# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math


def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False


def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join((pretty_str(y) for y in x)))
    else:
        return str(x)


def do_test(r, t, __expected):
    startTime = time.time()
    instance = TheSquareCityDiv2()
    exception = None
    try:
        __result = instance.find(r, t);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime  # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0


def run_tests():
    sys.stdout.write("TheSquareCityDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheSquareCityDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            r = int(f.readline().rstrip())
            t = []
            for i in range(0, int(f.readline())):
                t.append(int(f.readline().rstrip()))
            t = tuple(t)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(r, t, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1526551561
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
