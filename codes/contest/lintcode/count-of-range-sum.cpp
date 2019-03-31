/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

struct Node {
    int value;
    int height;
    int lenum;
    Node* left;
    Node* right;
    Node(int value) {
        this->value = value;
        height = 1;
        lenum = 1;
        left = NULL;
        right = NULL;
    }
};

int get_height(Node* root) {
    if (root == NULL) return 0;
    return root->height;
}

Node* left_rotate(Node* root) {
    Node* left = root->left;
    root->left = left->right;
    root->lenum = root->lenum - left->lenum;
    root->height = max(get_height(root->left), get_height(root->right)) + 1;
    left->right = root;
    left->height = max(get_height(left->left), get_height(left->right)) + 1;
    return left;
}

Node* right_rotate(Node* root) {
    Node* right = root->right;
    root->right = right->left;
    root->height = max(get_height(root->left), get_height(root->right)) + 1;
    right->lenum = right->lenum + root->lenum;
    right->left = root;
    right->height = max(get_height(right->left), get_height(right->right)) + 1;
    return right;
}

Node* balance(Node* root) {
    int lh = get_height(root->left);
    int rh = get_height(root->right);

    if ((lh - rh) >= 2) {
        int llh = get_height(root->left->left);
        int lrh = get_height(root->left->right);
        if (lrh > llh) {
            root->left = right_rotate(root->left);
        }
        root = left_rotate(root);
    } else if ((rh - lh) >= 2) {
        int rlh = get_height(root->right->left);
        int rrh = get_height(root->right->right);
        if (rlh > rrh) {
            root->right = left_rotate(root->right);
        }
        root = right_rotate(root);
    } else {
        root->height = max(lh, rh) + 1;
    }
    return root;
}

Node* insert_node(Node* root, int value) {
    if (root == NULL) {
        Node* node = new Node(value);
        return node;
    }

    if (root->value == value) {
        root->lenum += 1;
    } else if (root->value > value) {
        root->left = insert_node(root->left, value);
        root->lenum += 1;
    } else {
        root->right = insert_node(root->right, value);
    }
    root = balance(root);
    return root;
}

int query(Node* root, int value) {
    if (root == NULL) {
        return 0;
    }
    if (root->value == value) {
        return root->lenum;
    } else if (root->value > value) {
        return query(root->left, value);
    } else {
        int count = query(root->right, value);
        count += root->lenum;
        return count;
    }
}

class Solution {
   public:
    /**
     * @param nums: a list of integers
     * @param lower: a integer
     * @param upper: a integer
     * @return: return a integer
     */
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        // write your code here
        Node* root = NULL;

        int acc = 0;
        int res = 0;
        for (size_t i = 0; i < nums.size(); i++) {
            int num = nums[i];
            acc += num;
            int lo = query(root, acc - upper - 1);
            int hi = query(root, acc - lower);
            res += (hi - lo);
            root = insert_node(root, acc);
            if (acc >= lower && acc <= upper) {
                res += 1;
            }
        }
        return res;
    }
};
