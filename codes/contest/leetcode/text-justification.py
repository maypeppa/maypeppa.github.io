#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        gp = []
        r = []
        wc = 0
        for w in words:
            # at least len(r)-1 spaces to separate words.
            if (wc + len(w) + len(r) - 1) < maxWidth:
                r.append(w)
                wc += len(w)
            else:
                gp.append(r)
                r = [w]
                wc = len(w)
        gp.append(r)

        gp2 = []
        for r in gp[:-1]:
            wc = sum(map(len, r))
            rest = maxWidth - wc
            if len(r) == 1:
                s = r[0] + ' ' * rest
            else:
                avg = rest / (len(r) - 1)
                left = rest - avg * (len(r) - 1)
                if left:
                    s = (' ' * (1 + avg)).join(r[:left]) + ' ' * (1 + avg) + (' ' * avg).join(r[left:])
                else:
                    s = (' ' * avg).join(r)
            gp2.append(s)

        wc = sum(map(len, gp[-1]))
        rest = maxWidth - wc - len(gp[-1]) + 1
        gp2.append(' '.join(gp[-1]) + ' ' * rest)
        return gp2


if __name__ == '__main__':
    s = Solution()
    # print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    # print s.fullJustify(["What","must","be","shall","be."], 12)
    print(s.fullJustify(
        ["Don't", "go", "around", "saying", "the", "world", "owes", "you", "a", "living;", "the", "world", "owes",
         "you", "nothing;", "it", "was", "here", "first."], 30))
