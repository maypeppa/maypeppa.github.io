/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    int totalHammingDistance(vector<int>& nums) {
        int bits[32][2] = {0};
        for (int k = 0; k < nums.size(); k++) {
            int n = nums[k];
            for (int p = 0; p < 32; p++) {
                bits[p][n & 0x1] += 1;
                n = n >> 1;
            }
        }
        int count = 0;
        for (int p = 0; p < 32; p++) {
            count += (bits[p][0] * bits[p][1]);
        }
        return count;
    }
};
