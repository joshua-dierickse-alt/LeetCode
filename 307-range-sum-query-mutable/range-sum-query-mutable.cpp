class NumArray {
public:
    vector<int> nums;
    vector<int> fenwick;

    NumArray(vector<int>& n) : nums(n), fenwick(n.size()) {
        int s = 0;
        vector<int> prefix_sum(nums.size() + 1);
        for (int i = 0; i < nums.size(); ++i) {
            s += nums[i];
            prefix_sum[i + 1] = s;
        }

        for (int i = 1; i <= nums.size(); ++i) {
            int k = i & -i;
            fenwick[i - 1] = prefix_sum[i] - prefix_sum[i - k];
        }
    }
    
    void update(int index, int val) {
        int diff = val - nums[index];

        int i = index + 1;
        while (i <= nums.size()) {
            fenwick[i - 1] += diff;
            i += i & -i;
        }

        nums[index] = val;
    }

    int sumRange(int r) {
        int s = 0;
        r += 1;

        while (r) {
            s += fenwick[r - 1];
            r -= r & -r;
        }

        return s;
    }
    
    int sumRange(int left, int right) {
        return sumRange(right) - sumRange(left - 1);
    }
};
