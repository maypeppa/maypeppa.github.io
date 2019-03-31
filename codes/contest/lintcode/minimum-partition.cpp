/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <iostream>
#include <set>
#include <vector>
using namespace std;

class Solution {
   public:
    /**
     * @param nums: the given array
     * @return: the minimum difference between their sums
     */
    int findMin(vector<int> &nums) {
        // write your code here
        int acc = 0;
        for (int i = 0; i < nums.size(); i++) {
            acc += nums[i];
        }
        int lmax = acc / 2;
        set<int> values;
        values.insert(0);
        for (int i = 0; i < nums.size(); i++) {
            vector<int> tmp;
            for (auto it = values.begin(); it != values.end(); ++it) {
                int v = *it;
                if ((v + nums[i]) <= lmax) {
                    tmp.push_back(v + nums[i]);
                } else {
                    break;
                }
            }
            for (auto it = tmp.begin(); it != tmp.end(); ++it) {
                values.insert(*it);
            }
        }
        lmax = *(values.rbegin());
        int res = acc - 2 * lmax;
        return res;
    }
};
