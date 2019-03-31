/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    // worst case is O(n) if all elements are same.
    bool search(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) return true;
        }
        return false;
    }
};
