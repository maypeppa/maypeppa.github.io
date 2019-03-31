/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <string>
#include <utility>
using namespace std;
class Solution {
   public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        int** dp = new int*[n];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[n];
        }
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        for (int k = 2; k <= n; k++) {
            for (int i = 0; i <= (n - k); i++) {
                int j = i + k - 1;
                if (s[i] == s[j]) {
                    if ((i + 1) <= (j - 1)) {
                        dp[i][j] = dp[i + 1][j - 1] + 2;
                    } else {
                        dp[i][j] = 2;
                    }
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        int res = dp[0][n - 1];
        for (int i = 0; i < n; i++) {
            delete[] dp[i];
        }
        delete[] dp;
        return res;
    }
};
