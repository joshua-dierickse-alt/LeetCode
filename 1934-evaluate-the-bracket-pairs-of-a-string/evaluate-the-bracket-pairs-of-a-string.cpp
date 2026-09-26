class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> pairs;

        for (const vector<string> &value_pair : knowledge) {
            pairs[value_pair[0]] = value_pair[1];
        }

        string result;
        string key;
        bool in_pair = false;

        for (char c : s) {
            if (c == ')') {
                in_pair = false;
                auto it = pairs.find(key);
                result += it == pairs.end() ? "?" : it->second;
                key = "";
            } else if (c == '(') {
                in_pair = true;
            } else if (in_pair) {
                key += c;
            } else {
                result += c;
            }
        }

        return result;
    }
};