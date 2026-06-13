class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string f(words.size(), '\0');

        for (size_t i = 0; i < words.size(); ++i) {
            int s = 0;

            for (char c : words[i])
                s = (s + weights[c - 'a']) % 26;
            
            f[i] = 'a' + (25 - s);
        }

        return f;
    }
};