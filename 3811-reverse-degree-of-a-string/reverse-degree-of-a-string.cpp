class Solution {
public:
    int reverseDegree(string s) {
        int result = 0;

        for (int i = 0; i < s.size(); ++i) {
            result += (i + 1) * (1 + 'z' - s[i]); 
        }

        return result;
    }
};