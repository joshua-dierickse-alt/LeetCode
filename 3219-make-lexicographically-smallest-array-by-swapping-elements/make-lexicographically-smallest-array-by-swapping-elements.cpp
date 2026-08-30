class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<pair<int, int>> nums_with_index;
        nums_with_index.reserve(nums.size());

        for (int i = 0; i < nums.size(); ++i)
            nums_with_index.emplace_back(nums[i], i);
        
        sort(nums_with_index.begin(), nums_with_index.end());

        int prev = -pow(10, 9) - 10;
        vector<priority_queue<int, vector<int>, greater<int>>> heaps;

        for (auto &[num, i] : nums_with_index) {
            if (num - prev > limit) {
                heaps.emplace_back();
            }
            heaps[heaps.size() - 1].push(i);
            i = heaps.size() - 1;
            prev = num;
        }

        for (auto &[num, i] : nums_with_index) {
            nums[heaps[i].top()] = num;
            heaps[i].pop();
        }

        return nums;
    }
};