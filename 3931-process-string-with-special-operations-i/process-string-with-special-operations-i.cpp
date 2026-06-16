class Solution {
public:
    string processStr(string s) {
        string n;

        for (char c : s) {
            if (c == '*') { if (n.size()) n.pop_back(); }
            else if (c == '#') n += n;
            else if (c == '%') reverse(n.begin(), n.end());
            else n += c;
        }

        return n;
    }
};