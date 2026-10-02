class Solution {
    vector<string> result;

    void dfs(int open, int closed, string &cur) {
        if (closed == 0) {
            result.push_back(cur);
            return;
        }

        if (open > 0) {
            cur += "(";
            dfs(open - 1, closed, cur);
            cur.pop_back();
        }
        if (closed > open) {
            cur += ")";
            dfs(open, closed - 1, cur);
            cur.pop_back();
        }
    }

public:
    vector<string> generateParenthesis(int n) {
        result.clear();

        string cur;

        dfs(n, n, cur);

        return result;
    }
};