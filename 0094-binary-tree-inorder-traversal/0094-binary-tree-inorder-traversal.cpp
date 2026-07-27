/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>

class Solution {
public:
    void inorder(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) {
            return;
        }
        
        // 1. Traverse the left subtree
        inorder(node->left, result);
        
        // 2. Visit the root
        result.push_back(node->val);
        
        // 3. Traverse the right subtree
        inorder(node->right, result);
    }
    
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        inorder(root, result);
        return result;
    }
};