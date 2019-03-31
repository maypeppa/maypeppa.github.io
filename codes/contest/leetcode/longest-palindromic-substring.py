#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n == 0:
            return ''

        dp = []
        for i in range(n):
            dp.append([0] * n)
        for k in range(1, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if (i + 1) <= (j - 1):
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 1

        max_len = -1
        max_res = None
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = (j - i + 1)
                    max_res = (i, j)
        return s[max_res[0]: max_res[1] + 1]


if __name__ == '__main__':
    s = Solution()
    print((s.longestPalindrome(
        "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir")))
    print((s.longestPalindrome(
        "dqlvtrcystnncxjffjrkiiqgtcunbwntqrpqkjepzbxzodeckrbrwzjjuptloypmjgbwioqtjzjjgqpaemgvxkapjgbfhhwltvtqgkozuzvlwetftjeocjqrdwlhdwtgzdhwvmuhvmdpkxnzrrizjntxbbpzwtjryecgfajolalwdzxqtknvvvaxuhanzowlbwjraigvrflcqoormbeexekmqpmuuobseumctsiwhvdohywjaylixqgqookgneokebtmoyaspnzbwqzffyocvcylcjobnzbmhsdprzrgdlyzuutyuwygzeldfewicjnukguisceeopckkoviayrcqanzsryhwqhxjxcpiejojztrxad")))
    print((s.longestPalindrome(
        "lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc")))
