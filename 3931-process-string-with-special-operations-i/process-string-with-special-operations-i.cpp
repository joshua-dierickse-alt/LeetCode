void reverse(string &s) {
    for (size_t i = 0; i < s.size() / 2; ++i)
        swap(s[i], s[s.size() - i - 1]);
}

class Solution {
public:
    string processStr(string s) {
        string n;

        for (char c : s) {
            if (c == '*') { if (n.size()) n.pop_back(); }
            else if (c == '#') n += n;
            else if (c == '%') reverse(n);
            else n += c;
        }

        return n;
    }
};