typedef priority_queue<int, vector<int>, greater<int>> MinHeap;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        const int N = nums.size();

        vector<pair<int, int>> nums_with_index;
        nums_with_index.reserve(N);
        
        vector<int> result(N);

        for (int i = 0; i < N; ++i)
            nums_with_index.emplace_back(nums[i], i);
        
        sort(nums_with_index.begin(), nums_with_index.end());

        int start = 0;
        int prev = nums_with_index[0].first;
        MinHeap heap;

        auto process_heap = [&]{
            const int size = heap.size();

            for (int i = 0; i < size; ++i) {
                result[heap.top()] = nums_with_index[start + i].first;
                heap.pop();
            }
        };

        for (int i = 0; i < nums_with_index.size(); ++i) {
            auto &[num, idx] = nums_with_index[i];

            if (num - prev > limit) {
                process_heap();
                start = i;
            }
            
            heap.push(idx);
            prev = num;
        }

        process_heap();

        return result;
    }
};