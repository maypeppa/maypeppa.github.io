# -*- coding: utf-8 -*-


class ChessMatch:
    def bestExpectedScore(self, teamA, teamB, lim):
        return 0.0


# CUT begin
# TEST CODE FOR PYTHON {{{
import math
import sys
import time


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


def do_test(teamA, teamB, lim, __expected):
    startTime = time.time()
    instance = ChessMatch()
    exception = None
    try:
        __result = instance.bestExpectedScore(teamA, teamB, lim);
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
    sys.stdout.write("ChessMatch (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ChessMatch.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            teamA = []
            for i in range(0, int(f.readline())):
                teamA.append(int(f.readline().rstrip()))
            teamA = tuple(teamA)
            teamB = []
            for i in range(0, int(f.readline())):
                teamB.append(int(f.readline().rstrip()))
            teamB = tuple(teamB)
            lim = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(teamA, teamB, lim, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1528419798
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
