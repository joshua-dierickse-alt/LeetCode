class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);

        int acc = 0;
        for (int i = n - 1; i >= 0; --i) {
            res[i] = acc;
            acc += nums[i];
        }

        acc = 0;
        for (int i = 0; i < n; ++i) {
            res[i] = abs(acc - res[i]);
            acc += nums[i];
        }

        return res;
    }
};