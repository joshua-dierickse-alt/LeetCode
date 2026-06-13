class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string f;

        for (const string &word : words) {
            int s = 0;

            for (char c : word)
                s = (s + weights[static_cast<int>(c) - 97]) % 26;
            
            f += static_cast<char>(97 + (25 - s));
        }

        return f;
    }
};