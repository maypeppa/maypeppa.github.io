#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ps = [x for x in path.split('/') if x]
        ps2 = []
        for p in ps:
            if p == '.':
                continue
            elif p == '..':
                if not ps2:
                    break
                ps2.pop()
            else:
                ps2.append(p)
        return '/' + '/'.join(ps2)


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath('/'))
