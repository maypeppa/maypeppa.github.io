/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <map>
#include <vector>
using namespace std;

class Solution {
   public:
    /*
     * @param edges: a directed graph where each edge is represented by a tuple
     * @return: the number of edges
     */
    int balanceGraph(vector<vector<int>>& edges) {
        // Write your code here
        map<int, int> degs;
        for (int i = 0; i < edges.size(); i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            degs[u] -= w;
            degs[v] += w;
        }
        vector<int> debts;
        for (auto it = degs.begin(); it != degs.end(); ++it) {
            if (it->second != 0) {
                debts.push_back(it->second);
            }
        }
        int n = debts.size();
        if (n == 0) return 0;
        int size = (1 << n);
        int* dp = new int[size];
        fill_n(dp, size, -1);

        for (int i = 1; i < size; i++) {
            int balance = 0;
            int count = 0;
            for (int j = 0; j < n; j++) {
                if ((1 << j) & i) {
                    balance += debts[j];
                    count += 1;
                }
            }

            if (balance == 0) {
                int exchange = count - 1;
                for (int j = 1; j < i; j++) {
                    if (((i & j) == j) and (dp[j] != -1) and
                        (dp[i - j] != -1)) {
                        exchange = min(dp[j] + dp[i - j], exchange);
                    }
                }
                dp[i] = exchange;
            }
        }
        int res = dp[size - 1];
        delete[] dp;
        return res;
    }
};
