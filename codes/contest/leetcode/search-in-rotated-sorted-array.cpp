/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    int search(vector<int>& nums, int target) {
        int size = nums.size();
        int s = 0, e = size - 1;
        while (s <= e) {
            int m = (s + e) / 2;
            if (nums[m] == target) return m;
            if (target > nums[m]) {
                if (nums[m] >= nums[s]) {
                    s = m + 1;
                } else if (target >= nums[s]) {
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            } else {
                if (nums[m] <= nums[e]) {
                    e = m - 1;
                } else if (target >= nums[s]) {
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            }
        }
        return -1;
    }
};
