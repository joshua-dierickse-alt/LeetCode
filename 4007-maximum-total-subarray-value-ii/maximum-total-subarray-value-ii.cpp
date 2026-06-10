int int_log(int v) {
    double x = std::log2(v);
    return static_cast<int>(x + 1e-9);
}

long long hash2(int x, int y) {
    return (static_cast<long long>(x) << 32) | static_cast<unsigned int>(y);
}

class Solution {
    vector<vector<int>> st_min;
    vector<vector<int>> st_max;

    int range_diff(int l, int r) {
        int j = int_log(r - l + 1);

        return max(st_max[j][l], st_max[j][r - (1 << j) + 1])
             - min(st_min[j][l], st_min[j][r - (1 << j) + 1]);
    }

public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();

        st_min.resize(int_log(n) + 1);
        st_max.resize(int_log(n) + 1);

        st_min[0] = nums;
        st_max[0] = std::move(nums);

        for (size_t i = 1, len = 2; i < st_min.size(); ++i, len <<= 1) {
            st_min[i].reserve(n - len + 1);
            st_max[i].reserve(n - len + 1);
            for (int k = 0; k < n - len + 1; ++k) {
                st_min[i].push_back(min(st_min[i - 1][k], st_min[i - 1][k + (len >> 1)]));
                st_max[i].push_back(max(st_max[i - 1][k], st_max[i - 1][k + (len >> 1)]));
            }
        }

        priority_queue<std::tuple<int, int, int>> max_heap;

        long long s = 0;

        unordered_set<long long> v;

        v.insert(hash2(0, n - 1));
        max_heap.push({range_diff(0, n - 1), 0, n - 1});

        while (k--) {
            auto [range, l, r] = max_heap.top();
            s += range;
            max_heap.pop();

            if (r != l) {
                if (!v.contains(hash2(l, r - 1))) {
                    v.insert(hash2(l, r - 1));
                    max_heap.push({range_diff(l, r - 1), l, r - 1});
                }
                if (!v.contains(hash2(l + 1, r))) {
                    v.insert(hash2(l + 1, r));
                    max_heap.push({range_diff(l + 1, r), l + 1, r});
                }
            }
        }

        return s;
    }
};