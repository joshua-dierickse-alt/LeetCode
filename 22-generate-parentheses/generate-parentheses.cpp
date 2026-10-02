class Solution {
    string cur;
    vector<string> result;

    void dfs(const int open, const int closed) {
        if (closed == 0) {
            result.push_back(cur);
            return;
        }

        if (open > 0) {
            cur += "(";
            dfs(open - 1, closed);
            cur.pop_back();
        }
        if (closed > open) {
            cur += ")";
            dfs(open, closed - 1);
            cur.pop_back();
        }
    }

public:
    vector<string> generateParenthesis(int n) {
        dfs(n, n);

        return result;
    }
};