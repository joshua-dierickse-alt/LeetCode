typedef priority_queue<int, vector<int>, greater<int>> MinHeap;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<pair<int, int>> nums_with_index(nums.size());
        vector<int> result(nums.size());

        for (int i = 0; i < nums.size(); ++i)
            nums_with_index[i] = pair<int, int>(nums[i], i);
        
        sort(nums_with_index.begin(), nums_with_index.end());

        int start = 0;
        int count = 0;
        int prev = nums_with_index[0].first;
        MinHeap heap;

        auto process_heap = [&]{
            const int size = heap.size();

            for (int i = 0; i < size; ++i) {
                result[heap.top()] = nums_with_index[start + i].first;
                heap.pop();
            }
            start = count;
        };

        for (auto &[num, i] : nums_with_index) {
            if (num - prev > limit) {
                process_heap();
            }
            heap.push(i);
            prev = num;
            ++count;
        }

        process_heap();

        return result;
    }
};