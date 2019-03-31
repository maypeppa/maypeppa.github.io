# -*- coding: utf-8 -*-

class ChessKnight:
    def probability(self, x, y, n):
        dp = [[], []]
        for i in range(8):
            dp[0].append([0] * 8)
            dp[1].append([0] * 8)
        now = 0
        x -= 1
        y -= 1
        dp[now][x][y] = 1.0
        nexts = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for _ in range(n):
            for i in range(8):
                for j in range(8):
                    dp[1 - now][i][j] = 0.0
            for i in range(8):
                for j in range(8):
                    for (di, dj) in nexts:
                        ni = i + di
                        nj = j + dj
                        if ni >= 0 and ni < 8 and nj >= 0 and nj < 8:
                            dp[1 - now][ni][nj] += dp[now][i][j] * 0.125
            now = 1 - now
        res = 0.0
        for i in range(8):
            for j in range(8):
                res += dp[now][i][j]
        return res


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


def do_test(x, y, n, __expected):
    startTime = time.time()
    instance = ChessKnight()
    exception = None
    try:
        __result = instance.probability(x, y, n);
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
    sys.stdout.write("ChessKnight (450 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ChessKnight.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = int(f.readline().rstrip())
            y = int(f.readline().rstrip())
            n = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, y, n, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1528419808
    PT, TT = (T / 60.0, 75.0)
    points = 450 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
