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
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> m;
        m.reserve(descriptions.size() * 1.5);

        int root = 0;

        for (const auto &d : descriptions) {
            int p = d[0];
            int c = d[1];
            int is_left = d[2];

            if (!m.contains(p)) { 
                m[p] = new TreeNode(p);
                root ^= p;
            }
            if (!m.contains(c)) {
                m[c] = new TreeNode(c);
                root ^= c;
            }

            if (is_left) m[p]->left = m[c];
            else m[p]->right = m[c];

            root ^= c;
        }

        return m[root];
    }
};