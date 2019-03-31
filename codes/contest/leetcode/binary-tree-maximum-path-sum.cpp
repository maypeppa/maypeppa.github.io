/* coding:utf-8
 * Copyright (C) dirlt
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <algorithm>
#include <climits>
#include <cstdio>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
};

class Solution {
   public:
    // 返回包含必须root节点的最大值
    // kmax 表示当前已知的最大值
    int trace(TreeNode* root, int* kmax) {
        int R = INT_MIN;
        if (root == NULL) {
            *kmax = R;
            return 0;
        }

        int lkmax = 0;
        int lv = trace(root->left, &lkmax);
        int rkmax = 0;
        int rv = trace(root->right, &rkmax);

        // value包括
        // root, root + lv, root + rv
        // kmax包括
        // lkmax, rkmax, root + lv, root + rv, root + lv + rv, root
        int value = max(0, max(lv, rv)) + root->val;
        *kmax = max(value, max(lv + rv + root->val, max(lkmax, rkmax)));
        return value;
    }
    int maxPathSum(TreeNode* root) {
        int kmax = 0;
        trace(root, &kmax);
        return kmax;
    }
};
