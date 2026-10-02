vector<string> result;

void dfs(int open, int closed, string cur) {
    if (closed == 0) {
        result.push_back(cur);
        return;
    }

    if (open == closed) {
        dfs(open - 1, closed, cur + "(");
    }
    else {
        if (open > 0) dfs(open - 1, closed, cur + "(");
        dfs(open, closed - 1, cur + ")");
    }
}

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        result.clear();

        dfs(n, n, "");

        return result;
    }
};