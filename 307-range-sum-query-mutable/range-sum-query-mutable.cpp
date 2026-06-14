class NumArray {
public:
    vector<int> nums;
    vector<int> fenwick;

    NumArray(vector<int>& n) : nums(n), fenwick(n.size(), 0) {
        for (size_t i = 1; i <= nums.size(); ++i) {
            int k = 1;
            while (i % k == 0) k <<= 1;
            k >>= 1;
            int s = 0;
            for (int j = 0; j < k; ++j) s += nums[(i - 1) - j];
            fenwick[i - 1] = s;
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
