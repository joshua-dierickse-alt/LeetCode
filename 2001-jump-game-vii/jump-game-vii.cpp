class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        size_t n = s.length();
        
        if (s[n - 1] == '1') return false;

        size_t check_next = 0;
        s[0] = '2';

        for (size_t i = 0; i < n; ++i) {
            if (i + maxJump < check_next || s[i] != '2') continue;

            size_t lower_bound = max(i + minJump, check_next);
            size_t upper_bound = min(i + maxJump, n - 1);

            if (lower_bound <= n - 1 && n - 1 <= upper_bound) return true;

            for (size_t j = lower_bound; j <= upper_bound; ++j)
                if (s[j] == '0') s[j] = '2';

            check_next = i + maxJump + 1;
        }

        return false;
    }
};