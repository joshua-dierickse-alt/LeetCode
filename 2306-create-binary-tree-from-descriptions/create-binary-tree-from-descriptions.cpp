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

        unordered_set<int> s;
        for (const auto &d : descriptions) {
            s.insert(d[0]);
            s.insert(d[1]);
        }

        for (const auto &d : descriptions) {
            int p = d[0];
            int c = d[1];
            int is_left = d[2];

            s.erase(c);

            if (!m.contains(p) && !m.contains(c)) {
                m[c] = new TreeNode(c);
                m[p] = new TreeNode(p, is_left ? m[c] : nullptr, is_left ? nullptr : m[c]);
            } else if (!m.contains(c)) {
                TreeNode* &choice = is_left ? m[p]->left : m[p]->right;
                choice = new TreeNode(c);
                m[c] = choice;
            } else if (!m.contains(p)) {
                m[p] = new TreeNode(p, is_left ? m[c] : nullptr, is_left ? nullptr : m[c]);
            } else {
                TreeNode* &choice = is_left ? m[p]->left : m[p]->right;
                choice = m[c];
            }
        }

        int head = *s.begin();
        return m[head];
    }
};