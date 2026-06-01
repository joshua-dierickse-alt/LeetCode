class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end(), greater<int>());

        int c = 0;

        for (size_t i = 0; i < cost.size(); ++i)
            if ((i + 1) % 3 != 0) c += cost[i];
        
        return c;
    }
};