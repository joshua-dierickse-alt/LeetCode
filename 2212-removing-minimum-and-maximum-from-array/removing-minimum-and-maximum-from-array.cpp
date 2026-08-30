class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int lower = 0;
        int upper = 0;

        for (int i = 0; i < n; ++i) {
            if (nums[lower] < nums[i]) lower = i;
            if (nums[upper] > nums[i]) upper = i;
        }

        if (lower > upper) swap(lower, upper);

        return min({upper + 1, n - lower, lower + 1 + n - upper});
    }
};